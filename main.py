import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help = "Write here your name")
args = parser.parse_args()
print(f"Hello {args.name}, how are you")