from typing import TypedDict, NotRequired

__all__ = ()

class ProtocolsData(TypedDict):
    requires: list[str]
    implements: list[str]

class PluginData(TypedDict):
    name: str
    authors: list[str]
    protocols: NotRequired[ProtocolsData]

class PluginManifestData(TypedDict):
    version: int
    plugin: PluginData
