import datetime
import argparse
import logging
import urllib
from lxml import html


def parse_snapshots(input_html):
    parsed = html.fromstring(input_html.read())
    year = int(parsed.find_class("activeHighlight")[0].text_content())
    url_match = "http://web.archive.org/web/{}".format(year)
    snapshots = []

    for link in parsed.findall(".//a"):
        if link.attrib["href"].startswith(url_match):
            snapshots.append(link.attrib["href"])

    return year, set(snapshots)


def parse_datetime(url):
    date_str = url.replace("http://web.archive.org/web/", "").split("/")[0]
    year = int(date_str[0:4])
    month = int(date_str[4:6])
    day = int(date_str[6:8])
    hour = int(date_str[8:10])
    minutes = int(date_str[10:12])
    seconds = int(date_str[12:14])
    return datetime.datetime(year, month, day, hour, minutes, seconds)


def get_snapshots(year, url):
    """Return a list of all snapshots for this year"""
    wayback_url = "http://wayback.archive.org/web/{}0101000000*/http://{}"
    try:
        return parse_snapshots(urllib.urlopen(wayback_url.format(year, url)))
    except:
        return False 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download websites from archive.org")
    parser.add_argument("url", help="URL to download")
    parser.add_argument("-v", "--verbose", help="Verbose output",
                        action="store_true", default=False)
    parser.add_argument("-d", "--dir", help="Download directory", default=None)
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    snapshots = [get_snapshots(year, args.url) for year in range(1998, 2013)]
    snapshots = [snapshot for snapshot in snapshots if snapshot]
    print snapshots




