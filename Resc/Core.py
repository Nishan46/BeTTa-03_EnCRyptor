from Resc import Crypts as Cryptor
from rich.progress import track
from time import sleep

class ENCRYPT:

    def __init__(self,text):
        self.text = text
        self.__index = None
        self.__Binary_String = ""
        self.__Decimal_List = [64,32,16,8,4,2,1]
        self.__Finaly = ""
        self.__symbols = Cryptor.Get()
        self.__symbols_length = (len(self.__symbols) - 1)

    def __str__(self):
        result = f'\n\nHey...\nI am from encrypt class. I think you got what you want now.\nSo... Have a nice day ... !\n\nYour Text = {self.text}\n\nYour Key -->\n{self.__Finaly} '
        return result

    def Get_Code(self,key):
        Codes = (self.__symbols_length - key)
        return Codes

    def Encript(self):       
        self.__Finaly = ''
        for steps in track(range((len(self.text))), description="[green bold]Encrypting ..."):
            self.__index = ENCRYPT.Get_Code(self,self.__symbols.index(self.text[steps]))
            self.__Finaly += ENCRYPT.Get_Binary(self)                   
        return self.__Finaly

    def Get_Binary(self):
        self.__Binary_String = ""
        for count in range(0,len(self.__Decimal_List)):
            if self.__index >= self.__Decimal_List[count]:
                self.__Binary_String +="1"
                self.__index = self.__index - self.__Decimal_List[count]
            else:
                self.__Binary_String +="0"
        return self.__Binary_String







# def Decrypt(Texts):
#     key = ''
#     for items in Texts:
#         Code = symbols[DecryptCode(symbols.index(items),symbols_length)]
#         sleep(0.1)
#         key += Code
#     return key