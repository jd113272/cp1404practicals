class ProgrammingLanguage:
    """Represent a ProgrammingLanguage Object"""

    def __init__(self, language, typing, reflection, year):
        """Initialise fields."""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string element."""
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return if ProgrammingLanguage is dynamic of not."""
        if self.typing == "Dynamic":
            return True
        return False  # return False when if statement is false, meaning no else is required.
