from typing import TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from ..metadata import Metadata

    from ....runtime.dispatcher import ProtocolDispatcher

__all__ = ("search",)

# TODO: add search method that will call the search protocols on the dispatcher.

def search(dispatcher: ProtocolDispatcher, query: str) -> Iterable[Metadata]:
    iterable = dispatcher.call("v1/mov-core.media.search-hook", query = query)

    return iterable