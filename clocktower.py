import time
import datetime
import itertools
import argparse
import urllib
import os
from lxml import html


def parse_snapshots(input_html):
    parsed = html.fromstring(input_html.read())
    year = int(parsed.find_class("activeHighlight")[0].text_content())
    url_match = "http://web.archive.org/web/{}".format(year)
    snapshots = set()

    for link in parsed.findall(".//a"):
        if link.attrib["href"].startswith(url_match):
            snapshots.add(link.attrib["href"])

    return year, snapshots


def parse_datetime(url):
    date_str = url.replace("http://web.archive.org/web/", "").split("/")[0]
    year = int(date_str[0:4])
    month = int(date_str[4:6])
    day = int(date_str[6:8])
    hour = int(date_str[8:10])
    minutes = int(date_str[10:12])
    seconds = int(date_str[12:14])
    return datetime.datetime(year, month, day, hour, minutes, seconds)


def save_snapshot(url, directory):
    timestamp = parse_datetime(url)
    filename = "{}.html".format(int(time.mktime(timestamp.timetuple())))
    filename = os.path.join(directory, filename)
    created = False

    if not os.path.exists(filename):
        urllib.urlretrieve(url, filename)
        created = True

    return filename, created


def get_snapshots(year, url):
    """Return a list of all snapshots for this year"""
    wayback = "http://wayback.archive.org/web/{}0701000000*/http://{}"
    y, snapshots = parse_snapshots(urllib.urlopen(wayback.format(year, url)))

    # We got the wrong year
    if not year == y:
        return []

    return snapshots


def main():
    desc = "Download websites from archive.org"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("url", help="URL to download")
    parser.add_argument("-d", "--directory", help="Download directory",
                        default="~/clocktower")
    args = parser.parse_args()

    website_dir = os.path.expanduser(os.path.join(args.directory, args.url))

    if not os.path.isdir(website_dir):
        os.makedirs(website_dir)

    snapshots = set()

    for year in range(1998, 2013):
        urls = get_snapshots(year, args.url)
        start = len(snapshots)
        for url in urls:
            snapshots.add(url)
        print "Got {} snapshot urls for {}, {}".format(len(snapshots) - start,
                                                       args.url, year)
        time.sleep(1)

    for snapshot_url in snapshots:
        path, created = save_snapshot(snapshot_url, website_dir)
        if created:
            print "Saved {} to {}".format(snapshot_url, path)
            time.sleep(1)
        else:
            print "Already downloaded {} to {}".format(snapshot_url, path)
