from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..plugins.plugin import Plugin

from ..errors import ProtocolNotImplemented

class ProtocolDispatcher():
    def __init__(self, plugin: Plugin):
        self.plugin = plugin

    def call(self, protocol: str, **kwargs):
        plugin = self.plugin

        if protocol not in plugin.implemented_protocols:
            raise ProtocolNotImplemented(
                f"The plugin '{plugin.name}' is expected to implement the protocol '{protocol}' but does not! " \
                    "Contact the developer of the plugin." # TODO: Add contacts of developer or the link to the plugin repo.
            )

        raise NotImplementedError()