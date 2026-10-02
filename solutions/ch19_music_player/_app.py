"""Helper: import the chapter's player (Code 19.5) from codes/ch19_music_player.py."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "codes"))
from ch19_music_player import MusicPlayerApp, TRACK_SECONDS, format_time   # noqa: E402,F401
