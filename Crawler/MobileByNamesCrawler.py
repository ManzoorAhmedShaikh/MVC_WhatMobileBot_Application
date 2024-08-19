from bs4 import BeautifulSoup
from Utilities._StatusUpdate import *
from Utilities._Selenium import SeleniumUtils
import os

class MobileByNamesCrawler:

    def __init__(self, views, FilterValue: str):
        self.view = views
        self.Filter = FilterValue
        self.Sel = SeleniumUtils()

    def start_scraping(self, Data_dict : dict):
        '''
        It will scrap the website based on Filter values (Mobile Name) and save it to Data_Dict parameter
        :param Data_dict: (dict) -> A Dictionary to store data of Mobile Specs
        :return: None
        '''

        print('start_scraping() Started')

        URL = 'https://www.whatmobile.com.pk'
        try:
            self.Sel.NavigateToPage(URL)
            WaitOne()
            update_status_text(self, StatusText=Status.STATUS9.format(URL.split("//")[-1]))
            self.search_and_scrap(Data_dict)

            self.view.clear_entrybox_values()
            os.system("taskkill /f /im chromedriver.exe /T")

        except Exception as error:
            print(f"start_scraping() Error occured -> {error}")
            update_error_text(self)
        print('start_scraping() Ended')

    def search_and_scrap(self,Data_dict : dict):
        """
        It will search the Mobile on website and scrap its features
        :param Data_dict: (dict) -> A Dictionary to store data of Mobile Specs
        :return: None
        """

        print('search_and_scrap() Started')

        search_file_path = '//input[@id="searchInput"]'
        no_mobile_path = "//div[@id='livesearch' and not(contains(@style,'none'))]//div[.='No mobile found!' or contains(.,'Invalid input')]"
        first_mobile_path = '(//div[@id="livesearch" and not(contains(@style,"none"))]//div[@class="searchDiv"]//a)[1]'
        exact_mobile_path = '//div[@id="livesearch" and not(contains(@style,"none"))]//div[@class="searchDiv"]//a[translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz") = "{0}"]'
        mobile_name_path = "//div[starts-with(@class,'Heading1')]/h2"
        mobile_data_path = mobile_name_path + '/following-sibling::table'

        try:
            update_status_text(self, StatusText=Status.STATUS11.format(self.Filter))
            self.Sel.InsertKeys(self.Filter, search_file_path)
            WaitCustom(2)

            if self.Sel.IsElementPresent(no_mobile_path):
                update_status_text_warning_reset(self,StatusText = Status.STATUS1,WStatusText = Warning.WARNING3, WFontColor = "#BF352B", Seconds=2)

            else:
                self.Sel.ClickElement(exact_mobile_path.format(self.Filter.lower())) if self.Sel.IsElementPresent(exact_mobile_path.format(self.Filter.lower())) else self.Sel.ClickElement(first_mobile_path)
                WaitOne()

                mobile_name = self.Sel.GetElement(mobile_name_path).text.split('detailed')[0].strip()
                update_status_text(self, StatusText=Status.STATUS12.format(mobile_name))
                update_status_text(self, StatusText=Status.STATUS13.format(mobile_name))
                Data_dict.update({"Mobile Name": mobile_name})

                self.parse_table_data(mobile_data_path, Data_dict)
                update_status_text(self, StatusText=Status.STATUS14.format(mobile_name),FontColor='#50C878')

        except Exception as error:
            print(f"search_and_scrap() Error occured -> {error}")
            update_error_text(self)
        print('search_and_scrap() Ended')

    def parse_table_data(self,mobile_data_path : str, Data_dict : dict):
        """
        It will parse the table that contains all the features of the searched Mobile
        :param Data_dict: (dict) -> A Dictionary to store data of Mobile Specs
        :return: None
        """

        print('parse_table_data() Started')

        tables_html = self.Sel.GetElements(mobile_data_path)
        if len(tables_html) > 0:
            for table_html in tables_html:
                if table_html is not None:
                    table_html = table_html.get_attribute('innerHTML')
                    soup = BeautifulSoup(table_html,'html.parser')

                    #Parsing Specs Heading
                    headings = [tr.find(attrs = {'class':'specs-mainHeading'}).text.strip() if tr.find(attrs = {'class':'specs-mainHeading'}) is not None else '' for tr in soup.find_all('tr') ]
                    for i in range(len(headings)):
                        if len(headings[i]) == 0:
                            headings[i] = headings[i - 1]

                    #Parsing Specs SubHeading
                    sub_headings = [tr.find_next(attrs = {'class':'specs-subHeading'}).text.strip() for tr in soup.find_all('tr')]
                    if sub_headings[-2].lower().startswith('price in rs'):
                        sub_headings[-1], sub_headings[-2] = ['', '']

                    #Parsing Specs Value
                    values_soup = [tr.find_next(attrs={'class':'specs-value'}) for tr in soup.find_all('tr') if tr.find_next(attrs={'class':'specs-value'}) is not None]
                    if len(values_soup) == 0:
                        values_soup = [tr.find_next(attrs={'class': 'specs-subHeading'}) for tr in soup.find_all('tr') if tr.find_next(attrs={'class': 'specs-subHeading'}) is not None]
                    values = [value.text.strip().replace('\xa0','').replace('\n',' ') for value in values_soup if value is not None]

                    #Creating the data dictionary
                    for heading,sub_heading,value in zip(headings,sub_headings,values):
                        if sub_heading.strip() == '':
                            Data_dict[heading] = value
                        else:
                            Data_dict[heading + " - " + sub_heading] = value


                else:
                    print("Element not found")
                    update_status_text_warning_reset(self, StatusText=Status.STATUS1, WStatusText=Warning.WARNING5,WFontColor="#BF352B", Seconds=2)

        else:
            update_status_text_warning_reset(self, StatusText=Status.STATUS1, WStatusText=Warning.WARNING4, WFontColor="#BF352B", Seconds=2)

        print('parse_table_data() Ended')