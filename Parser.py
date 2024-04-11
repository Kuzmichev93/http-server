from bs4 import BeautifulSoup
import requests as rq

class Parser():


    def get_page(self):
        url = 'https://ru.wikipedia.org/wiki/EBCDIC'
        req = rq.get(url).text
        return req

    def parsers(self,arg=None):
        soap = BeautifulSoup(self.get_page(),'html.parser')
        b = soap.find_all('table')[0]
        b1 = b.find_all('tr')[0].text.split('\n')
        b2 = b.find_all('tr')
        A={}
        i=0
        for z in range(1,len(b2)-1):
            #print(b2[z].find_all('th')[0].text)
            i=0
            for k in range(len(b1)):
                if len(b1[k])==2 and i<=len(b2)-2:
                    l=b2[z].find_all('th')[0].text
                    p=l+b1[k]
                    d=p.rstrip('\n').replace('.','')
                    A.setdefault(d.replace('\n',''),b2[z].find_all('td')[i].text.replace('\n',''))
                    i+=1

        return A

    def rec(self,A,array,n):
        """рекурсивный поиск в массиве"""
        if n == 0:
            return A
        A+=self.get_array[array[self.len_n-n].replace('.','')]
        return self.rec(A,array,n-1)


    def get_respons(self,array):
        A = ''
        self.len_n = len(array)
        self.get_array = self.parsers()
        value = self.rec(A,array,self.len_n)
        return value



