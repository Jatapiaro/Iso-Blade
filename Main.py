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

Builder.load_file('Kivy_Files/WorkingScreen.kv')
Builder.load_file('Kivy_Files/InitialScreen.kv')
Builder.load_file('Kivy_Files/SaveLoad.kv')


class ProfileListButton(ListItemButton):

    def change(self,change):
        print("Hola: "+str(change.index))
    """def change(self,change):
        if screen_manager.get_screen("working_screen").profile_added is True:
            screen_manager.get_screen("working_screen").profile_added = False
        else:
            screen_manager.get_screen("working_screen").profile_added = False
            screen_manager.get_screen("working_screen").profile_selected = change.text
            screen_manager.get_screen("working_screen").draw_on_selection_change()"""


class InitialScreen(Screen):
   def new_blade(self):
       save_dialog = SaveDialog()
       save_dialog.open()

   def load_blade(self):
       load_dialog = LoadBladeDialog()
       load_dialog.open()

   def close_app(self):
       App.get_running_app().stop()


class WorkingScreen(Screen):

    blade = Blade()
    blade_path = ""
    profile_added = False
    profile_selected = ""

    control_points_input = ObjectProperty()
    percentage_input =  ObjectProperty()
    profile_list = ObjectProperty()

    def on_pre_enter(self, *args):
        if len(self.blade.profiles) == 0:
            fig, ax = plt.subplots()
            self.ids['drawing_box'].clear_widgets()
            self.ids['drawing_box'].add_widget(fig.canvas)
        else:
            self.set_after_load()


    def load_profile(self):
        load_dialog = LoadDialog()
        load_dialog.open()

    def draw_on_profile_load(self):
        fig, ax = plt.subplots()
        p = self.blade.profiles[-1]
        plt.axis([-0.2, 1.2, -0.7, .7])
        plt.plot(p.x_coordinates,p.y_coordinates)
        plt.plot(p.center.x, p.center.y,'g^')
        self.ids['drawing_box'].clear_widgets()
        self.ids['drawing_box'].add_widget(fig.canvas)

    def draw_on_selection_change(self):
        fig, ax = plt.subplots()
        for profile in self.blade.profiles:
            if profile.name == self.profile_selected:
                self.ids['drawing_box'].clear_widgets()
                plt.axis([-0.2, 1.2, -0.7, .7])
                plt.plot(profile.x_coordinates,profile.y_coordinates)
                plt.plot(profile.center.x, profile.center.y,'g^')
                self.ids['drawing_box'].add_widget(fig.canvas)
                break

    def set_after_load(self):
        for profile in self.blade.profiles:
            self.profile_list.adapter.data.extend([profile.name])
        self.profile_list._trigger_reset_populate()
        self.profile_added = True
        self.profile_list.adapter.get_view(0).trigger_action(duration=0)
        fig, ax = plt.subplots()
        p = self.blade.profiles[0]
        plt.axis([-0.2, 1.2, -0.7, .7])
        plt.plot(p.x_coordinates,p.y_coordinates)
        plt.plot(p.center.x,p.center.y,'g^')
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

        screen_manager.get_screen(
            "working_screen").profile_list.adapter.data.extend([p.name])

        screen_manager.get_screen(
            "working_screen").profile_list._trigger_reset_populate()

        index_to_trigger = \
            len(screen_manager.get_screen("working_screen").blade.profiles)-1

        screen_manager.get_screen(
            "working_screen").profile_load = True

        screen_manager.get_screen(
            "working_screen").profile_list.adapter.get_view(
            index_to_trigger).trigger_action(duration=0)

        screen_manager.get_screen(
            "working_screen").draw_on_profile_load()

        self.dismiss()


class LoadBladeDialog(Popup):

    def load_blade(self,path):
        screen_manager.get_screen(
            "working_screen").blade = FilesModule.load_blade(path[0])
        screen_manager.get_screen(
            "working_screen").blade_path = path[0]
        screen_manager.current = 'working_screen'
        self.dismiss()


class IsoBladeApp(App):

    def build(self):
        return screen_manager

sample = IsoBladeApp()

sample.run()
