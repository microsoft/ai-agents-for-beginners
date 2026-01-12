#!/usr/bin/env python3
"""
Event Store Implementation for MCP Session Resumption

This module provides event store implementations that enable MCP session resumption
by storing and replaying events after client reconnection.
"""

import asyncio
import logging
import sqlite3
from typing import Optional

from pydantic import TypeAdapter

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
    Event store that persists events to disk using SQLite.
    """
    
    def __init__(self, storage_path: str = "events.db") -> None:
        self.storage_path = storage_path
        self._adapter = TypeAdapter(JSONRPCMessage)

        # Use check_same_thread=False to allow access from asyncio executor threads
        self._conn = sqlite3.connect(self.storage_path, check_same_thread=False)
        self._create_table()
        logger.info(f"PersistentEventStore initialized with {self.storage_path}")

    def _create_table(self) -> None:
        """Create the events table if it doesn't exist."""
        cursor = self._conn.cursor()
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    stream_id TEXT NOT NULL,
                    message TEXT NOT NULL
                )
            """)
            self._conn.commit()
        except sqlite3.Error:
            logger.exception("Failed to create 'events' table in PersistentEventStore")
            try:
                self._conn.close()
            except Exception:
                logger.exception("Failed to close SQLite connection after table creation error")
            raise
        finally:
            try:
                cursor.close()
            except Exception:
                logger.exception("Failed to close SQLite cursor after table creation")
    
    async def store_event(self, stream_id: StreamId, message: JSONRPCMessage) -> EventId:
        """Store an event and return its ID."""
        # Serialize message to JSON
        json_str = self._adapter.dump_json(message).decode('utf-8')

        # Run DB operation in thread pool to avoid blocking event loop
        return await asyncio.to_thread(self._store_event_sync, stream_id, json_str)

    def _store_event_sync(self, stream_id: StreamId, json_str: str) -> EventId:
        cursor = self._conn.cursor()
        cursor.execute(
            "INSERT INTO events (stream_id, message) VALUES (?, ?)",
            (stream_id, json_str)
        )
        self._conn.commit()

        event_id = str(cursor.lastrowid)
        logger.info(f"Stored event {event_id} for stream {stream_id}")
        return event_id
    
    async def replay_events_after(
        self,
        last_event_id: EventId,
        send_callback: EventCallback,
    ) -> StreamId | None:
        """Replay events after the specified ID, filtered by the stream of the last event."""
        logger.info(f"Replaying events after {last_event_id}")

        # Fetch events in thread pool
        events_data = await asyncio.to_thread(self._fetch_events_sync, last_event_id)

        if events_data is None:
            logger.warning(f"Could not resume stream from event {last_event_id}")
            return None

        stream_id = None
        replayed_count = 0

        for event_id, row_stream_id, message_json in events_data:
            if stream_id is None:
                stream_id = row_stream_id

            try:
                message = self._adapter.validate_json(message_json)
                await send_callback(EventMessage(message, event_id))
                replayed_count += 1
            except Exception as e:
                logger.error(f"Failed to deserialize event {event_id}: {e}")

        logger.info(f"Replayed {replayed_count} events for stream {stream_id}")
        return stream_id

    def _fetch_events_sync(self, last_event_id: EventId) -> list[tuple[EventId, StreamId, str]] | None:
        try:
            target_id = int(last_event_id)
        except (ValueError, TypeError):
            logger.warning(f"Invalid event ID format: {last_event_id}")
            return None

        cursor = self._conn.cursor()

        # 1. Identify the stream from the last event ID
        cursor.execute("SELECT stream_id FROM events WHERE id = ?", (target_id,))
        result = cursor.fetchone()

        if not result:
            logger.warning(f"Event ID {target_id} not found")
            return None

        stream_id = result[0]

        # 2. Fetch subsequent events for THIS STREAM ONLY
        cursor.execute(
            "SELECT id, stream_id, message FROM events WHERE id > ? AND stream_id = ? ORDER BY id ASC",
            (target_id, stream_id)
        )

        # Convert rows to list of (str_id, stream_id, msg_json)
        return [(str(row[0]), row[1], row[2]) for row in cursor.fetchall()]

    def get_event_count(self) -> int:
        """Get the total number of stored events."""
        cursor = self._conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM events")
        result = cursor.fetchone()
        return result[0] if result else 0

    def clear_events(self) -> None:
        """Clear all stored events."""
        cursor = self._conn.cursor()
        cursor.execute("DELETE FROM events")
        # Reset auto-increment sequence
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='events'")
        self._conn.commit()
        logger.info("Event store cleared")

    def close(self) -> None:
        """Close the underlying SQLite connection."""
        conn = getattr(self, "_conn", None)
        if conn is None:
            return
        try:
            conn.close()
            logger.info("PersistentEventStore connection closed")
        except sqlite3.Error as exc:
            logger.warning("Error closing PersistentEventStore connection: %s", exc)
        finally:
            self._conn = None

    def __enter__(self) -> "PersistentEventStore":
        """Enter the runtime context related to this object."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit the runtime context and close the connection."""
        self.close()
