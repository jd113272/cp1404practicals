"""
Create a KIVY app that dynamically adds labels based on a predefined list.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Create an instance of the DynamicLabelsApp class."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # Sample data
        self.names = ['Bob', 'Jane', 'John', 'Donald', 'Smith']

    def build(self):
        """Build the KIVY program."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from the sample data."""
        for name in self.names:
            # Create the button
            new_button = Label(text=name)
            self.root.ids.main.add_widget(new_button)


DynamicLabelsApp().run()
