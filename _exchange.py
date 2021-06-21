import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="

bozulanDoviz = input("Bozulan döviz türü: ")
alinanDöviz = input("Alınan döviz türü: ")
miktar = int(input(f"Ne kadar {bozulanDoviz} bozdurmak istiyorsunuz: "))

result = requests.get(api_url+bozulanDoviz)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulanDoviz, result["rates"][alinanDöviz],alinanDöviz))
print("{0} {1} = {2} {3}".format(miktar,bozulanDoviz,miktar*result["rates"][alinanDöviz],alinanDöviz))
