'''
Author: www.github.com/JuanBindez
Description: App KivyMD
Python Version: 3.10
year: 2022
Local: Brazil
OS: Linux
'''


import os
import time
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, World", halign="center")


MainApp().run()