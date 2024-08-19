from Utilities._Time import *
from Utilities._Logs import *

def update_status_text(self, StatusText: str, FontColor: str = '#151515', Seconds: int = 1):
    '''
    It will update the Status text, color, and hold that status for your desired time in seconds
    :param StatusText: (str) -> The message to show on Status section
    :param FontColor: (str) -> Color Hex code or english Alphabets color for the status text
    :param Seconds: (int) -> The amount of time to hold the Status text
    :return: None
    '''

    self.view.StatusofAll.configure(text=StatusText, text_color=FontColor)
    self.view.StatusofAll.update()
    WaitCustom(Seconds)

def update_status_text_warning_reset(self, StatusText: str, WStatusText: str, FontColor: str = '#151515', WFontColor: str = '#151515', Seconds: int = 1):
    '''
    It will update the Status text WARNING and Button, color, and hold that status for your desired time in seconds and then reset it to original
    :param StatusText: (str) -> The message to show on Status section
    :param WStatusText: (str) -> The warning to show on Status section
    :param FontColor: (str) -> Color Hex code or english Alphabets color for the status text
    :param WFontColor: (str) -> Color Hex code or english Alphabets color for the status warning text
    :param Seconds: (int) -> The amount of time to hold the Warning Status text
    :return: None
    '''

    self.view.StatusofAll.configure(text=WStatusText, text_color=WFontColor)
    self.view.SearchNExportBtn.configure(fg_color = WFontColor)
    self.view.SearchNExportBtn.update()
    self.view.StatusofAll.update()

    WaitCustom(Seconds)

    self.view.StatusofAll.configure(text=StatusText, text_color=FontColor)
    self.view.SearchNExportBtn.configure(fg_color = '#1f4cad')
    self.view.SearchNExportBtn.update()
    self.view.StatusofAll.update()

def update_error_text(self, StatusText: str = Error.ERROR1, Seconds: int = 1):
    '''
    It will update the Status to show Error message and then reset to original
    :param StatusText: (str) -> The Error to show on Status section
    :param Seconds: (int) -> Time till then to show the status in seconds
    :return: None
    '''

    self.view.StatusofAll.configure(text=StatusText, text_color='#BF352B')
    self.view.StatusofAll.update()

    WaitCustom(Seconds)

    self.view.StatusofAll.configure(text=Status.STATUS1, text_color='#151515')
    self.view.StatusofAll.update()