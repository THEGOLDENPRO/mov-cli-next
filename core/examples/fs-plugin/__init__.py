from typing import Iterable

from mov_core.runtime.dispatcher import ProtocolDispatcher

def media_search(query: str) -> Iterable[SearchResult]:
    # yield
    ...

def media_watch(search_result: SearchResult) -> Media:
    ...

def load_plugin(dispatcher: ProtocolDispatcher):
    dispatcher.bind("v1/mov-cli.media.search", media_search)
    dispatcher.bind("v1/mov-cli.media.watch", media_watch)

    ...