from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from ... import types

__all__ = ()

from abc import ABC, abstractmethod

class Dispatcher(ABC):
    @abstractmethod
    def call(self, protocol: types.ProtocolHookLiteralT, **kwargs):
        ...

    @abstractmethod
    def hook(self, protocol: types.ProtocolHookLiteralT, callback: Callable[..., any]):
        """
        Binds a callback to this protocol that is executed when 
        called by someone with the dispatcher (e.g. mov-core, juno-cli).
        """
        ...

    @abstractmethod
    def exempt(self, protocol: types.ProtocolExemptLiteralT):
        """
        Exempts a protocol telling mov-core it is implemented but should not be called.

        If an "implemented" protocol is not used and hooked by a plugin mov-core will complain, but 
        some protocols are not made to actually be hooked and called by mov-core; some exist just to show 
        a plugin supports various features and other plugins can require for those features to be present 
        for example `v1/mov-core.player.url` (used by plugins to require for players that support passing URLs).
        """
        ...