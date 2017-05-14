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
from cruiser.change_wallpaper_cruiser import ChangeWallPaperCruiser
from cruiser.download_wallpapers_cruiser import DownloadWallPaperCruiser
from threading import Thread
import time
from scrapers.wallpaper_scraper import WallpaperScraper


def start_cruisers_threads():
    change_wallpaper_cruiser = ChangeWallPaperCruiser()
    change_wallpaper_thread = Thread(name='change_wallpaper', target=change_wallpaper_cruiser.cruise_change_wallpaper)
    # change_wallpaper_thread.setDaemon(True)
    change_wallpaper_thread.start()

    download_wallpaper_cruiser = DownloadWallPaperCruiser()
    download_wallpaper_thread = Thread(name='download_wallpaper',
                                       target=download_wallpaper_cruiser.cruise_download_wallpaper)
    # download_wallpaper_thread.setDaemon(True)
    download_wallpaper_thread.start()


def main_loop():
    start_cruisers_threads()
    while True:
        time.sleep(120)
        print('I am alive.')


def scrap_wallpapers():
    scraper = WallpaperScraper()
    scraper.scrap()

if __name__ == '__main__':
    # scrap_wallpapers()
    main_loop()