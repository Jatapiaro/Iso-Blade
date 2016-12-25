import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder

Builder.load_file('Kivy_Files/Screens.kv')

class InitialScreen(Screen):

   def new_blade(self):
       pass

   def load_blade(self):
       pass

   def close_app(self):
       App.get_running_app().stop()


screen_manager = ScreenManager()
screen_manager.add_widget(InitialScreen(name="initial_screen"))



class IsoBladeApp(App):

    def build(self):
        return screen_manager

sample = IsoBladeApp()

sample.run()
