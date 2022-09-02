#webscrape the data from the imdb for top 250 movies
#https://www.imdb.com/chart/top/?ref_=nv_mv_250
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Basappa\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
soup = BeautifulSoup(driver.page_source, 'lxml')
table = soup.find('table', class_='chart')
for td in table.find_all('td', class_='titleColumn'):
    print(td.text.strip().replace('\n', '      '))
    print(td.a['href'])
    print('https://www.imdb.com' + td.a['href'])
    print('')
driver.quit()

from IPython.utils.py3compat import MethodType


#/**this is my main method
#!only static
#?Exception
#todo: call MethodType
#**/