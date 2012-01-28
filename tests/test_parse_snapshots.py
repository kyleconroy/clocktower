import datetime
import logging
from clocktower import parse_snapshots, parse_datetime
from nose.tools import assert_equals

def test_parse_google_year():
    year, snapshots = parse_snapshots(open("tests/hackernews.html"))
    assert_equals(year, 2007)

def test_parse_google_snapshots():
    year, snapshots = parse_snapshots(open("tests/google.html"))
    assert_equals(snapshots, set([
        'http://web.archive.org/web/19981202230410/http://www.google.com/',
        'http://web.archive.org/web/19981111184551/http://google.com/',
        ]))

def test_parse_datetime():
    url = "http://web.archive.org/web/20070928205125/http://news.ycombinator.com/"
    parse = parse_datetime(url)
    assert_equals(parse, datetime.datetime(2007, 9, 28, 20, 51, 25))
