from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from ... import types

    from ...plugins.plugin import Plugin

__all__ = ("ProtocolDispatcher",)

from .base import Dispatcher
from ...errors import ProtocolNotImplemented, ProtocolNotHooked

class ProtocolDispatcher(Dispatcher):
    def __init__(self, plugins: tuple[Plugin]):
        self.__plugins = plugins

        self._exempted_protocols: list[str] = []
        self.__hooked_protocols: dict[str, Callable[..., any]] = {}

        super().__init__()

    def call(self, protocol: types.ProtocolHookLiteralT, **kwargs):
        for plugin in self.__plugins:
            if protocol not in plugin.implemented_protocols:
                continue

            callback = self.__hooked_protocols.get(protocol, None)

            if callback is None:
                raise ProtocolNotHooked(
                    f"The implemented protocol '{protocol}' was expected to be hooked in the plugin '{plugin.name}' " \
                        "but was not! Contact the developer of the plugin." # TODO: Add contacts of developer or the link to the plugin repo.
                    )

            return callback(self, **kwargs)

        raise ProtocolNotImplemented(
            f"None of the plugins ('{[f"{plugin} | " for plugin in self.__plugins][:-2]}') implement the '{protocol}' protocol!"
        )

    def hook(self, protocol: types.ProtocolHookLiteralT, callback: Callable[..., any]):
        self.__hooked_protocols[protocol] = callback

    def exempt(self, protocol: types.ProtocolExemptLiteralT):
        self._exempted_protocols.append(protocol)