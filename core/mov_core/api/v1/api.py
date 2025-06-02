from typing import Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from .metadata import Metadata

    from ...runtime.dispatcher import ProtocolDispatcher

from . import protocols

__all__ = ("API",)

# TODO: complete api class

# The API class is a simple way for CLI app developers to 
# interface with mov-core. It's also how mov-core maintains some state.
class API():
    def __init__(self):
        self.dispatcher: ProtocolDispatcher = ...

    def search(self, query: str) -> Iterable[Metadata]:
        return protocols.search(self.dispatcher, query)

    # TODO: pass some type of object like metadata that
    # we can use to pass to the plugin to make the plugin give
    # us data we can then use to tell a media player to play content.
    def watch(self, metadata: Metadata):
        return protocols.watch(self.dispatcher, metadata)