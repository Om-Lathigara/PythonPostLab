# from kivy.app import App
# from kivy.uix.button import Button

# class MyApp(App):
#     def build(self):
#         return Button(
#             text='Click Me',
#             on_press=lambda x: print("Hello, Kivy!"),
#             background_normal='',     # removes default button background image
#             background_down='',       # disables pressed-state image
#             background_color=(1, 1, 1, 1),  # white background (no color change on press)
#             color=(0, 0, 0, 1)         # black text
#         )

# MyApp().run()
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        # Set window background to black
        Window.clearcolor = (0, 0, 0, 1)  # RGBA for black

        return Button(
            text='Click Me',
            on_press=lambda x: print("Hello, Kivy!"),
            background_normal='',        # no default image
            background_down='',          # no press image
            background_color=(0, 0, 0, 1),  # black button background
            color=(1, 1, 1, 1)           # white text
        )

MyApp().run()
