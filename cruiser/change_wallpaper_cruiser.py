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
this cruiser will charging wallpapers management.
it will download new wallpapers in 8:00 everyday,
and after that, it will cha
"""
import numpy as np
import datetime
import time
import os
import requests
import pickle
from settings.config import WALLPAPERS_DIR


class ChangeWallPaperCruiser(object):

    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def change_wallpaper():
        if os.path.exists(WALLPAPERS_DIR):
            all_file = [i for i in os.listdir(WALLPAPERS_DIR) if os.path.isfile(os.path.join(WALLPAPERS_DIR, i))]
            image_files = [i for i in all_file if 'jpg' or 'png' or 'jpeg' in i]
            if len(image_files) > 0:
                saved_image_path = os.path.join(WALLPAPERS_DIR, np.random.choice(image_files))
                full_path = os.path.abspath(saved_image_path)
                command = 'gsettings set org.gnome.desktop.background picture-uri file://{}'.format(full_path)
                print('[CRUISE] change wallpaper, command: ', command)
                os.system(command)
            else:
                print('no images to set')
                pass
        else:
            pass

    def cruise_change_wallpaper(self):
        print('[CRUISE] change wallpaper cruise start...')
        while True:
            self.change_wallpaper()
            time.sleep(20)