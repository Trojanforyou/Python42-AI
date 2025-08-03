#! /usr/bin/env python3

kata = (0, 4, 132, 42222, 10000, 12345.67)

def main():
    dec_part = str(kata[3])[:2]
    res = f"{kata[2]}.{dec_part}"
    print(f"module_{kata[0]:02d} ex{kata[1]:02d} : {res}, {kata[4]:.2e}, {kata[5]:.2e}")    

if (__name__ == "__main__"):
    main()