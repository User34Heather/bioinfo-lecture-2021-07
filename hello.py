#!/usr/bin/python

import sys

print(sys.argv)
# sys.exit

name = sys.argv[1]   #리스트에서 1번째 리스트를 가져와서 argument에 넣는다.
name2 = sys.argv[2]

print(f"Hello {name}")
print(f"hello {name2}")

