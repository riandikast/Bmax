# importing the module
import os
import sys

import screen_brightness_control as sbc
from win11toast import toast

current_path = os.path.dirname(os.path.abspath(__file__))

if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
else:
    app_path = current_path

# fade brightness from the current brightness to %
sbc.fade_brightness(100)

# appLogoOverride
#hero
#
icon = {
    'src': str(app_path) + r"\bmax.jpg" ,
    'placement': 'appLogoOverride'
}

toast('Brightness Changed', 'Brightness Set to Maximum', icon=icon, duration='short')
