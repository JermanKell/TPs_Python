#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

id = "raphlazz"
pwd = "arccho"

# On recupere le nom venant de la requete ou de l'URL et on le stocke dans une variable pour affichage
userName = form.getvalue("name")
userPwd = form.getvalue("password")

url = "http://localhost:8888/"

#Code HTML avec requete a executer des l'appui sur le bouton envoyer
html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    No connected user
    <form action="/index.py" method="post">
        <input type="text" name="name" value="Your id" />
        <input type="text" name="password" value="Your password"/>
        <input type="submit" name="send" value="Envoyer information au serveur">        
    </form>
</body>
</html>
"""

# Dans le cas ou les credentiels sont identiques, on redirige
if (id == userName and pwd == userPwd):
    refURL = url + "auth_page.py?name=" + userName + "&password=" + userPwd
    html2 = """<!DOCTYPE html>
    <head>
        <meta http-equiv="refresh" content="0;url='%s'" />
    </head>
    </html>
    """ % (refURL)
    print(html2)

print(html)