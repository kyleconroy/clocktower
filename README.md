![Hill Valley Clock Tower](https://github.com/derferman/clocktower/raw/master/tower.jpg)

The [Wayback Machine](http://www.archive.org/web/web.php) contains a unique history for many websites. However, downloading and accessing these archives is tedious. With clocktower, no more!

## Installation

    pip install clocktower

but if you must

    easy_install clocktower

## Usage

clocktower is really easy to use

    clocktower news.ycombinator.com

will download all snapshots into `~/clocktower/news.ycombinator.com`. Each file will be named `<unix timestamp>.html`

You can specify the download directory with the `-d` flag 

    clocktower -d /tmp/clocktower news.ycombinator.com
