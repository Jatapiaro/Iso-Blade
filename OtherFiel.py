import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from matplotlib.figure import Figure
from numpy import arange, sin, pi
from kivy.app import App

import numpy as np
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas,\
                                                NavigationToolbar2Kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from matplotlib.transforms import Bbox
from kivy.uix.button import Button
from kivy.graphics import Color, Line, Rectangle

import matplotlib.pyplot as plt


def givemeFig():

    fig, ax = plt.subplots()

    ax.plot([1, 2, 3])

    ax.plot([-1, -2, -3])

    return fig.canvas

class MatplotlibTest(App):
    title = 'Matplotlib Test'

    def build(self):
        fl = BoxLayout(orientation="vertical")
        canvas  = givemeFig()
        canvas2 = givemeFig()
        fl.add_widget(canvas)
        fl.add_widget(canvas2)
        return fl

MatplotlibTest().run()