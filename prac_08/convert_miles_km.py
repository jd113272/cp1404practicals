from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONVERSION = 1.60934


class MilesConverterApp(App):
    """Create a ConvertMilesKm KIVY class."""
    message = StringProperty()

    def build(self):
        """Create a KIVY instance of the class."""
        self.title = "Convert Miles to kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """Convert the input from miles to km."""
        try:
            self.message = str(float(self.root.ids.user_input.text) * MILES_TO_KM_CONVERSION)
        except ValueError:
            self.message = str(0.0)

    def handle_increment(self, increment):
        """Change the calculated value by the given increment."""
        try:
            self.message = str(float(self.message) + increment)
        except ValueError:
            self.message = str(increment)


MilesConverterApp().run()
