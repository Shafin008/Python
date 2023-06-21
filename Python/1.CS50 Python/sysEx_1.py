import sys
## Ex.4: handling errors(Version 3) with sys.exit()
if len(sys.argv) < 2:
    sys.exit("Too few arguments.")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments.")

print("Hello, my name is", sys.argv[1])
