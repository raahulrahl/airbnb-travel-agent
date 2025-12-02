"""Airbnb Travel Agent - An intelligent AI-powered travel assistant.

This package helps users discover and plan their perfect accommodations using
real-time Airbnb listings and Google Maps location data.
"""

from airbnb_travel_agent.__version__ import __version__
from airbnb_travel_agent.main import (
    handler,
    initialize_agent,
    initialize_all,
    initialize_mcp_tools,
    main,
)

__all__ = [
    "__version__",
    "handler",
    "initialize_agent",
    "initialize_all",
    "initialize_mcp_tools",
    "main",
]
