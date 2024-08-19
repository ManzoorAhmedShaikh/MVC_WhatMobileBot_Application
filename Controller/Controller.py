from Utilities._StatusUpdate import *
import threading
from Crawler.MobileByBrandsCrawler import MobileByBrandsCrawler
from Crawler.MobileByNamesCrawler import MobileByNamesCrawler

class Controller:

    def __init__(self, model, view):
        self.view = view
        self.model = model
        self.view.SearchNExportBtn.configure(command = self.SearchNExportMobiles)

    def SearchNExportMobiles(self):
        '''
        It will triggered if the Search and Export button pressed, Based on the values inserted on the Texbox,
        or Checkbox checked, it will scrap respectively
        :return: None
        '''

        if self.view.SearchByBrandFrame.winfo_viewable() == 1:
            brands_filter = self.view.fetch_checkboxes_values()

            if 1 in list(brands_filter.values()):
                mobile_by_brands_data = {}
                self.view.SearchNExportBtn.configure(state = 'disabled')
                self.view.BackToMenu_Btn.configure(state = 'disabled')
                self.view.SearchNExportBtn.update()
                self.view.BackToMenu_Btn.update()
                update_status_text(self,StatusText = Status.STATUS6, Seconds=2)
                update_status_text(self,StatusText = Status.STATUS2, Seconds=2)

                threading.Thread(target=MobileByBrandsCrawler(views = self.view,FilterValue = brands_filter).start_scraping(mobile_by_brands_data)).start()
                if len(mobile_by_brands_data) > 0:
                    update_status_text(self, StatusText=Status.STATUS15)
                    file_status = self.model.export_mobile_by_brand_data(mobile_by_brands_data)

                    if file_status == "FILEPATH EMPTY":
                        update_status_text(self, StatusText=Error.ERROR3, FontColor = '#BF352B', Seconds = 2)

                    elif file_status == "FILE SAVED":
                        update_status_text(self, StatusText=Status.STATUS16, FontColor = "#50C878")

                update_status_text(self,StatusText = Status.STATUS1)
                self.view.SearchNExportBtn.configure(state = 'normal')
                self.view.BackToMenu_Btn.configure(state = 'normal')
                self.view.SearchNExportBtn.update()
                self.view.BackToMenu_Btn.update()

            else:
                update_status_text_warning_reset(self,StatusText = Status.STATUS1,WStatusText = Warning.WARNING1, WFontColor = "#BF352B", Seconds=2)

        elif self.view.SearchByMobileFrame.winfo_viewable() == 1:
            mobile_filter = self.view.fetch_entrybox_values()

            if len(mobile_filter) > 0:
                mobile_by_name_data = {}
                self.view.SearchNExportBtn.configure(state = 'disabled')
                self.view.BackToMenu_Btn.configure(state = 'disabled')
                self.view.SearchNExportBtn.update()
                self.view.BackToMenu_Btn.update()
                update_status_text(self,StatusText = Status.STATUS6, Seconds=2)
                update_status_text(self,StatusText = Status.STATUS3, Seconds=2)

                threading.Thread(target=MobileByNamesCrawler(views = self.view,FilterValue = mobile_filter).start_scraping(mobile_by_name_data)).start()
                if len(mobile_by_name_data) > 0:
                    update_status_text(self, StatusText=Status.STATUS15)

                    mobile_name = mobile_by_name_data["Mobile Name"]
                    file_status = self.model.export_mobile_by_name_data(Data_dict = mobile_by_name_data, FileName = mobile_name)

                    if file_status == "FILEPATH EMPTY":
                        update_status_text(self, StatusText=Error.ERROR3, FontColor = '#BF352B', Seconds = 2)

                    elif file_status == "FILE SAVED":
                        update_status_text(self, StatusText=Status.STATUS16, FontColor = "#50C878")

                update_status_text(self, StatusText=Status.STATUS1)
                self.view.SearchNExportBtn.configure(state='normal')
                self.view.BackToMenu_Btn.configure(state='normal')
                self.view.SearchNExportBtn.update()
                self.view.BackToMenu_Btn.update()

            else:
                update_status_text_warning_reset(self,StatusText = Status.STATUS1,WStatusText = Warning.WARNING2, WFontColor = "#BF352B", Seconds=2)