from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..metadata import Metadata

    from ....runtime.dispatcher import ProtocolDispatcher

__all__ = ("watch",)

def watch(dispatcher: ProtocolDispatcher, metadata: Metadata) -> Media:
    return dispatcher.call("v1/mov-core.media.watch-hook", metadata = metadata)