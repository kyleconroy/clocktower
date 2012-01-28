![Hill Valley Clock Tower](https://github.com/derferman/clocktower/raw/master/tower.jpg)

Clock Tower allows you to go back in time. Using the [Wayback Machine](http://www.archive.org/web/web.php), Clock Tower downloads every historical snapshot of a given URL.

## Installation

    pip install clocktower

Or, if you must

    easy_install clocktower

## Usage

    clocktower news.ycombinator.com

will download all snapshots into `~/clocktower/news.ycombinator.com`. Each file will be named `<unix timestamp>.html`

You can specify the download directory with the `-d` flag 

    clocktower -d /tmp/clocktower news.ycombinator.com
