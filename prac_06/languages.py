"""
Estimated time: 15 minutes
Actual time: 13 minutes
"""
from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic]
dynamic_languages = [programming_language for programming_language in programming_languages if
                     programming_language.is_dynamic()]

print("The dynamically typed languages are: ")
for dynamic_language in dynamic_languages:
    print(dynamic_language.language)
