import requests

try:
    string = ""
    texto = requests.get("http://www.g1.com")
    #print(texto.text)
    string = texto.text

    item = "body"

    for i in range(len(string)):
        achou = 0
        if(string[i] == "b" or string[i] == "B"):
            idx = i
            flag = 0
            for j in range(len(item)):
                if string[idx] == item[j]:
                    idx = idx + 1
                    flag = flag + 1
                if(flag == len(item)):
                    print("Achou")
                    achou = 1;
                    break;
            if(achou != 0):
                print("Parou")
                break

except Exception as e:
    print(e.args)
