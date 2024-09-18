import argparse

parser = argparse.ArgumentParser(
    prog="argparsetest.py",
    description="IdK",
    epilog="Arguments: x value"
)

parser.add_argument("-c --count")
parser.add_argument("filename")
args = parser.parse_args()

print(parser)