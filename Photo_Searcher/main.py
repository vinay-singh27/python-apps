import random

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def get_image_link(self):
        #get user query from text input
        user_query = self.manager.current_screen.ids.user_input.text
        print(user_query)
        #get wikipedia page & list of image urls
        try:
            page = wikipedia.page(user_query)
        except wikipedia.DisambiguationError as e:
            s = random.choice(e.options)
            print(s)
            page = wikipedia.page(s)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        #download the image
        req = requests.get(self.get_image_link())
        image_path = 'Files/image.jpg'
        with open(image_path, 'wb') as f:
            f.write(req.content)
        return image_path

    def set_image(self):
        #set the image widget
        self.manager.current_screen.ids.back_img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
