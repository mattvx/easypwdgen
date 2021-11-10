import getopt, random, string, sys

usage = "Python random password generator.\n \
        You must provide: -l xxx ---> Lenght of the password\n\
        If no options are specified, default charset is lower+upper\n\
        One of these options:\n\
        -n -> lower+upper+digits \n\
        -s -> lower+upper+symbols \n\
        -S -> lower+upper+digits+symbols

argomentiPassati = sys.argv[1:]

try:
    opts, args = getopt.getopt(argomentiPassati, "l:nsS")
    
except getopt.GetoptError:
    print(usage)

try:
    for opt, arg in opts:
        if opt in ['-l']:
            length = int(arg)
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
