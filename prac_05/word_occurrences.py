"""
Word Occurrences
Estimate: 10 minutes
Actual: 10 minutes
"""

word_to_count = {}
string = input("Text: ").lower()
words = string.split()

for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
maximum_width = max([len(word) for word in words])

for word, count in sorted(word_to_count.items()):
    print(f"{word:{maximum_width}} : {count}")
