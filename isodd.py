#!/usr/bin/env python
import webbrowser
import sys

if len(sys.argv) > 1:
	number = sys.argv[1]
else:
	number = input("Enter a number to determine if it is odd: ")

webbrowser.open("https://www.wolframalpha.com/input/?i=is+" + str(number) + "+an+odd+number")