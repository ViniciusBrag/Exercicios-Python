import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O Site pudim não está disponível')
else:
    print('Site está disponivel')


