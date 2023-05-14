#!/usr/bin/env python
import sys

def mail(s):
   digits = "0123456789"
   tokens = s.split("@")
   [first, last] = tokens[0].strip(digits).split('.')
   name = first.capitalize() + " " + last.capitalize()

   return name

def email():

   for line in sys.stdin:
      tokens = line.strip()
      print(mail(tokens))

if __name__ == '__main__':
   email()
