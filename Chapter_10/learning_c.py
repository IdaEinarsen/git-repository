# 10.2 Learning C

from pathlib import Path

path = Path("C:/Users/idaze/Desktop/school_work/Chapter_10/learning_python.txt")
contents = path.read_text()

#When you wanna replace a word you use the replace method like I did here.
contents = contents.replace("Python", "C")
print(contents)