"""
Demo tool agent plugins for testing purposes.
These are extracted from the 04-python-agent-framework.ipynb notebook.
"""

from datetime import datetime
from typing import Union


class TimePlugin:
    """Plugin for time-related operations."""
    
    def get_current_time(self) -> str:
        """Get the current time in YYYY-MM-DD HH:MM:SS format."""
        now: datetime = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
    
    def get_time_zone(self, timezone: str = "UTC") -> str:
        """Get time in a specific timezone (simplified implementation)."""
        # This is a simplified implementation - in production, you'd use pytz or similar
        now: datetime = datetime.now()
        return f"{now.strftime('%Y-%m-%d %H:%M:%S')} ({timezone})"


class CalculatorPlugin:
    """Plugin for basic arithmetic operations."""
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        result: Union[int, float] = a + b
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a."""
        result: Union[int, float] = a - b
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        result: Union[int, float] = a * b
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result: Union[int, float] = a / b
        return result
