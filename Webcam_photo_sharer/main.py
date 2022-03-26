from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time
import webbrowser

from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def start(self):
        """
        1. Starts the camera
        2. Change the button text
        3. Set the texture to camera default texture
        """
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        """
        1. Stops the camera
        2. Change the button text
        3. Set the texture to None
        """
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        """
        1. Capture the image & save it in images folder
        2. Change the screen and set it to image in new screen
        """
        current_time = time.strftime("%Y%m%d_%H%M%S")
        self.filepath = "images/image_" + current_time + ".png"
        self.ids.camera.export_to_png(self.filepath)

        # change the screen
        self.manager.current = 'image_screen'

        # set the captured image to new screen
        self.manager.current_screen.ids.image.source = self.filepath


class ImageScreen(Screen):

    link_message = "Create a link first"

    def create_link(self):
        """
        1. Access the filepath from the CameraScreen class
        2. Upload the file to FileStack and save the url
        3. Show the url to label's text
        """

        filepath = App.get_running_app().root.ids.camera_screen.filepath
        file_sharer = FileSharer(filepath)
        self.url = file_sharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        """
        Copy the shared link
        """
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        """
        Open the link in the browser
        """
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message






class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
