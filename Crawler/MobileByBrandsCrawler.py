import requests
from bs4 import BeautifulSoup
from Utilities._Proxies import ProxiesCrawler
from Utilities._StatusUpdate import *
import random

class MobileByBrandsCrawler:

    def __init__(self, views, FilterValue):
        self.view = views
        self.Filter = {x:y for x,y in  FilterValue.items() if y != 0}

    def start_scraping(self, Data_dict : dict):
        '''
        It will scrap the website based on Filter values (Mobile Brands) and save it to Data_Dict parameter
        :param Data_dict: (dict) -> A Multi-dimensional Dictionary to store data of Mobile brands
        :return: None
        '''

        print('start_scraping() Started')
        URL = "https://www.whatmobile.com.pk/"
        try:
            Proxies = ProxiesCrawler(self.view).get_proxies()
            if len(Proxies) > 0:
                for brand in list(self.Filter.keys()):
                    update_status_text(self, StatusText=Status.STATUS7.format(brand.upper()))

                    res = requests.get(URL + brand + "_Mobiles_Prices", proxies = {random.choice(Proxies)[1]: random.choice(Proxies)[0]}).text
                    soup = BeautifulSoup(res, 'html.parser')

                    Names = [name.find_next('a').attrs['title'].replace('price','').strip() for name in soup.find_all('h4')]
                    Links = [URL[:-1] + link.find_next('a').attrs['href'].strip() for link in soup.find_all('h4')]
                    Prices = [price.find_next('span').text.strip() if "N/A" not in price.find_next('span').text.strip() else "N/A"  for price in soup.find_all('h4')]

                    Data_dict.update({
                        brand: {
                            "Mobile Name" : Names,
                            "Mobile Price" : Prices,
                            "Mobile Link" : Links
                        }
                    })
                    update_status_text(self, StatusText=Status.STATUS8.format(brand.upper()))

                update_status_text(self, StatusText=Status.STATUS10, FontColor = "#50C878", Seconds = 2)

            else:
                update_status_text(self,StatusText=Status.STATUS1)

        except Exception as error:
            print(f"start_scraping() Error -> {error}")
            update_error_text(self)
        print('start_scraping() Ended')
