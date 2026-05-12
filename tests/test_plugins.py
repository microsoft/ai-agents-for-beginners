"""
Tests for demo tool agent plugins.
"""

import pytest
from datetime import datetime
import sys
import os

# Add the code_samples directory to the path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '04-tool-use', 'code_samples'))

from demo_tool_agent import TimePlugin, CalculatorPlugin


class TestTimePlugin:
    """Test cases for TimePlugin class."""
    
    def test_get_current_time_format(self):
        """Test that get_current_time returns correct format."""
        plugin = TimePlugin()
        time_str = plugin.get_current_time()
        
        # Check format: YYYY-MM-DD HH:MM:SS (19 characters)
        assert len(time_str) == 19
        assert time_str[4] == '-'
        assert time_str[7] == '-'
        assert time_str[10] == ' '
        assert time_str[13] == ':'
        assert time_str[16] == ':'
        
        # Verify it's a valid datetime
        datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    
    def test_get_time_zone_default(self):
        """Test get_time_zone with default timezone."""
        plugin = TimePlugin()
        time_str = plugin.get_time_zone()
        
        assert "UTC" in time_str
        assert len(time_str) > 19  # Should include timezone info
    
    def test_get_time_zone_custom(self):
        """Test get_time_zone with custom timezone."""
        plugin = TimePlugin()
        time_str = plugin.get_time_zone("EST")
        
        assert "EST" in time_str
        assert len(time_str) > 19


class TestCalculatorPlugin:
    """Test cases for CalculatorPlugin class."""
    
    def test_add_integers(self):
        """Test addition with integers."""
        plugin = CalculatorPlugin()
        result = plugin.add(5, 7)
        assert result == 12
        assert isinstance(result, int)
    
    def test_add_floats(self):
        """Test addition with floats."""
        plugin = CalculatorPlugin()
        result = plugin.add(5.5, 7.3)
        assert result == 12.8
        assert isinstance(result, float)
    
    def test_add_mixed(self):
        """Test addition with mixed types."""
        plugin = CalculatorPlugin()
        result = plugin.add(5, 7.5)
        assert result == 12.5
        assert isinstance(result, float)
    
    def test_subtract_integers(self):
        """Test subtraction with integers."""
        plugin = CalculatorPlugin()
        result = plugin.subtract(10, 4)
        assert result == 6
        assert isinstance(result, int)
    
    def test_subtract_floats(self):
        """Test subtraction with floats."""
        plugin = CalculatorPlugin()
        result = plugin.subtract(10.5, 4.2)
        assert result == 6.3
        assert isinstance(result, float)
    
    def test_multiply_integers(self):
        """Test multiplication with integers."""
        plugin = CalculatorPlugin()
        result = plugin.multiply(3, 4)
        assert result == 12
        assert isinstance(result, int)
    
    def test_multiply_floats(self):
        """Test multiplication with floats."""
        plugin = CalculatorPlugin()
        result = plugin.multiply(2.5, 4.0)
        assert result == 10.0
        assert isinstance(result, float)
    
    def test_divide_integers(self):
        """Test division with integers."""
        plugin = CalculatorPlugin()
        result = plugin.divide(12, 3)
        assert result == 4.0
        assert isinstance(result, float)
    
    def test_divide_floats(self):
        """Test division with floats."""
        plugin = CalculatorPlugin()
        result = plugin.divide(5.5, 2.0)
        assert result == 2.75
        assert isinstance(result, float)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        plugin = CalculatorPlugin()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            plugin.divide(5, 0)
