from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from ...types import ProtocolLiteralT

__all__ = ()

from abc import ABC, abstractmethod

class Dispatcher(ABC):
    @abstractmethod
    def call(self, protocol: str, **kwargs):
        ...

    @abstractmethod
    def hook(self, protocol: ProtocolLiteralT, callback: Callable[..., any]):
        """Binds a callback to this protocol that is executed when needed to by mov-core."""
        ...

    @abstractmethod
    def hook_multiple(self, *protocols: ProtocolLiteralT, callback: Callable[..., any]):
        """Binds this callback to multiple protocols that will be executed by mov-core when needed."""
        ...

    @abstractmethod
    def exempt(self, protocol: str):
        """
        Exempts a protocol telling mov-core it is implemented but should not be called.

        If an "implemented" protocol is not used and bound by a plugin mov-core will complain, but 
        some protocols are not made to actually be bound and called by mov-core; some exist just to show
        a plugin supports various features and other plugins can require for those features to be present 
        for example `v1/mov-core.player.url` (used by plugins to require for players that support passing URLs).
        """
        ...