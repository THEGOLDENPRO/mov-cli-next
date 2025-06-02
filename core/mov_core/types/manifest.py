from typing import TypedDict, NotRequired

__all__ = (
    "PluginManifestData",
)

class ProtocolsData(TypedDict):
    requires: list[str]
    implements: list[str]

class PluginData(TypedDict):
    name: str
    authors: list[str]
    source_code: NotRequired[str]
    protocols: NotRequired[ProtocolsData]

class PluginManifestData(TypedDict):
    version: int
    plugin: PluginData
