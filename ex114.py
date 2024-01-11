import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://pomofocus.io")
except urllib.error.URLError:
    print("O site não está acessível no momento.")
else:
    print("consegui acessar o site com sucesso!")
    print(site.read())
