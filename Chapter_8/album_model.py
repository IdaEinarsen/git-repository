
# import module_name

import album_functions

result = album_functions.make_album("Jason Derulo", "Nu king")
print(result)


# from module_name import function_name

from album_functions import make_album

result = make_album("Taylor Swift", "Red")
print(result)


# from module_name import function_name as fn

from album_functions import make_album as ma

result = ma("Miss Li", "Underbart i all missär")
print(result)


# import module_name as mn

import album_functions as af

result = af.make_album("Lovad", "Älskling EP")
print(result)


# from module_name import *
from album_functions import *

result = make_album("Ed Sheeran", "Divide")
print(result)