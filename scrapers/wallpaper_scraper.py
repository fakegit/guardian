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
as scrapy very hard to control in script inside, and consider of
our goal are simple scrap images, so we using lxml to analysis html
and get image urls which we want
"""
from lxml import etree
import requests
from settings.config import WALLPAPERS_DIR
from datetime import datetime
import os
import time
from clint.textui import progress
from threading import Thread
from random import sample


class WallpaperScraper(object):

    def __init__(self):
        self.base_url = 'https://www.pexels.com'

    def _get_html(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        }
        response = requests.get(self.base_url, headers=headers)
        html = response.text
        self.html = html

    def _parse_html(self):
        selector = etree.HTML(self.html)
        image_urls = []
        for src in selector.xpath('//article[@class="photo-item"]/a/img/@src'):
            image_urls.append(src.split('?')[0].replace('images', 'static'))
        self.image_urls = image_urls

    @staticmethod
    def save_image_from_url(url):
        print('current url: ', url)
        try:
            save_path = WALLPAPERS_DIR
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            file_name = ''.join(sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789', 16))
            file_name = str(datetime.now().strftime('%Y_%m_%d_') + file_name + '.jpg')
            print(file_name)
            save_file = os.path.join(save_path, file_name)
            start = time.time()
            response = requests.get(url, stream=True)
            with open(save_file, 'wb') as f:
                # f.write(requests.get(_url).content)
                total_length = int(response.headers.get('content-length'))
                for chunk in progress.bar(response.iter_content(chunk_size=1024),
                                          expected_size=(total_length / 1024) + 1):
                    end = time.time()
                    if end - start > 500:
                        raise TimeoutError
                    if chunk:
                        f.write(chunk)
                        f.flush()
            print('downloaded {}. time cost {} seconds'.format(file_name, round(end - start, 4)))
            pass
        except requests.Timeout or requests.ConnectTimeout:
            pass

    def scrap(self):
        """
        we will using multi process to download images,
        make time as tiny as possible
        :return:
        """
        self._get_html()
        self._parse_html()
        # [UPDATE] we are using 4 images, not all 12
        if len(self.image_urls) < 4:
            pass
        else:
            to_download_images = self.image_urls[0: 4]
            threads = []
            for i in range(len(to_download_images)):
                t = Thread(target=self.save_image_from_url, args=(to_download_images[i],))
                threads.append(t)
                t.setDaemon(True)
                t.start()
            for t in threads:
                t.join()
            print('[WALLPAPER SCRAPER] all images downloaded.!!!!!!')










