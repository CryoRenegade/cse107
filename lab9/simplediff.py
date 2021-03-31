import difflib
import sys

def diff():
    file1 = open(input("What file do you want to diff?")).readlines()
    file2 = open(input("What is the other file do you want to diff?")).readlines()
    delta = difflib.unified_diff(file1, file2)
    return delta

def main():
    delta = diff()
    sys.stdout.writelines(delta)

if __name__ == "__main__":
    main()