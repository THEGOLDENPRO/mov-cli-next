from pathlib import Path

from .plugin import Plugin

__all__ = ()

def load_plugin(plugin_path: Path) -> Plugin:
    ...