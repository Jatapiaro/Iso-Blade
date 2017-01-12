import kivy
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas,\
                                                NavigationToolbar2Kivy
import pickle
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from Models.Blade import Blade


Builder.load_file('Kivy_Files/Screens.kv')

blade = Blade()

class Prueba(BoxLayout):
    pass

class InitialScreen(Screen):

   def new_blade(self):
       save_dialog = SaveDialog()
       save_dialog.open()

   def load_blade(self):
       pass

   def close_app(self):
       App.get_running_app().stop()


class AnotherScreen(Screen):

    def on_pre_enter(self, *args):
        fig, ax = plt.subplots()
        self.ids['box_box2'].clear_widgets()
        self.ids['box_box2'].add_widget(fig.canvas)

    def say_hi(self):
        fig, ax = plt.subplots()
        self.ids['box_box2'].clear_widgets()
        self.ids['box_box2'].add_widget(fig.canvas)




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
