from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumUtils:

    def __init__(self):
        Options = self.GetChromePreferences()
        self.keys = Keys()
        self.driver = Chrome(service= Service(ChromeDriverManager().install()),options= Options)
        self.driver.implicitly_wait(15)

    def GetElement(self, Xpath : str):
        """
        It will get the single element available on the webpage
        :param Xpath: (str) -> The xpath for the web element
        :return: (WebElement) -> It will return the webelement (Selenium Object) if found, otherwise an empty list
        """

        Element = []
        try:
            Element = self.driver.find_elements(By.XPATH, Xpath)
            if len(Element) > 0:
                return Element[0]
            else:
                return Element

        except Exception as error:
            print(f"Error in Getting the element with Error -> {error}")
            return Element

    def GetElements(self, Xpath : str):
        """
        It will find multiple elements available on the webpage in a list
        :param Xpath: (str) -> The xpath for the web element
        :return: (list) -> Return the List of web elements, if nothing found, return an empty list
        """

        Elements = []

        try:
            Elements = self.driver.find_elements(By.XPATH, Xpath)

        except Exception as error:
            print(f"Error in Getting the list of elements with Error -> {error}")

        return Elements

    def IsElementPresent(self, Xpath : str):
        """
        It will find the availability of the element in the webpage
        :param Xpath: (str) -> The xpath for the web element
        :return: (bool) -> Return True if element avaiable on Webpage, otherwise False
        """

        Visible = False

        try:
            if not isinstance(self.GetElement(Xpath), list):
                Visible = True

            return Visible

        except Exception as error:
            print(f"Error in Checking the element availability with Error -> {error}")
            return Visible

    def ClickElement(self, Xpath : str):
        """
        It will click the element available on the webpage
        :param Xpath: (str) -> The xpath for the web element
        :return: None
        """

        try:
            Element = self.GetElement(Xpath)
            if Element is not None:
                Element.click()
            else:
                print("Element not found")

        except Exception as error:
            print(f"Error in Clicking the element with Error -> {error}")

    def InsertKeys(self,Value : str, Xpath : str):
        '''
        It will insert the keys in any input field with Xpath (str) given
        :param Value: (str) -> The Value to give in the input field
        :param Xpath: (str) -> The xpath for the web element
        :return:
        '''
        try:
            Element = self.GetElement(Xpath)
            if Element is not None:
                Element.send_keys(Value)

            else:
                print("Element not found")

        except Exception as error:
            print(f"Error in Sending the keys to the element with Error -> {error}")

    def NavigateToPage(self, url : str):
        '''
        It will navigate the browser (Chrome) to desired web page with (url)
        :param url: (str) -> A Link to where you want to navigate
        :return: (Webdriver)
        '''

        self.driver.get(url)

        return self.driver


    def GetChromePreferences(self):
        '''
        Get all the necessary Chrome Options which is recommended for best performance in Headless Mode
        :return: (ChromeOptions)
        '''

        options = Options()

        options.add_argument("--headless") # Headless mode
        options.add_argument("--disable-gpu") # Disable GPU hardware acceleration
        options.add_argument("--disable-infobars") # Disable browser UI components
        options.add_argument("--disable-extensions") # Disable browser UI components
        options.add_argument("--no-sandbox") # Disable sandbox mode (useful for some OS configurations)
        options.add_argument("--ignore-certificate-errors") # Ignore certificate errors
        options.add_argument("--disable-dev-shm-usage") # Disable dev-shm-usage (necessary for some environments, like Docker)
        options.add_argument("--log-level=3") # Disable logging
        options.add_argument("--window-size=1920x1080") # Set window size (important for headless mode)
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3") # User agent to avoid detection

        return options