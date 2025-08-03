#! /usr/bin/env python3
import sys

def text_analizer(string):
    counts = {
        'upper': 0,
        'lower': 0,
        'spaces': 0,
        'punctuation': 0,
        'printable': 0,
    }
    for i in string:
        if (i.islower()):
            counts["lower"] += 1
        if (i.isupper()):
            counts["upper"] += 1
        if (i == " "):
            counts["spaces"] += 1
        if (i.isprintable()):
            counts["printable"] += 1
        if (i == "." or i == "," or i == "!" or i == "?"):
            counts["punctuation"] += 1
    print(f"The text contains {counts['printable']} printable character(s):" )
    print(f"-{counts['upper']} upper letter(s)\n-{counts['lower']} lower letter(s)\n-{counts['punctuation']} punctuation mark(s)\n-{counts['spaces']} space(s)")
def main():
    if (len(sys.argv) < 2):
        text = input("What is the string: ")
        text_analizer(text)
    elif (len(sys.argv) > 2):
        print("ERROR: Too many arguments")
        return
    else:
        text_analizer(sys.argv[1])
if __name__ == "__main__":
    main()
