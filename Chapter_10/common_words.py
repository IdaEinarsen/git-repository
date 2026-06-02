# 10.10 Common Words

from pathlib import Path

files = [
    Path(r'C:\Users\EinarsenIda\Desktop\projects\Chapter_10\meditation.txt'),
    Path(r'C:\Users\EinarsenIda\Desktop\projects\Chapter_10\pride_and_prejudice.txt'),
    Path(r'C:\Users\EinarsenIda\Desktop\projects\Chapter_10\beyond_good_and_evil.txt')
]

for path in files:

    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist")
    else:
        contents = contents.lower()


# 'the' count counts all words like the,there,they 
# 'the ' only counts the words

        print(f"\n{path.name}")
        print(f"'the' count: {contents.count('the')}")
        print(f"'the ' count: {contents.count('the ')}")