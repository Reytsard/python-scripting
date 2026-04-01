import argparse

def run(name, times):
    for _ in range(0,times):
        print(f"Roll a Dice {name}!")


def main():
    parser = argparse.ArgumentParser(description="Greet number of times indicated by the argument.") #a description for the argparse
    
    parser.add_argument("name",help="Input name for greeting") # first argument (no need double dashes)
    parser.add_argument("--times", type=int, default=1, help="times to repeat")

    args = parser.parse_args() # doing this will now have .name and .times
    run(args.name, args.times) # make code more modular by separating the logic into a different function.
    
if __name__ == "__main__":
    main()

#when using the code, you cant use code without an argument for "name"
#so that means when we input "python hello-times.py", it will throw an error
# so we need a value, "python hello-times.py <name>", this will work (name = <name>, times = 1(default))
# even "python hello-times.py <name> --times <number>" this will also work (name = <name>, times = <number>)
