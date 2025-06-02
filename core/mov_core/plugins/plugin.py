from dataclasses import dataclass

from ..types.manifest import PluginManifestData

__all__ = ()

@dataclass
class Plugin:
    manifest: PluginManifestData
    """This dict is expected to be validated to match 'PluginManifestData' before passing."""

    @property
    def name(self) -> str:
        # name will exist as manifest data passed 
        # into this class should be validated beforehand.
        return self.manifest["name"]

    @property
    def required_protocols(self) -> list[str]:
        protocols = self.manifest.get("protocols", None)

        if protocols is None:
            return []

        return protocols.get("requires", [])

    @property
    def implemented_protocols(self) -> list[str]:
        protocols = self.manifest.get("protocols", None)

        if protocols is None:
            return []

        return protocols.get("implements", [])