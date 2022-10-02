import lxml
from bs4 import BeautifulSoup as bs
from create_json import CreateJson

# Класс по парсингу таблиц из сайта
#genTbl closedTbl crossRatesTbl
#genTbl closedTbl crossRatesTbl elpTbl elp20

class Table:
    def __init__(self,source):
        self.soup = bs(source,'lxml')
        self.soup_body = None
        self.list_table = None
        self.inform = False
        self.not_table = None
        self.create_json = CreateJson()

#Проверка наличии таблицы

    def check_body_table(self):
        self.list_table = self.soup_body.select("table.genTbl")
        self.not_table = self.soup_body.find('div',{'class':'fullHeaderTwoColumnPage--top'})
        if self.not_table:
            self.inform = True
        else:
            self.inform = False
            
        
# Поиск елементов в разных блоках

    def find_table(self):
        if self.soup.main:
            self.soup_body = self.soup.main
            self.check_body_table()
        elif self.soup.section:
            self.soup_body = self.soup.section
            self.check_body_table()
            
#Функция поиска если не таблица

    def find_not_table(self):
        list_title = self.soup_body.find('h1').text.replace("\t", "")
        information = self.soup_body.find('div',{'class':'fullHeaderTwoColumnPage--top'}).select_one('div.top.bold.inlineblock').select('span')
        table = {list_title: [information[1].text, information[2].text, information[4].text]}
        self.create_json.create(table)
        self.create_json.print_no_table()



#Функция вывода если таблица

    def output_info_table(self,list_title):
        table = {}
        if len(list_title) == len(self.list_table):
            for i in range(len(list_title)):
                title = list_title[i].text
                if title not in table.keys():
                    table[title] = {}
                list_tag_td = self.list_table[i].find_all('td')
                tbl = [tag_td.text.strip() for tag_td in list_tag_td]
                for j in range(len(tbl)):
                    if j % 10 == 1:
                        table[title][tbl[j]] = tbl[j + 1:j + 8]

        self.create_json.create(table)
        self.create_json.print_table()
#Вывод информации с сайта

    def info_tables(self):
        self.find_table()
        if self.inform:
            self.find_not_table()
        else:
            if len(self.list_table)>1:
                list_title = self.soup_body.find_all('h2')
                self.output_info_table(list_title)
            elif len(self.list_table) == 1:
                list_title = self.soup_body.find_all('h1')
                self.output_info_table(list_title)



