# GitHub Actions Workflows

## Overview

This directory contains GitHub Actions workflows for CI/CD automation.

## Workflows

### 1. `main.yml` - Main CI Pipeline
Runs on every push and pull request to validate code quality:
- **Quality checks**: Linting and code formatting
- **Tests**: Unit tests with coverage reporting
- **Type checking**: Static type analysis
- **Documentation**: Validates documentation builds

### 2. `build-and-push.yml` - Docker Build & Deploy
Runs on push to `main` branch when relevant files change:
- **Validation**: Runs all quality checks, tests, and documentation builds
- **Docker Build**: Builds multi-platform Docker images (amd64, arm64)
- **Docker Push**: Pushes to Docker Hub with version tags

**Triggers:**
- Push to `main` branch
- Changes to: `Dockerfile.agent`, `airbnb_travel_agent/**`, `pyproject.toml`, `uv.lock`, `.version`
- Manual workflow dispatch

**Docker Images:**
- `raahulrahl/airbnb-travel-agent:latest`
- `raahulrahl/airbnb-travel-agent:<version>` (from `.version` file)

### 3. `validate-codecov-config.yml` - Codecov Validation
Validates Codecov configuration.

## Required Secrets

Configure these in GitHub repository settings → Secrets and variables → Actions:

| Secret | Description | Required For |
|--------|-------------|--------------|
| `DOCKERHUB_TOKEN` | Docker Hub access token | `build-and-push.yml` |
| `CODECOV_TOKEN` | Codecov upload token | `main.yml` |

## Version Management

The Docker image version is managed via the `.version` file in the repository root. Update this file to change the version tag for Docker images.

Current version: `0.1.0`

## Manual Workflow Dispatch

You can manually trigger the `build-and-push.yml` workflow from the GitHub Actions tab:
1. Go to Actions → Build and Push to Docker Hub
2. Click "Run workflow"
3. Select branch and click "Run workflow"
