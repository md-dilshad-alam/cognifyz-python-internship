import re
from collections import Counter

filename = r"Level_2\Task_4_File_Manipulation\sample.txt"

with open(filename, "r") as file:
    content = file.read()

words = re.findall(r"\b\w+\b", content.lower())

word_counts = Counter(words)

print("Word occurrences:")

for word in sorted(word_counts):
    print(word, ":", word_counts[word])