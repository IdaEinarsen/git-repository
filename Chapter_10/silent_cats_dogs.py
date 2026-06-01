# 10.9 Silent Cats and Dogs

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(f"\nContents of {filename}:")
            print(contents)

    except FileNotFoundError:
        pass # Don't send out an error (ignore error)

read_file(r'C:\Users\idaze\Desktop\school_work\Chapter_10\cats.txt')
read_file(r'C:\Users\idaze\Desktop\school_work\Chapter_10\dogs.txt')