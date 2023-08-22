import requests
import re


url = input('Введите страницу: ')

#url = 'http://www.columbia.edu/~fdc/sample.html'

response = requests.get(url).text

res = re.findall(r'>.+</h3>', response)
release = list(map(lambda x: x[1:-5], res))
print(release)