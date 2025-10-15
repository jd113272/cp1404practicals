"""
Word Occurrences
Estimate: 10 minutes
Actual: 10 minutes
"""

WORD_TO_COUNT = {}
string = input("Text: ").lower()
words = string.split()

for word in words:
    try:
        WORD_TO_COUNT[word] += 1
    except KeyError:
        WORD_TO_COUNT[word] = 1
maximum_width = max([len(word) for word in words])

for word, count in sorted(WORD_TO_COUNT.items()):
    print(f"{word:{maximum_width}} : {count}")
