from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from airbnb_travel_agent.main import handler


@pytest.mark.asyncio
async def test_handler_returns_response():
    """Test that handler accepts messages and returns a response."""
    messages = [{"role": "user", "content": "Hello, how are you?"}]

    # Mock the agent.arun method to return a mock response
    mock_response = MagicMock()
    mock_response.run_id = "test-run-id"
    mock_response.status = "COMPLETED"

    mock_agent = MagicMock()
    mock_agent.arun = AsyncMock(return_value=mock_response)

    # Mock _initialized to skip initialization and agent to return our mock
    with (
        patch("airbnb_travel_agent.main._initialized", True),
        patch("airbnb_travel_agent.main.agent", mock_agent),
    ):
        result = await handler(messages)

    # Verify we get a result back
    assert result is not None
    assert result.run_id == "test-run-id"
    assert result.status == "COMPLETED"


@pytest.mark.asyncio
async def test_handler_with_multiple_messages():
    """Test that handler processes multiple messages correctly."""
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the weather?"},
    ]

    mock_response = MagicMock()
    mock_response.run_id = "test-run-id-2"

    mock_agent = MagicMock()
    mock_agent.arun = AsyncMock(return_value=mock_response)

    with (
        patch("airbnb_travel_agent.main._initialized", True),
        patch("airbnb_travel_agent.main.agent", mock_agent),
    ):
        result = await handler(messages)

    # Verify agent.arun was called
    mock_agent.arun.assert_called_once_with(messages)
    assert result is not None
    assert result.run_id == "test-run-id-2"


@pytest.mark.asyncio
async def test_handler_initialization():
    """Test that handler initializes on first call."""
    messages = [{"role": "user", "content": "Test"}]

    mock_response = MagicMock()
    mock_agent = MagicMock()
    mock_agent.arun = AsyncMock(return_value=mock_response)

    # Start with _initialized as False to test initialization path
    with (
        patch("airbnb_travel_agent.main._initialized", False),
        patch("airbnb_travel_agent.main.initialize_all", new_callable=AsyncMock) as mock_init,
        patch("airbnb_travel_agent.main.agent", mock_agent),
        patch("airbnb_travel_agent.main._init_lock"),
    ):
        result = await handler(messages)

        # Verify initialization was called
        mock_init.assert_called_once()
        # Verify agent.arun was called with messages
        mock_agent.arun.assert_called_once_with(messages)
        assert result == mock_response
