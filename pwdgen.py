import getopt, random, string, sys

usage = "\n\tCommand usage:\tpwdgen.py -lx -n -s\n\t\t\
Where x is an integer defining password lenght\n\t\t\
And \"charset\" is available options:\n\n\t\t\t\
l = only lower\n\t\t\tu = only upper\n\t\t\t\
n = only numbers\n\t\t\ts = only symbols.\n\n\t\t\
There are also combinations available:\n\n\t\t\t\
l,lu,lun,luns\n"

argomentiPassati = sys.argv[1:]

try:
    opts, args = getopt.getopt(argomentiPassati, "l:nsS")
    
except getopt.GetoptError:
    print(usage)

try:
    for opt, arg in opts:
        if opt in ['-l']:
            argomento_stringa = arg
            length = int(argomento_stringa)
            chars = string.ascii_letters 
        elif opt in ['-n']:
            chars = string.ascii_letters + string.digits
        elif opt in ['-s']:
            chars = string.ascii_letters + '!@#$%^&*()'
        elif opt in ['-S']:
            chars = string.ascii_letters + '!@#$%^&*()' + string.digits
    
#        random.seed = (os.urandom(1024))

        password = "".join(random.choice(chars) for i in range(length))

        print(password)
    
except:
    print(usage)
