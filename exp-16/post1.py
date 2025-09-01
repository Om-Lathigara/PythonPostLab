# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout

# # Main Application Class
# class CounterApp(App):
#     def build(self):
#         # Create the main layout
#         self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

#         # Label to display the counter
#         self.counter = 0
#         self.label = Label(text=f"Count: {self.counter}", font_size=32)
#         self.layout.add_widget(self.label)

#         # Button to increment the counter
#         self.button = Button(text="Increment", font_size=24)
#         self.button.bind(on_press=self.increment_counter)
#         self.layout.add_widget(self.button)

#         return self.layout

#     # Function to increment the counter
#     def increment_counter(self, instance):
#         self.counter += 1
#         self.label.text = f"Count: {self.counter}"

# # Run the application
# if __name__ == '__main__':
#     CounterApp().run()
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class CounterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Label initialized with 0
        self.counter_label = Label(text="0")
        layout.add_widget(self.counter_label)
        
        # Button that increments the counter
        button = Button(text="Click Me!")
        button.bind(on_press=self.increment_counter)
        layout.add_widget(button)
        
        return layout

    def increment_counter(self, instance):
        # Read and update the counter directly from label text
        current_count = int(self.counter_label.text)
        self.counter_label.text = str(current_count + 1)

if __name__ == '__main__':
    CounterApp().run()
