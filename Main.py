import kivy
import pickle
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from Models.Blade import Blade


Builder.load_file('Kivy_Files/Screens.kv')


class InitialScreen(Screen):

   def new_blade(self):
       save_dialog = SaveDialog()
       save_dialog.open()

   def load_blade(self):
       pass

   def close_app(self):
       App.get_running_app().stop()


class AnotherScreen(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(InitialScreen(name="initial_screen"))
screen_manager.add_widget(AnotherScreen(name="another_screen"))


class SaveDialog(Popup):

    file_name = ObjectProperty(None)

    def save_file(self,path,file_name):
        blade = Blade()
        print("Write "+file_name+" in "+path)
        file_name+=".ibd"
        path+="/"+file_name
        pickle._dump(blade, open(path, "wb" ))
        screen_manager.current = 'another_screen'
        self.dismiss()


class IsoBladeApp(App):

    def build(self):
        return screen_manager

sample = IsoBladeApp()

sample.run()
