from pynput.mouse import Controller, Button
from time import sleep
import requests
from bs4 import BeautifulSoup

mouse =  Controller()

url = "https://apprentissage.appli1.projet-voltaire.fr/exercise"

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print(response.text)

    soup = BeautifulSoup(response.text, 'html.parser')

    elements = soup.find_all(class_='css-146c3p1')    

    for element in elements:
        print(element.text)
else:
    print('Failed to retrieve the webpage')
    
    
