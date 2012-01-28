# Clock Tower: Marty, we have to back, to the future!

The [Wayback Machine](http://www.archive.org/web/web.php) contains a unique history for many websites. However, downloading and accessing these archives is tedious. With `clocktower`, no more!

## Installation

    pip install clocktower

but if you must

    easy_install clocktower

## Usage

`clocktower` is really easy to use

    clocktower news.ycombinator.com

will download all snapshots in `~/clocktower/news.ycombinator.com`

You can specify the download directory with the `-d` flag 

    clocktower -d /tmp/clocktower news.ycombinator.com

`clocktower` expects the directory to exist


