from typing import Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from mov_core.runtime.dispatcher import ProtocolDispatcher

from mov_core.api.v1 import Metadata, MetadataType

def media_search(query: str) -> Iterable[Metadata]:
    # yield
    ...

def media_watch(ui_dispatcher: ProtocolDispatcher, metadata: Metadata) -> Media:
    if not metadata.type == MetadataType.SINGLE:
        raise ValueError(
            "Metadata should always be of type SINGLE! This plugin only supports singular content."
        )

    # dispatcher.call("v1/mov-core.ui.select.episode-hook", episode_by_season)

def load_plugin(plugin_dispatcher: ProtocolDispatcher):
    plugin_dispatcher.hook("v1/mov-core.media.search-hook", media_search)
    plugin_dispatcher.hook("v1/mov-core.media.watch-hook", media_watch)

    ...