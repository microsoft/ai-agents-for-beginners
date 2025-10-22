#!/usr/bin/env python3
"""
Event Store Implementation for MCP Session Resumption

This module provides an in-memory event store that enables MCP session resumption
by storing and replaying events after client reconnection.
"""

import logging
from typing import Optional

from mcp.server.streamable_http import (
    EventCallback,
    EventId,
    EventMessage,
    EventStore,
    StreamId,
)
from mcp.types import JSONRPCMessage

logger = logging.getLogger(__name__)


class SimpleEventStore(EventStore):
    """Simple in-memory event store for testing resumption functionality."""

    def __init__(self):
        self._events: list[tuple[StreamId, EventId, JSONRPCMessage]] = []
        self._event_id_counter = 0
        logger.info("SimpleEventStore initialized")

    async def store_event(self, stream_id: StreamId, message: JSONRPCMessage) -> EventId:
        """Store an event and return its ID."""
        self._event_id_counter += 1
        event_id = str(self._event_id_counter)
        self._events.append((stream_id, event_id, message))
        logger.info(f"Stored event {event_id} for stream {stream_id}")
        return event_id

    async def replay_events_after(
        self,
        last_event_id: EventId,
        send_callback: EventCallback,
    ) -> StreamId | None:
        """Replay events after the specified ID."""
        logger.info(f"Replaying events after {last_event_id}")
        
        # Find the index of the last event ID
        start_index = None
        for i, (_, event_id, _) in enumerate(self._events):
            if event_id == last_event_id:
                start_index = i + 1
                break

        if start_index is None:
            # If event ID not found, start from beginning
            start_index = 0
            logger.info("Event ID not found, starting from beginning")

        stream_id = None
        # Replay events
        replayed_count = 0
        for _, event_id, message in self._events[start_index:]:
            await send_callback(EventMessage(message, event_id))
            replayed_count += 1
            # Capture the stream ID from the first replayed event
            if stream_id is None and len(self._events) > start_index:
                stream_id = self._events[start_index][0]

        logger.info(f"Replayed {replayed_count} events, stream_id: {stream_id}")
        return stream_id

    def get_event_count(self) -> int:
        """Get the total number of stored events."""
        return len(self._events)

    def clear_events(self) -> None:
        """Clear all stored events."""
        self._events.clear()
        self._event_id_counter = 0
        logger.info("Event store cleared")


class PersistentEventStore(EventStore):
    """
    Event store that persists events to disk.
    
    Note: This is a placeholder for future implementation.
    In production, you would want to use a proper database.
    """
    
    def __init__(self, storage_path: str = "events.db"):
        self.storage_path = storage_path
        # TODO: Implement persistent storage
        raise NotImplementedError("Persistent event store not yet implemented")
    
    async def store_event(self, stream_id: StreamId, message: JSONRPCMessage) -> EventId:
        raise NotImplementedError()
    
    async def replay_events_after(
        self,
        last_event_id: EventId,
        send_callback: EventCallback,
    ) -> StreamId | None:
        raise NotImplementedError()
