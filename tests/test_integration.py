"""
Integration tests for Azure AI services and agent framework.
"""

import pytest
import os
from unittest.mock import Mock, patch, AsyncMock
import sys
from pathlib import Path

# Add code samples to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "04-tool-use" / "code_samples"))


class TestAzureIntegration:
    """Test Azure AI service integrations."""
    
    @pytest.mark.asyncio
    async def test_azure_provider_creation(self, mock_azure_credentials, mock_env_vars):
        """Test Azure AI provider can be created with mocked credentials."""
        with patch('agent_framework.azure.AzureAIProjectAgentProvider') as mock_provider:
            mock_instance = Mock()
            mock_provider.return_value = mock_instance
            
            # This would normally create the provider
            from agent_framework.azure import AzureAIProjectAgentProvider
            from azure.identity import AzureCliCredential
            
            provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
            
            assert provider is not None
            mock_provider.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_agent_creation_with_tools(self, mock_azure_credentials, mock_env_vars):
        """Test agent creation with tools."""
        with patch('agent_framework.azure.AzureAIProjectAgentProvider') as mock_provider_class:
            mock_provider = Mock()
            mock_agent = Mock()
            mock_provider.create_agent = AsyncMock(return_value=mock_agent)
            mock_provider_class.return_value = mock_provider
            
            from agent_framework.azure import AzureAIProjectAgentProvider
            from azure.identity import AzureCliCredential
            from agent_framework import tool
            
            # Define a test tool
            @tool(approval_mode="never_require")
            def test_tool():
                """Test tool."""
                return "test result"
            
            # Create provider and agent
            provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
            agent = await provider.create_agent(
                name="TestAgent",
                instructions="Test instructions",
                tools=[test_tool]
            )
            
            assert agent is not None
            mock_provider.create_agent.assert_called_once()


class TestEnvironmentConfiguration:
    """Test environment configuration and validation."""
    
    def test_required_env_vars_present(self, mock_env_vars):
        """Test that required environment variables are set."""
        required_vars = [
            'AZURE_AI_PROJECT_ENDPOINT',
            'AZURE_AI_MODEL_DEPLOYMENT_NAME'
        ]
        
        for var in required_vars:
            assert os.getenv(var), f"Required environment variable {var} is not set"
    
    def test_optional_env_vars_validation(self, mock_env_vars):
        """Test optional environment variables validation."""
        optional_vars = [
            'AZURE_SEARCH_SERVICE_ENDPOINT',
            'AZURE_SEARCH_API_KEY',
            'GITHUB_TOKEN',
            'GITHUB_ENDPOINT',
            'GITHUB_MODEL_ID'
        ]
        
        # These should be set in our mock, but in real usage they're optional
        for var in optional_vars:
            assert os.getenv(var) is not None, f"Optional environment variable {var} should be set for testing"


class TestPluginIntegration:
    """Test integration of plugins with agent framework."""
    
    def test_plugin_import_and_usage(self):
        """Test that plugins can be imported and used."""
        from demo_tool_agent import TimePlugin, CalculatorPlugin
        
        # Test TimePlugin
        time_plugin = TimePlugin()
        time_result = time_plugin.get_current_time()
        assert isinstance(time_result, str)
        assert len(time_result) == 19
        
        # Test CalculatorPlugin
        calc_plugin = CalculatorPlugin()
        calc_result = calc_plugin.add(2, 3)
        assert calc_result == 5
    
    def test_plugin_error_handling(self):
        """Test plugin error handling."""
        from demo_tool_agent import CalculatorPlugin
        
        calc_plugin = CalculatorPlugin()
        
        # Test division by zero
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc_plugin.divide(10, 0)
