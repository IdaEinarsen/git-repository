# 10.8 Cats and Dogs



def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(f"\nContents of {filename}:")
            print(contents)

    except FileNotFoundError:
        print(f"\nSorry, the file '{filename}' was not found. Please check the path.")

read_file(r'C:\Users\idaze\Desktop\school_work\Chapter_10\cats.txt')
read_file(r'C:\Users\idaze\Desktop\school_work\Chapter_10\dogs.txt')

# I got the file error message because i had problems making the read_file work because
# it couldnt find the path to the file.

# i changed folder for dogs file, got the error and then put it back in the right folder
# again.