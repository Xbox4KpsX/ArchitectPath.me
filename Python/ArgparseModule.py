import argparse

# the first step is to create the object of ArgumentParser
parser = argparse.ArgumentParser(description='Test argparse.')

# add arguments
parser.add_argument("-t", "--test", default = 100, type = int, help = "just try")
parser.add_argument("-v", "--verbose", type = str, help = "verbose is ?")

# parse arguments
args = parser.parse_args()
print(args)
print(args.verbose)
print(args.test)

args.verbose = "thank you ~" if args.verbose is None else not None
print(args.verbose)

def paint():
    print("paint")
    def paintA():
        print("paintA")
    paintA()

paint()



