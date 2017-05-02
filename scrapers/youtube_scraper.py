# Copyright 2017 Jin Fagang. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =======================================================================
"""
this scraper will download videos from youtube using multiprocess
basically using this xpath to scrap video:

"//*[starts-with(@id, 'item-section')]/li/div/@data-context-item-id"

and the query url is:

https://www.youtube.com/results?search_query=fly+iron+man

so that we can get urls, and we will using 'pytube' library to multiprocess download videos

or simply using this xpath:

'//*[@data-context-item-id]'

and base url from

https://www.youtube.com/feed/recommended?spfreload=10

"""
from pytube import YouTube
import requests
import numpy as np
from lxml.html import etree


class YoutubeScraper(object):
    """
    this scraper will download videos from youtube,
    if auto_mode is on, this scrap will download videos from random query
    if off, it will download specific urls you given, and download the highest resolution one
    
    """

    def __init__(self, auto_mode=True, url=None):
        self.auto_mode = auto_mode
        if self.auto_mode:
            pass
        else:
            self.url = url
        self.base_url_query = 'https://www.youtube.com/results?search_query'
        self.base_url_recommend = 'https://www.youtube.com/feed/recommended?spfreload=10'

    def crawl(self):
        self._get_html()
        self._parse_html()
        result = self._multi_process()
        return result

    def _get_html(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        response = requests.get(self.base_url_query, headers=headers)
        html = response.text
        self.html = html

    def _parse_html(self):
        selector = etree.HTML(self.html)
        image_urls = []
        for src in selector.xpath('//*[@data-context-item-id]'):
            image_urls.append(src.split('?')[0].replace('images', 'static'))
        self.image_urls = image_urls