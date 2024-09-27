import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
        
        s = s.strip()
        yum_list = re.findall(r'(\bum\b)', s, re.IGNORECASE)
        list_no = len(yum_list)
        return list_no


if __name__ == "__main__":
    main()