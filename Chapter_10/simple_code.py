# 10.3 Simple Code

# An example of how to simplefy the code's from this chapter 
# by using splitlines and using 10.2 as the example

from pathlib import Path

path = Path("C:/Users/idaze/Desktop/school_work/Chapter_10/learning_python.txt")


# Eliminates temporary contents and lines.

for line in path.read_text().splitlines():
    print(line.replace("Python", "C"))

