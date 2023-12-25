import os
import sys


def main():
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

    file = open("1/input.txt", "r")
    content = file.readlines()

    result = 0

    for line in content:
        a = ""
        
        for i,c in enumerate(line):
            if c.isdigit():
                a += c
            for d, val in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if line[i:].startswith(val):
                    a += str(d)
        
        num = a[0] + a[-1]
        result += int(num)
    return result
    

if __name__ == "__main__":
    print(main())

            
            

