from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from ...plugins.plugin import Plugin

    from ...types import ProtocolLiteralT

__all__ = ("ProtocolDispatcher",)

from .base import Dispatcher
from ...errors import ProtocolNotImplemented

class ProtocolDispatcher(Dispatcher):
    def __init__(self, plugin: Plugin):
        self.plugin = plugin

        self.__exempted_protocols: list[str] = []
        self.__bound_protocols: dict[str, Callable[..., any]] = {}

        super().__init__()

    def call(self, protocol: ProtocolLiteralT, **kwargs):
        plugin = self.plugin

        if protocol not in plugin.implemented_protocols:
            raise ProtocolNotImplemented(
                f"The plugin '{plugin.name}' is expected to implement the protocol '{protocol}' but does not! " \
                    "Contact the developer of the plugin." # TODO: Add contacts of developer or the link to the plugin repo.
            )

        raise NotImplementedError()

    def hook(self, protocol: ProtocolLiteralT, callback: Callable[..., any]):
        self.__bound_protocols[protocol] = callback

    def hook_multiple(self, *protocols: ProtocolLiteralT, callback: Callable[..., any]):
        for protocol in protocols:
            self.__bound_protocols[protocol] = callback

    def exempt(self, protocol: str):
        self.__exempted_protocols.append(protocol)