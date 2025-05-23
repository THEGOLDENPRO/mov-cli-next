from typing import Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from mov_core.runtime.dispatcher import ProtocolDispatcher

from mov_core.api.v1 import Metadata

def media_search(query: str) -> Iterable[Metadata]:
    # yield
    ...

def media_watch(metadata: Metadata) -> Media:
    ...

def load_plugin(dispatcher: ProtocolDispatcher):
    dispatcher.hook("v1/mov-cli.media.search", media_search)
    dispatcher.hook("v1/mov-cli.media.watch", media_watch)

    ...