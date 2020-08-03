import requests
import threading

def find_files(url_input,domain):
    
    try:
        global request
        request = requests.get(f"http://{url_input}/{domain}",timeout=0.4)
    except:
        pass
    
    url = f"{request}"
    
    server_response_code = int(url[11:14])

    if 200<=server_response_code<=299:
        print(f"found: {domain}")
    

url_input = input("Url: ")

domains = open('domains.txt','r')

for domain in domains:
    thread = threading.Thread(target=find_files, args = (url_input,domain,))
    find_files(url_input,domain)    




