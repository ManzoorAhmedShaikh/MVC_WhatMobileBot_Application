import requests
import json
from Utilities._StatusUpdate import *

class ProxiesCrawler:

    def __init__(self, views):
        self.view = views

    def get_proxies(self):
        '''
        It will fetch the 15 free working proxies to utilize in the code, in order to avoid getting BAN.
        :return: (list) -> A 2D list that contains the Proxy and its protocol which is used for scrapping
        '''
        print("get_proxies() Started")

        valid_proxies = []
        try:
            update_status_text(self,StatusText=Status.STATUS4)
            response = requests.get('https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc')
            if response.status_code == 200:
                raw_proxies = json.loads(response.text)

                proxies = [x['ip'].strip() + ":" + x['port'].strip() for x in raw_proxies['data']]
                proxies_protocols = [x['protocols'][0] for x in raw_proxies['data']]
                for proxies_protocol,proxy in zip(proxies_protocols,proxies):
                    try:
                        res = requests.get('https://ifconfig.me/', proxies={proxies_protocol:proxy})

                        if res.status_code == 200:
                            print(f"Valid Proxy: {proxy} with protocol: {proxies_protocol}")
                            valid_proxies.append([proxy,proxies_protocol])

                        if len(valid_proxies) >= 15:
                            break

                    except Exception as er:
                        continue

                print(f"Total Valid Proxies we get: {len(valid_proxies)}")
                update_status_text(self,StatusText=Status.STATUS5)
                return valid_proxies

            else:
                update_error_text(self, StatusText = Error.ERROR2 ,Seconds = 2)
                return valid_proxies

        except Exception as error:
            print(f"get_proxies() Error -> {error}")
            update_error_text(self, Seconds = 2)
            return valid_proxies

        print("get_proxies() ended")
