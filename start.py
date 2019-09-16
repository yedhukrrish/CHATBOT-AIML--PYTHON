from typing import Any, Union

import aiml
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    name1: TextInput

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.rows = 3
        self.name1 = TextInput(multiline=True)
        self.add_widget(self.name1)
        self.label=Label(text="Hi there ,it's me tezz ur personal AI bot")
        self.add_widget(self.label)

        self.butt = Button(text="submit", font_size=40)
        self.butt.bind(on_press=self.pressed)
        self.add_widget(self.butt)

    def pressed(self, instance):
        name = self.name1.text
        kernel = aiml.Kernel()
        kernel.bootstrap(learnFiles="std.startup.xml", commands="LOAD AIML B")

        if name == "quit":
            exit()
        elif name == "save":
            pass
        else:
            bot_response = kernel.respond(name)

            assert isinstance(bot_response, object)
            self.label.text = str(bot_response)

    def on_start(self):
        self.name1.focus = True


class MyApp(App):
    def build(self):
        return MyGrid()

        # Do something with bot_response


if __name__ == "__main__":
    MyApp().run()
