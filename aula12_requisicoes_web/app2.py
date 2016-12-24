#Beautiful Soup 4 BS4 - pip install bs4

#Site para testar as requisições - https://putsreq.com/

import requests

try:
    string = ""
    texto = requests.request("https://putsreq.com/5vebcqga9k9ykDsdGylr")
    print(texto.text)
    string = texto.text

except Exception as e:
    print(e.args)