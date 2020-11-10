from selenium import webdriver
import time


class RemoveItems:
    def __init__(self, login, password):
        self.bot = webdriver.Firefox()
        self.login = login
        self.password = password

    def account_login(self):
        self.bot.get("https://steamcommunity.com/market/")
        time.sleep(1)
        self.bot.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[1]/div/div[3]/div/a').click()
        self.bot.find_element_by_xpath(
            '//*[@id="input_username"]').send_keys(self.login)
        self.bot.find_element_by_xpath(
            '//*[@id="input_password"]').send_keys(self.password)
        self.bot.find_element_by_xpath(
            '/html/body/div[1]/div[7]/div[2]/div[1]/div/div[1]/div/div/div/div/div[3]/div[1]/button').click()

        try:
            guard = self.bot.find_element_by_xpath(
                '//*[@id="twofactorcode_entry"]')
            if guard:
                time.sleep(1)
                code = input("Podaj kod: ").upper()
                guard.send_keys(code)
                time.sleep(1)
                self.bot.find_element_by_xpath(
                    '/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]').click()
                time.sleep(5)
        except:
            pass

    def increase_list(self):
        self.bot.find_element_by_xpath(
            '//*[@id="my_listing_pagesize_100"]').click()
        time.sleep(2)

    def remove_item(self):
        items_list = [
            "Wzmocniona robo-pompa tłumienia emocji",
            "Wzmocniony robo-stabilizator bomby",
            "Nietknięta robo-żarówka olśnienia",
            "Wzmocniony robo-wykrywaczNietknięty robo-przetrawiacz pieniędzy",
            "Podniszczony robo-analizator drwin",
            "Podniszczony Robo-KB-808",
            "Podniszczony robo-piec na pieniądze"]

        item_row = self.bot.find_elements_by_class_name(
            'market_recent_listing_row')
        for x in range(0, len(item_row)):
            if item_row[x].is_displayed():
                item_name_qs = item_row[x].find_elements_by_class_name(
                    'market_listing_item_name_link')
                item_remove_qs = item_row[x].find_elements_by_class_name(
                    'item_market_action_button_edit')
                for item_name in item_name_qs:
                    if item_name.text in items_list:
                        for a in item_remove_qs:
                            a.click()
                            self.bot.find_element_by_xpath(
                                '//*[@id="market_removelisting_dialog_accept"]').click()
                            time.sleep(5)


data = RemoveItems("username", "password")
data.account_login()
data.increase_list()
data.remove_item()
