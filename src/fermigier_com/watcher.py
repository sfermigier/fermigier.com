from pathlib import Path

import watchfiles
from watchfiles import DefaultFilter

from fermigier_com.builder import build


def watch():
    build()

    ignore_dirs = tuple(DefaultFilter.ignore_dirs) + ("dist",)
    filter = DefaultFilter(ignore_dirs=ignore_dirs)

    for changes in watchfiles.watch('.', watch_filter=filter):
        print(changes)
        print("Changes detected, rebuilding...")
        build()
        print("Done.")
