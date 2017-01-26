import kivy
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas,\
                                                NavigationToolbar2Kivy
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty
from IsoBladeModules import FilesModule
from Models.Profile import Profile
from kivy.uix.popup import Popup
from kivy.lang import Builder
from Models.Blade import Blade
import matplotlib.pyplot as plt
from kivy.app import App

Builder.load_file('Kivy_Files/InitialScreen.kv')
Builder.load_file('Kivy_Files/WorkingScreen.kv')
Builder.load_file('Kivy_Files/SaveLoad.kv')


class ProfileListButton(ListItemButton):

    def change(self,change):
        print("Currente: "+str(change.text))
        screen_manager.get_screen("working_screen").draw_on_change()



class InitialScreen(Screen):
   def new_blade(self):
       save_dialog = SaveDialog()
       save_dialog.open()

   def load_blade(self):
       pass

   def close_app(self):
       App.get_running_app().stop()


class WorkingScreen(Screen):

    blade = Blade()
    blade_path = ""

    control_points_input = ObjectProperty()
    percentage_input =  ObjectProperty()
    profile_list = ObjectProperty()

    def on_pre_enter(self, *args):
        fig, ax = plt.subplots()
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(fig.canvas)

    def load_profile(self):
        load_dialog = LoadDialog()
        load_dialog.open()

    def draw_on_change(self):
        if self.profile_list.adapter.selection:
            print(self.profile_list.adapter.selection[0].text)


    def draw(self):
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3])
        ax.plot([-1, -2, -3])
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(fig.canvas)


screen_manager = ScreenManager()
screen_manager.add_widget(InitialScreen(name="initial_screen"))
screen_manager.add_widget(WorkingScreen(name="working_screen"))


class SaveDialog(Popup):

    file_name = ObjectProperty(None)

    def save_file(self,path,file_name):

        path = FilesModule.save_blade(
            screen_manager.get_screen("working_screen").blade,file_name,path)

        screen_manager.get_screen("working_screen").blade_path = path
        screen_manager.current = 'working_screen'

        self.dismiss()


class LoadDialog(Popup):

    profile_name = ObjectProperty(None)

    def load_profile(self,path,file_name,profile_name):

        x_points,y_points = FilesModule.load_profile(file_name[0])

        p = Profile(x_points,y_points)

        if(len(profile_name) == 0):
            p.name = file_name[0].replace(path+"/","").replace(".csv","")
        else:
            p.name = profile_name

        screen_manager.get_screen("working_screen").blade.add_profile(p)

        FilesModule.update_blade(
            screen_manager.get_screen("working_screen").blade,
            screen_manager.get_screen("working_screen").blade_path)

        p = screen_manager.get_screen("working_screen").blade.profiles[-1]

        screen_manager.get_screen("working_screen").profile_list.adapter.data.extend([p.name])

        screen_manager.get_screen("working_screen").profile_list._trigger_reset_populate()



        self.dismiss()

    def load_blade(self,path):
        pass


class IsoBladeApp(App):

    def build(self):
        return screen_manager

sample = IsoBladeApp()

sample.run()
