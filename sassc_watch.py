"""A wrapper for libsass to generate css when a sass file is modified.

Usage:
    python sassc_watcher.py yoursassfile.scss yourcssfile.css

Only tested on Windows
"""
from __future__ import print_function

import argparse
import time
import os

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

import sass


def get_cmd_line_args():
    """Parse cmd line args into tuple."""
    parser = argparse.ArgumentParser(
        prog='sassc_watcher.py',
        description="A watcher wrapper for libsass"
    )
    parser.add_argument(dest="source")
    parser.add_argument(dest="destination")
    return (parser.parse_args())


def file_exists(file_path):
    if os.path.isfile(path):
        return True

class MyHandler(PatternMatchingEventHandler):
    def add_destination(self, destination):
        self.destination = destination

    def on_modified(self, event):
        print("Detected modification of {}".format(event.src_path))
        sass_content = ""
        with open(event.src_path, "r") as f:
            sass_content = f.read()
        try:
            css_content = sass.compile(string=sass_content)
        except sass.CompileError:
            print("Compilation error occured")
            print("========================================================")
            return
        with open(self.destination, "w") as f:
            f.write(css_content)
        print("Modified contents of {}".format(self.destination))


if __name__ == "__main__":
    cmd_args = get_cmd_line_args()
    cwd = os.getcwd()

    file_pattern = cwd + os.path.sep + cmd_args.source
    event_handler = MyHandler(patterns=[file_pattern])
    event_handler.add_destination(cwd + os.path.sep + cmd_args.destination)
    observer = Observer()
    # For now you need to run it in the directory with css. We could allow parent directoried to work by changing recursive to True, but this does not feel like good solution
    observer.schedule(event_handler, path=cwd, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
