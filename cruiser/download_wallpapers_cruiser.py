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
this cruiser will download wallpapers in every day of 8:00 from pexels
"""
import numpy as np
import datetime
import time
import os
import requests
import pickle
from settings.config import WALLPAPERS_DIR
from scrapers.wallpaper_scraper import WallpaperScraper


class DownloadWallPaperCruiser(object):

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def download_wallpaper():
        wallpaper_scraper = WallpaperScraper()
        wallpaper_scraper.scrap()

    def cruise_download_wallpaper(self):
        print('[CRUISE] download wallpaper cruise start...')
        download_start_time = '12:20:00'
        while True:
            today_date = datetime.datetime.now().date().strftime('%Y-%m-%d')
            now_time = datetime.datetime.now()
            start = datetime.datetime.strptime(today_date + ' ' + download_start_time, '%Y-%m-%d %H:%M:%S')
            print('[CRUISER] start download time: ', start)
            time.sleep((start - now_time).seconds)
            self.download_wallpaper()




