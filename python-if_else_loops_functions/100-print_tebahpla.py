#!/usr/bin/python3

print("".join(f"{chr(c - (32 * (c % 2)))}" for c in range(122, 96, -1)), end="")

