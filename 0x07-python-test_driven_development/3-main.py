#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("Olayode", "yusuf")
say_my_name("Doctware the", "coder")
say_my_name("yusclever", "C")

try:
    say_my_name(12, "Black")
except Exception as e:
    print(e)
