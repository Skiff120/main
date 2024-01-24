import requests

coin_list = []

'''response = requests.get("https://bank.gov.ua/ua/markets/exchangerates/")
response_text = response.text
response_parse = response_text.split("<td>")
for parse_elem in response_parse:
    if parse_elem.("\"Офіційний курс\""):
        print("Ok")
        for parse_elem_2 in parse_elem.split("</tr>"):
            if parse_elem_2.startswith("3"):
                coin_list.append(parse_elem_2.split("3")[1])


#print(float(coin_list[0].replace(",", "")))'''




from bs4 import BeautifulSoup

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td",{'data-label':"Офіційний курс"})
    print(soup_list[7].text)