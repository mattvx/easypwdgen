import random
import string
import sys

helper = "\n\tCommand usage:\tpwdgen.py x charset\n\t\t\
Where x is an integer defining password lenght\n\t\t\
And \"charset\" is available options:\n\n\t\t\t\
l = only lower\n\t\t\tu = only upper\n\t\t\t\
n = only numbers\n\t\t\ts = only symbols.\n\n\t\t\
There are also combinations available:\n\n\t\t\t\
l,lu,lun,luns\n"

try:
    lenght = int(sys.argv[1])

    if lenght > 94:
        print('\n\tlenght must be not 0 nor greater than 94')
        exit

    low = string.ascii_lowercase
    up = string.ascii_uppercase
    num = string.digits
    sym = string.punctuation

    if sys.argv[2] == 'l':
        all = low
    if sys.argv[2] == 'u':
        all = up
    if sys.argv[2] == 'n':
        all = num
    if sys.argv[2] == 's':
        all = sym    
    if sys.argv[2] == 'lu':
        all = low + up
    if sys.argv[2] == 'lun':
        all = low + up + num
    if sys.argv[2] == 'luns':
        all = low + up + num + sym

    temp_pass = random.sample(all, lenght)

    password = "".join(temp_pass)

    print(password)  

except ValueError:
    print(helper)
except IndexError:
    print(helper)
except NameError:
    print(helper)
except TypeError:
    print(helper)









