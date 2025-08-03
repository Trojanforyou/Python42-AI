#! /usr/bin/env python3
kata = (19, 42, 21)

def main():
    print(f"The {len(kata)} numbers are: {', '.join(map(str, kata))}")
if (__name__ == "__main__"):
    main()