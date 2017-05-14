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

    def solve_one_day_single_job(self):
        # given time points here
        download_time_points = ['8:30:00', '9:30:00', '12:30:00', '13:55:00', '23:10:00', '23:30:00']

        now_time = datetime.datetime.now()
        today_date = datetime.datetime.now().date().strftime('%Y-%m-%d')
        time_points = [datetime.datetime.strptime(today_date + ' ' + t, '%Y-%m-%d %H:%M:%S') for
                       t in download_time_points]

        still_need_to_do_points = [t for t in time_points if t > now_time]
        still_need_to_do_points.append(now_time)
        still_need_to_do_points = sorted(still_need_to_do_points)
        print('still to do work time: ', still_need_to_do_points)
        intervals = [(still_need_to_do_points[i] - still_need_to_do_points[i - 1]).seconds
                     for i in range(1, len(still_need_to_do_points))]
        print('[DOWNLOAD CRUISER] intervals: ', intervals)
        for i, interval in enumerate(intervals):
            print('[MULTI TIME POINT CRUISER] currently solve interval: ', interval)
            time.sleep(interval)
            self.download_wallpaper()

    @staticmethod
    def seconds_left_util_tomorrow():
        now = datetime.datetime.now()
        tomorrow = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
        return abs(tomorrow - now).seconds

    def cruise_download_wallpaper(self):
        """
        updated to a more universal algorithm. just given some time points
        and this cruiser will execute same thing in these time points.
        :return: 
        """
        print('[CRUISE] download wallpaper cruise start...')
        while True:
            self.solve_one_day_single_job()
            # after today's job done, see how many seconds until tomorrow, sleep for that long
            # when tomorrow comes, back to solve one day's job again.
            seconds_to_tomorrow = self.seconds_left_util_tomorrow()
            time.sleep(seconds_to_tomorrow)









