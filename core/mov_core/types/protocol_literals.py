from typing import Literal

__all__ = (
    "ProtocolHookLiteralT",
    "ProtocolExemptLiteralT"
)

ProtocolHookLiteralT = Literal[
    "v1/mov-core.media.watch-hook",
    "v1/mov-core.media.search-hook",
]

ProtocolExemptLiteralT = Literal[
    "v1/mov-core.plugin.loader",
    "v1/mov-core.player.url",
    "v1/mov-core.player.subtitles",
]