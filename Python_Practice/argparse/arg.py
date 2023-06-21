# import argparse

# ## There are two types of arguments argparse support
# # Positional argument
# # Optional argument

# ## Positional Arguments
# if __name__ == "__main__":
#     ## Initialize a parser object
#     parser = argparse.ArgumentParser()
#     ## adding an argument using the parser
#     # 1st parameter = name of the argument; 2nd param = help
#     parser.add_argument("number1", help = "first number")
#     parser.add_argument("number2", help = "second number")
#     parser.add_argument("operation", help = "operation")
    
#     args = parser.parse_args()
#     print(args.number1)
#     print(args.number2)
#     print(args.operation)

#     n1 = int(args.number1)
#     n2 = int(args.number2)
#     result = None

#     if args.operation == "add":
#         result = n1+n2
#     elif args.operation == "sub":
#         result = n1-n2
#     elif args.operation == "mul":
#         result = n1*n2
#     elif args.operation == "div":
#         result = n1/n2

#     print(f"Result: {result}")


# import argparse

# ## There are two types of arguments argparse support
# # Positional argument
# # Optional argument

# ## Optional Arguments
# ## Use "--"
# if __name__ == "__main__":
#     ## Initialize a parser object
#     parser = argparse.ArgumentParser()
#     ## adding an argument using the parser
#     # 1st parameter = name of the argument; 2nd param = help
#     parser.add_argument("--number1", help = "first number")
#     parser.add_argument("--number2", help = "second number")
#     parser.add_argument("--operation", help = "operation")
    
#     args = parser.parse_args()
#     print(args.number1)
#     print(args.number2)
#     print(args.operation)

#     n1 = int(args.number1)
#     n2 = int(args.number2)
#     result = None

#     if args.operation == "add":
#         result = n1+n2
#     elif args.operation == "sub":
#         result = n1-n2
#     elif args.operation == "mul":
#         result = n1*n2
#     elif args.operation == "div":
#         result = n1/n2
#     else:
#         print("Unsupported Operation!")

#     print(f"Result: {result}")

import argparse

## There are two types of arguments argparse support
# Positional argument
# Optional argument

## Restrict user from passing argument
if __name__ == "__main__":
    ## Initialize a parser object
    parser = argparse.ArgumentParser()
    ## adding an argument using the parser
    # 1st parameter = name of the argument; 2nd param = help
    ## we don't want users to use division operation
    parser.add_argument("--number1", help = "first number")
    parser.add_argument("--number2", help = "second number")
    parser.add_argument("--operation", help = "operation",
                        choices = ['add', 'sub', 'mul'])
    
    args = parser.parse_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None

    if args.operation == "add":
        result = n1+n2
    elif args.operation == "sub":
        result = n1-n2
    elif args.operation == "mul":
        result = n1*n2
    elif args.operation == "div":
        result = n1/n2
    else:
        print("Unsupported Operation!")

    print(f"Result: {result}")

