#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

name = form.getvalue("name")

html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    Connected as %s  
    
    You are allowed to go wherever you want on the internet   
</body>
</html>
""" % (name)

print(html)