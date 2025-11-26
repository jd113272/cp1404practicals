"""
Search Wikipedia for a given phrase and return salient information.
"""
from wikipedia import wikipedia, DisambiguationError, PageError

SEARCH_INPUT_MESSAGE = "Enter page title: "

search_phrase = input(f"{SEARCH_INPUT_MESSAGE}")
while search_phrase != "":
    try:
        result = wikipedia.page(search_phrase, auto_suggest=False)
        print(result.title)
        print(result.summary)
        print(result.url)
    except DisambiguationError:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(wikipedia.search(search_phrase))
    except PageError:
        print(f'Page id "{search_phrase}" does not match any pages. Try another id!')
    search_phrase = input(f"{SEARCH_INPUT_MESSAGE}")
print("Thank you.")
