from category import Category
from connectrequests import NewConnect
from infotable import Table



class Investing:

    def __init__(self):
        self.__category = Category()
        self.__newconnect = NewConnect()
        self.__html_page = None

    

    def set_html_page(self,html_page=None):
        if html_page:
            self.__html_page = html_page


    def get_info(self):
        data_json = self.__category.get_category(self.__html_page)
        for cat in data_json:
            print(cat)
        categorys = input('Enter Category: ')
        if categorys in data_json:
            for cat in data_json[categorys]:
                print(cat)
            subcategories = input('Enter subcategory: ')
            if subcategories in data_json[categorys]:
                urls = data_json[categorys][subcategories]
                new_source = self.__newconnect.connect(urls)
                if new_source:
                    body_table = Table(new_source)
                    body_table.info_tables()
                else:
                    print('error')

    def get_info1(self, category, subcategory):
        data_json = self.__category.get_category(self.__html_page)
        urls = data_json[category][subcategory]
        new_source = self.__newconnect.connect(urls)
        body_table = Table(new_source)
        return body_table.info_tables()


