#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import socket
import urllib
import urllib2
import tqdm

request_headers = {
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Cookie": '__cfduid=d9c91fd06c1ac129d889eb4bb9336dafe1499854140; 91username=ak2500; language=cn_CN; __dtsu=D9E9B66B43F565597177864F02112562; CLIPSHARE=lluj4gh7q6pkrii83km76mlj62; watch_times=3; DUID=2e19XHcpaC5xpJIIZ6bk5fcXQeeD9tuCsi%2FP%2Fwj4B8UbHr71; USERNAME=ad470Men1Sdz%2FxSPWGhEeyF%2B9qmpH8VETA49p9e7pqvhfjQ; user_level=1; EMAILVERIFIED=no; level=1; __utma=50351329.847118676.1499854140.1503538554.1503542738.10; __utmb=50351329.0.10.1503542738; __utmc=50351329; __utmz=50351329.1499854140.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); AJSTAT_ok_pages=3; AJSTAT_ok_times=8'
}

progress = None


def show_progress(count, block_size, total_size):
    global progress
    if progress is None:
        progress = tqdm.tqdm(total=total_size, unit='B', unit_scale=True)
    progress.update(block_size)

    if count*8192 >= total_size:
        progress.close()
        progress = None


def get_content(url):
    request = urllib2.Request(url, headers=request_headers)
    return urllib2.urlopen(request).read()


def download_file(file_name, url):
    urllib.urlretrieve(url, file_name, show_progress)
