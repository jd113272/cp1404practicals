"""
CP1404 Practical
Hex colours in a dictionary
"""

CODE_TO_NAME = {"aliceblue": "f0f8ff", "amber": "ffbf00", "amaranth": "e52b50", "aqua": "00ffff", "aureolin": "fdee00",
                "beaver": "9f8170", "bone": "e3dac9", "camel": "c19a6b", "cerise": "de3163", "darkgreen": "006400"}

colour_name = input("Please enter a colour name: ").lower()
while colour_name != "":
    try:
        print(f"the colour {colour_name} has the code: {CODE_TO_NAME[colour_name]}")
    except KeyError:
        print("This colour is not in the dictionary")
    colour_name = input("Please enter a colour name: ").lower()
