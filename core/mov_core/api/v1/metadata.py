from __future__ import annotations
from typing import Optional

from enum import Enum
from datetime import datetime
from dataclasses import dataclass, field

__all__ = (
    "Metadata",
    "MetadataType"
)

class MetadataType(Enum):
    SINGLE = 0
    """Content released once. Like a film or short animation."""
    MULTI = 1
    """Content with multiple seasons and episodes."""

@dataclass(frozen = True)
class Metadata:
    """
    Metadata about the content.

    A base class for your plugin to use to pass metadata (about content) around - you may inherit from this and expand it if you want.
    """

    id: str
    """
    A unique ID to represent this specific content.
    """
    title: str
    """Title of the content."""
    type: MetadataType
    """
    The type of content this metadata represents. Does it represent multi release content 
    (e.g. a tv series with multiple seasons and episodes) or is it just a singular release?
    """
    description: Optional[str] = field(default = None)
    """Brief description about the content."""
    image_url: Optional[str] = field(default = None)
    """Image URL to a banner, cover or thumbnail of this content."""
    alternate_titles: Optional[list[str]] = field(default = None)
    """A list of alternative titles for this content."""
    release_date: Optional[datetime] = field(default = None)
    """The date and time the content was released."""