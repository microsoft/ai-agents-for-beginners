#!/usr/bin/env python3
"""
Client Utilities for MCP Session Management

This module provides utilities for managing MCP client sessions,
including token persistence and session resumption.
"""

import json
import os
from typing import Optional, Dict, Any

from rich.console import Console

# Import shared constants locally
DEFAULT_TOKEN_FILE = "resumption_tokens.json"

console = Console()


def cast_input_value(value: str, prop_info: dict):
    """Cast input value to the correct type based on schema property info."""
    if not value:
        return value
    
    prop_type = prop_info.get("type", "string")
    
    try:
        if prop_type == "integer":
            return int(value)
        elif prop_type == "number":
            return float(value)
        elif prop_type == "boolean":
            return value.lower() in ['true', 't', 'yes', 'y', '1']
        else:  # string or other types
            return value
    except ValueError:
        # If casting fails, return the original string
        return value


class TokenManager:
    """Manages resumption tokens and session information."""
    
    def __init__(self, token_file: str = DEFAULT_TOKEN_FILE):
        self.token_file = token_file
    
    def save_tokens(self, session_id: str, resumption_token: str, protocol_version: Optional[str] = None, 
                   last_tool: Optional[str] = None, last_args: Optional[dict] = None) -> bool:
        """Save session ID, resumption token, protocol version, and last tool info to file.
        
        Only creates a token file when we have an actual resumption token from the server.
        Never creates empty or placeholder token files.
        """
        # Validate that we have real tokens, not placeholders
        if not session_id or not resumption_token:
            console.print(f"[red]✗ Cannot save tokens: missing session_id or resumption_token[/red]")
            return False
            
        if resumption_token.startswith("pending_") or resumption_token.startswith("temp_"):
            console.print(f"[red]✗ Cannot save placeholder token: {resumption_token}[/red]")
            return False
        
        data: Dict[str, Any] = {
            "session_id": session_id,
            "resumption_token": resumption_token,
        }
        if protocol_version:
            data["protocol_version"] = protocol_version
        if last_tool:
            data["last_tool"] = last_tool
        if last_args:
            data["last_args"] = last_args
        
        try:
            with open(self.token_file, 'w') as f:
                json.dump(data, f, indent=2)
            console.print(f"[green]✓ Saved resumption token to {self.token_file}[/green]")
            return True
        except Exception as e:
            console.print(f"[red]✗ Failed to save tokens: {e}[/red]")
            return False
    
    def load_tokens(self) -> Optional[Dict[str, Any]]:
        """Load session ID, resumption token, and tool info from file."""
        if not os.path.exists(self.token_file):
            console.print(f"[yellow]No resumption token file found ({self.token_file})[/yellow]")
            return None
            
        try:
            with open(self.token_file, 'r') as f:
                data = json.load(f)
            
            if "session_id" in data and "resumption_token" in data:
                console.print(f"[cyan]📄 Found resumption tokens in {self.token_file}[/cyan]")
                console.print(f"[cyan]   Session ID: {data['session_id']}[/cyan]")
                console.print(f"[cyan]   Token: {data['resumption_token'][:20]}...[/cyan]")
                if "last_tool" in data:
                    console.print(f"[cyan]   Last Tool: {data['last_tool']}[/cyan]")
                return data
            else:
                console.print(f"[yellow]Invalid token file format[/yellow]")
                return None
                
        except Exception as e:
            console.print(f"[red]✗ Failed to load tokens: {e}[/red]")
            return None
    
    def delete_tokens(self) -> bool:
        """Delete the resumption token file."""
        try:
            if os.path.exists(self.token_file):
                os.remove(self.token_file)
                return True
            else:
                return False
        except Exception as e:
            console.print(f"[red]✗ Failed to delete token file: {e}[/red]")
            return False
