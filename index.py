#!C:/Users/1chi/AppData/Local/Microsoft/WindowsApps/python.exe

import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-Type: text/html; charset=utf-8")
print()
print("<h1> Hello, CGI</h1>", end="")
with open("homepage.html", encoding="utf-8") as file:
    print(file.read(), end="")
