"""
Pytest configuration and fixtures for the test suite.
"""

import os
import pytest
from unittest.mock import Mock, patch
from typing import Generator


@pytest.fixture
def mock_azure_credentials():
    """Mock Azure credentials for testing."""
    with patch('azure.identity.AzureCliCredential') as mock_credential:
        mock_credential.return_value = Mock()
        yield mock_credential


@pytest.fixture
def mock_env_vars():
    """Mock environment variables for testing."""
    original_env = os.environ.copy()
    os.environ.update({
        'AZURE_AI_PROJECT_ENDPOINT': 'https://test.endpoint.com',
        'AZURE_AI_MODEL_DEPLOYMENT_NAME': 'test-model',
        'AZURE_SEARCH_SERVICE_ENDPOINT': 'https://test.search.com',
        'AZURE_SEARCH_API_KEY': 'test-key',
        'GITHUB_TOKEN': 'test-github-token',
        'GITHUB_ENDPOINT': 'https://models.inference.ai.azure.com',
        'GITHUB_MODEL_ID': 'gpt-4o-mini'
    })
    yield
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def sample_agent_response():
    """Sample agent response for testing."""
    return {
        "content": "This is a test response from the AI agent.",
        "role": "assistant",
        "finish_reason": "stop"
    }
