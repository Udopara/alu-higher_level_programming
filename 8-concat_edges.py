#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\n language that combines remarkable power with very clear syntax"
str = str[str.index("object"): str.index("\n") ] + " " + str[str.index("with"): str.index(" very") ] + " " + str[str.index("Python"): str.index(" is") ]
print(str)