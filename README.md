# Libsass Python Watcher
Auto update CSS file when changes are detected to a Sass file

## Getting started
Clone or download the project and run
    
    python sassc_watcher.py your_sass_file.scss your_css_file.css

### Prerequisites
You must download libsass-python and watchdog

    pip install libsass
    pip install watchdog

## Built With
* [libsass-python](https://github.com/sass/libsass-python) - provides python binding to libsass library
* [Watchdog](https://github.com/gorakhargosh/watchdog) - for detecting file modification events