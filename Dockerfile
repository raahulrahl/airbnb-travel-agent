FROM ghcr.io/astral-sh/uv:alpine AS builder

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
ENV UV_PYTHON_INSTALL_DIR=/python
ENV UV_PYTHON_PREFERENCE=only-managed

RUN uv python install 3.12

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

FROM node:22-alpine AS node-base

FROM alpine:3.19

# OCI labels
LABEL org.opencontainers.image.title="airbnb-travel-agent"
LABEL org.opencontainers.image.description="An intelligent AI-powered travel assistant that helps users discover and plan their perfect accommodations using real-time Airbnb listings and Google Maps location data."
LABEL org.opencontainers.image.authors="raahul dutta <raahul@getbindu.com>"
LABEL org.opencontainers.image.version="0.0.1"
LABEL org.opencontainers.image.source="https://github.com/raahulrahl/airbnb-travel-agent"
LABEL org.opencontainers.image.licenses="MIT"

# Copy Python from builder
COPY --from=builder /python /python

# Copy Node.js from node-base
COPY --from=node-base /usr/local/bin/node /usr/local/bin/
COPY --from=node-base /usr/local/lib/node_modules /usr/local/lib/node_modules
RUN ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm && \
    ln -s /usr/local/lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx

# Copy the application with virtual environment from the builder
COPY --from=builder /app /app

# Add Python and venv to PATH
ENV PATH="/python/bin:/app/.venv/bin:$PATH"

# Use /app as the working directory
WORKDIR /app
EXPOSE 3773

# Run the application
CMD ["python", "-m", "airbnb_travel_agent.main"]
