import customtkinter
from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
from webbrowser import open

class View:
    def __init__(self, root):

        customtkinter.set_appearance_mode('light')

        self.root = root
        self.root.title("WhatMobile Bot")
        self.root.geometry('650x550')
        self.root.resizable(False, False)
        self.root.configure(fg_color='white')
        icon_img = PhotoImage(file = "Assets/APP_Icon.gif")
        self.root.tk.call('wm','iconphoto',self.root._w,icon_img)
        # self.root.iconbitmap("Assets/APP_Icon.ico") #Incase of Windows

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.design_window()

    def design_window(self):
        '''
        Design the complete WhatMobile Bot App with their interactive Widgets
        :return: None
        '''

        # Option Menu Frame defining
        self.OptionMenuFrame = CTkFrame(self.root, border_width=0,bg_color='white', fg_color='white')
        self.OptionMenuFrame.grid_rowconfigure(0, weight=1)
        self.OptionMenuFrame.grid_rowconfigure(1, weight=1)
        self.OptionMenuFrame.grid_rowconfigure(2, weight=1)

        #Execution Frame defining
        ExecutionFrame = CTkFrame(self.root, border_width=0,bg_color='white', fg_color='white')
        ExecutionFrame.grid_rowconfigure(0, weight=1)
        ExecutionFrame.grid_rowconfigure(1, weight=2)
        ExecutionFrame.grid_columnconfigure(0, weight=1)

        #SearchByMobileFrame Defining
        self.SearchByMobileFrame = CTkFrame(self.root, border_width=0,bg_color='white', fg_color='white')
        self.SearchByMobileFrame.grid_columnconfigure(0,weight=1)
        self.SearchByMobileFrame.grid_columnconfigure(1,weight=1)

        #SearchByBrandFrame Defining
        self.SearchByBrandFrame = CTkFrame(self.root, border_width=0,bg_color='white', fg_color='white')
        self.SearchByBrandFrame.grid_rowconfigure(0, weight=1)
        self.SearchByBrandFrame.grid_rowconfigure(1, weight=1)
        self.SearchByBrandFrame.grid_rowconfigure(2, weight=1)

        # Footer Frame Defining
        FooterFrame = CTkFrame(self.root,bg_color='white', fg_color='white')

        #Logo Header Defining
        Icon = CTkLabel(self.root,text = '', fg_color='white', bg_color='white', image = PhotoImage(file = 'Assets/Logo.png'))

        self.BackToMenu_Btn = CTkButton(self.root,text="BACK TO MAIN", corner_radius=10,  font = ('Arial Black', 15, 'bold'),  bg_color='white',hover_color= '#151515', fg_color='#1f4cad', command = self.back_to_menu)
        #Option Menu Button Widgets Defining
        self.SearchByMobile_Btn = CTkButton(self.OptionMenuFrame,text="SEARCH BY MOBILE", corner_radius=10,  font = ('Arial Black', 15, 'bold'),  bg_color='white',hover_color='#1f4cad', fg_color='#151515', command = self.search_by_mobile_frame)
        self.SearchByBrand_Btn = CTkButton(self.OptionMenuFrame,text="SEARCH BY BRAND", corner_radius=10,  font = ('Arial Black', 15, 'bold'),  bg_color='white', hover_color='#1f4cad', fg_color='#151515', command = self.search_by_brand_frame)

        #SearchByMobileFrame Widgets Defining
        self.MobileText = CTkLabel(self.SearchByMobileFrame, text='MOBILE', font=('Arial Black', 17.5, 'bold', 'underline'), text_color='#1f4cad')
        self.MobileNameText = CTkLabel(self.SearchByMobileFrame,text = 'MOBILE NAME', font = ('Arial Black', 18.5, 'bold'), text_color='#151515')
        self.MobileName_ENT = CTkEntry(self.SearchByMobileFrame, placeholder_text='Enter Mobile Name', width=200, bg_color='white', fg_color='white', border_color='#151515')

        #SearchByBrandFrame Widgets Defining
        self.BrandsText = CTkLabel(self.SearchByBrandFrame,text = 'BRANDS', font = ('Arial Black', 17.5, 'bold', 'underline'), text_color='#1f4cad')
        self.Apple = CTkCheckBox(self.SearchByBrandFrame,text = "APPLE" , font = ('Arial Black', 12.5, 'bold'), bg_color='white', text_color='#151515', border_color='#151515')
        self.Samsung = CTkCheckBox(self.SearchByBrandFrame,text = "SAMSUNG" , font = ('Arial Black', 12.5, 'bold'), bg_color='white', text_color='#151515', border_color='#151515')
        self.Huawei = CTkCheckBox(self.SearchByBrandFrame,text = "HUAWEI" , font = ('Arial Black', 12.5, 'bold'), bg_color='white', text_color='#151515', border_color='#151515')
        self.Xiaomi = CTkCheckBox(self.SearchByBrandFrame,text = "XIAOMI" , font = ('Arial Black', 12.5, 'bold'), bg_color='white', text_color='#151515', border_color='#151515')
        self.Nokia = CTkCheckBox(self.SearchByBrandFrame,text = "NOKIA" , font = ('Arial Black', 12.5, 'bold'), bg_color='white', text_color='#151515', border_color='#151515')
        self.Oppo = CTkCheckBox(self.SearchByBrandFrame,text = "OPPO" , font = ('Arial Black', 12.5, 'bold'), bg_color='white', text_color='#151515', border_color='#151515')
        self.Infinix = CTkCheckBox(self.SearchByBrandFrame,text = "INFINIX" , font = ('Arial Black', 12.5, 'bold'), bg_color='white', text_color='#151515', border_color='#151515')
        self.Tecno = CTkCheckBox(self.SearchByBrandFrame,text = "TECNO" , font = ('Arial Black', 12.5, 'bold'), bg_color='white', text_color='#151515', border_color='#151515')
        self.Lenovo = CTkCheckBox(self.SearchByBrandFrame,text = "LENOVO" , font = ('Arial Black', 12.5, 'bold'), bg_color='white', text_color='#151515', border_color='#151515')
        self.Realme = CTkCheckBox(self.SearchByBrandFrame,text = "REALME" , font = ('Arial Black', 12.5, 'bold'), bg_color='white', text_color='#151515', border_color='#151515')

        #Execution Frame Widgets Defining
        self.StatusofAll = CTkLabel(ExecutionFrame,text = 'EXECUTION NOT STARTED YET', font = ('Arial Black', 13.5, 'bold','underline'), text_color='#151515')
        self.SearchNExportBtn = CTkButton(ExecutionFrame, text = 'SEARCH AND EXPORT', corner_radius=10,  font = ('Arial Black', 15, 'bold'), bg_color='white',hover_color= '#151515', fg_color='#1f4cad')

        #Footer Widgets
        self.LinkedInBtn = CTkButton(FooterFrame,text = '',width=0,hover_color = 'white', image = self.resize_image('Assets/LinkedIn_Logo.png',45,25),fg_color='white', command=lambda: self.open_link("https://www.linkedin.com/in/manzoorahmedshaikh/"))
        self.FacebookBtn = CTkButton(FooterFrame,text = '',width=0,hover_color = 'white', image = self.resize_image('Assets/Facebook_Logo.png',45,25),fg_color='white', command=lambda: self.open_link("https://www.facebook.com/manzoorahmedshaikh234"))
        self.GithubBtn = CTkButton(FooterFrame,text = '',width=0,hover_color = 'white', image = self.resize_image('Assets/Github_Logo.png',25,25),fg_color='white', command=lambda: self.open_link("https://github.com/ManzoorAhmedShaikh"))
        FooterTextL = CTkLabel(FooterFrame,text = 'Developed By:')
        FooterTextR = CTkLabel(FooterFrame,text = 'Manzoor Ahmed', font = ('Arial Black', 14.5, 'bold'))

        #Logo Headers Widget Placement
        Icon.grid(row = 0, column = 0, columnspan = 3, sticky='', ipady = 5)

        #OptionMenuFrame Widgets Placement
        self.OptionMenuFrame.grid(row = 1, column = 0, sticky='')
        self.SearchByMobile_Btn.grid(row = 1,column = 0, ipady=7, pady = 8, sticky = 'EW')
        self.SearchByBrand_Btn.grid(row = 2,column = 0, ipady=7, pady = 8, sticky = 'EW')

        #ExecutionFrame Widgets Placement
        ExecutionFrame.grid(row = 2, column = 0, sticky = 'NS')
        self.StatusofAll.grid(row = 0, column = 0, ipadx = 5 ,sticky="")

        #FooterFrame Widgets Placement
        FooterFrame.grid(row=3, column=0,pady=2, sticky = "S")
        self.LinkedInBtn.grid(row = 0, column = 0,columnspan = 2,ipadx = 0,padx = 12, sticky='')
        self.FacebookBtn.grid(row = 0, column = 1,columnspan = 2,ipadx = 0,padx = 12,sticky='')
        self.GithubBtn.grid(row = 0, column = 2,columnspan = 2,ipadx = 0,padx = 12,sticky='')
        FooterTextL.grid(row = 1, column = 0,columnspan = 2, sticky='')
        FooterTextR.grid(row = 1, column = 2,columnspan = 2, sticky='')

    def fetch_entrybox_values(self):
        '''
        Get the Textbox field value
        :return: (str) -> It will return the text inserted in the Textbox
        '''

        return self.MobileName_ENT.get().strip()

    def clear_entrybox_values(self):
        '''
        Clear the Textbox field value
        :return: none
        '''

        self.MobileName_ENT.delete(0, 'end')


    def fetch_checkboxes_values(self):
        '''
        It will fetch all the checkbox values and return it in a dictionary form
        :return: (dict) -> A single dimensional dictionary that contains checkboxes values
        '''

        BrandsData = {"Apple": self.Apple.get(), "Samsung": self.Samsung.get(), "Huawei": self.Huawei.get(),
                      "Xiaomi": self.Xiaomi.get(), "Nokia": self.Nokia.get(), "Oppo": self.Oppo.get(),
                      "Infinix": self.Infinix.get(), "Tecno": self.Tecno.get(), "Lenovo": self.Lenovo.get(),
                      "Realme":self.Realme.get()}

        return BrandsData

    def resize_image(self,path : str, new_width : int, new_height : int):
        '''
        Open an image file and resize it according to given parameters
        :param path: (str) -> Relative File path where the image is present
        :param new_width: (int) -> New Width after resizing in Whole number i.e in Integers
        :param new_height: (int) -> New Height after resizing in Whole number i.e in Integers
        :return: Image object
        '''
        img = Image.open(path)
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)

    def open_link(self,url : str):
        '''
        Function to open a given URL in the web browser
        :param url: (str) -> The url link to redirect to
        :return: None
        '''
        open(url, new=0)

    def search_by_mobile_frame(self):
        '''
        By Clicking "Search By Mobile" button, it will hide the menu and appear the respective options
        and also the "Back To Menu" Button
        :return: None
        '''

        #OptionMenuFrame Hide and BackToMenu Button Appeared
        self.OptionMenuFrame.grid_forget()
        self.BackToMenu_Btn.grid(row = 1,column = 0,ipady=5,padx=5, sticky = 'NW')

        #SearchByBrandFrame Widgets Placement
        self.SearchByMobileFrame.grid(row = 1, column = 0, sticky = 'N')
        self.MobileText.grid(row = 0, column = 0, columnspan = 2, sticky = 'N', pady = 10)
        self.MobileNameText.grid(row = 1, column = 0, sticky = 'E', pady = 25, padx = 10)
        self.MobileName_ENT.grid(row = 1, column = 1, sticky = 'W', pady = 25, padx = 10)
        self.SearchNExportBtn.grid(row = 1, column = 0, ipadx = 5, ipady=5, sticky='S')

    def search_by_brand_frame(self):
        '''
        By Clicking "Search By Brand" button, it will hide the menu and appear the respective options
        and also the "Back To Menu" Button
        :return: None
        '''

        #OptionMenuFrame Hide and BackToMenu Button Appeared
        self.OptionMenuFrame.grid_forget()
        self.BackToMenu_Btn.grid(row = 1,column = 0,ipady=5,padx=5, sticky = 'NW')

        #SearchByBrandFrame Widgets Placement
        self.SearchByBrandFrame.grid(row = 1, column = 0, sticky = 'N')
        self.BrandsText.grid(row = 0, column = 0, columnspan = 6, sticky = 'N', pady = 10)
        self.Apple.grid(row = 1, column = 1, pady = 9, padx=5)
        self.Samsung.grid(row = 1, column = 2, pady = 9, padx=5)
        self.Huawei.grid(row = 1, column = 3, pady = 9, padx=5)
        self.Xiaomi.grid(row = 1, column = 4, pady = 9, padx=5)
        self.Nokia.grid(row = 1, column = 5, pady = 9, padx=5)
        self.Oppo.grid(row = 2, column = 1, pady = 9, padx=5)
        self.Infinix.grid(row = 2, column = 2, pady = 9, padx=5)
        self.Tecno.grid(row = 2, column = 3, pady = 9, padx=5)
        self.Lenovo.grid(row = 2, column = 4, pady = 9, padx=5)
        self.Realme.grid(row = 2, column = 5, pady = 9, padx=5)
        self.SearchNExportBtn.grid(row = 1, column = 0, ipadx = 5, ipady=5, sticky='S')

    def back_to_menu(self):
        '''
        By Clicking "Back To Menu" Button, it will unhide the Menu frame and Hide the "Back To Menu" Button
        :return: None
        '''

        self.BackToMenu_Btn.grid_forget()
        self.SearchByBrandFrame.grid_forget()
        self.SearchByMobileFrame.grid_forget()
        self.OptionMenuFrame.grid(row = 1, column = 0, sticky='')
        self.SearchNExportBtn.grid_forget()