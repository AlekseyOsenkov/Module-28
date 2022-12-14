# страница пользовательского профиля
from selenium.webdriver.common.by import By
from Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_css_selector = Locators.welcome_css_selector
        self.click_my_tabs_css_selector = Locators.click_my_tabs_css_selector
        self.my_tabs_link_text = Locators.my_tabs_link_text
        self.my_orders_link_text = Locators.my_orders_link_text
        self.my_profile_link_text = Locators.my_profile_link_text
        self.contact_info_link_text = Locators.contact_link_text
        self.delivery_info_link_text = Locators.delivery_info_link_text
        self.other_info_link_text = Locators.other_info_link_text
        self.change_password_link_text = Locators.change_password_link_text
        self.new_password_class_name = Locators.new_password_class_name
        self.confirmation_new_password_class_name = Locators.confirmation_new_password_class_name
        self.old_password_class_name = Locators.old_password_class_name
        self.exit_link_text = Locators.exit_link_text
        self.basket_id = Locators.basket_id
        self.catalog_products_class_name = Locators.catalog_products_class_name
        self.new_products_xpath = Locators.new_products_xpath
        self.sale_xpath = Locators.sale_xpath
        self.discounts_and_bonuses_xpath = Locators.discounts_and_bonuses_xpath
        self.payment_and_delivery_xpath = Locators.payment_and_delivery_xpath
        self.hurry_up_xpath = Locators.hurry_up_xpath
        self.contacts_xpath = Locators.contacts_xpath
        self.airsoft_guns_xpath = Locators.airsoft_guns_xpath
        self.all_guns_xpath = Locators.all_guns_xpath
        self.pyrotechnics_xpath = Locators.pyrotechnics_xpath
        self.all_guns_xpath_2 = Locators.all_guns_xpath_2
        self.link_vk_xpath = Locators.link_vk_xpath
        self.link_facebook_xpath = Locators.link_facebook_xpath
        self.link_twitter_xpath = Locators.link_twitter_xpath
        self.link_instagram_xpath = Locators.link_instagram_xpath
        self.link_youtube_xpath = Locators.link_youtube_xpath
        self.link_telegram_bot_xpath = Locators.link_telegram_bot_xpath
        self.email_us_css_selector = Locators.email_us_css_selector
        self.close_the_form_css_selector = Locators.close_the_form_css_selector
        self.articles_xpath = Locators.articles_xpath
        self.top_logo_css_selector = Locators.top_logo_css_selector
        self.button_buy_vint1_xpath = Locators.button_buy_vint1_xpath

    def check_welcome_message(self):
        msg = self.driver.find_element(By.CSS_SELECTOR, self.welcome_css_selector).text
        return msg

    def click_my_tabs(self):
        self.driver.find_element(By.LINK_TEXT, self.my_tabs_link_text).click()

    def click_my_orders(self):
        self.driver.find_element(By.LINK_TEXT, self.my_orders_link_text).click()

    def click_my_profile(self):
        self.driver.find_element(By.LINK_TEXT, self.my_profile_link_text).click()

    def contact_info_message(self):
        msg_8 = self.driver.find_element(By.LINK_TEXT, self.contact_info_link_text).text
        return msg_8

    def delivery_info_message(self):
        msg_9 = self.driver.find_element(By.LINK_TEXT, self.delivery_info_link_text).text
        return msg_9

    def other_info_message(self):
        msg_10 = self.driver.find_element(By.LINK_TEXT, self.other_info_link_text).text
        return msg_10

    def click_change_password(self):
        self.driver.find_element(By.LINK_TEXT, self.change_password_link_text).click()

    def new_password_value(self):
        self.driver.find_element(By.CLASS_NAME, self.new_password_class_name).clear()
        self.driver.find_element(By.CLASS_NAME, self.new_password_class_name)

    def confirmation_new_password_value(self):
        self.driver.find_element(By.CLASS_NAME, self.confirmation_new_password_class_name).clear()
        self.driver.find_element(By.CLASS_NAME, self.confirmation_new_password_class_name)

    def old_password_value(self):
        self.driver.find_element(By.CLASS_NAME, self.old_password_class_name).clear()
        self.driver.find_element(By.CLASS_NAME, self.old_password_class_name)

    def click_exit(self):
        self.driver.find_element(By.LINK_TEXT, self.exit_link_text).click()

    def click_basket(self):
        self.driver.find_element(By.ID, self.basket_id).click()

    def click_catalog_products(self):
        self.driver.find_element(By.CLASS_NAME, self.catalog_products_class_name).click()

    def click_new_products(self):
        self.driver.find_element(By.XPATH, self.new_products_xpath).click()

    def click_sale(self):
        self.driver.find_element(By.XPATH, self.sale_xpath).click()

    def click_discounts_and_bonuses(self):
        self.driver.find_element(By.XPATH, self.discounts_and_bonuses_xpath).click()

    def click_payment_and_delivery(self):
        self.driver.find_element(By.XPATH, self.payment_and_delivery_xpath).click()

    def click_hurry_up(self):
        self.driver.find_element(By.XPATH, self.hurry_up_xpath).click()

    def click_contacts(self):
        self.driver.find_element(By.XPATH, self.contacts_xpath).click()

    def click_airsoft_guns(self):
        self.driver.find_element(By.XPATH, self.airsoft_guns_xpath).click()

    def click_all_guns(self):
        self.driver.find_element(By.LINK_TEXT, self.all_guns_xpath).click()

    def click_pyrotechnics(self):
        self.driver.find_element(By.XPATH, self.pyrotechnics_xpath).click()

    def click_all_guns_2(self):
        self.driver.find_element(By.XPATH, self.all_guns_xpath_2).click()

    def click_link_vk(self):
        self.driver.find_element(By.XPATH, self.link_vk_xpath).click()

    def click_link_facebook(self):
        self.driver.find_element(By.XPATH, self.link_facebook_xpath).click()

    def click_link_twitter(self):
        self.driver.find_element(By.XPATH, self.link_twitter_xpath).click()

    def click_link_instagram(self):
        self.driver.find_element(By.XPATH, self.link_instagram_xpath).click()

    def click_link_youtube(self):
        self.driver.find_element(By.XPATH, self.link_youtube_xpath).click()

    def click_link_telegram_bot(self):
        self.driver.find_element(By.XPATH, self.link_telegram_bot_xpath).click()

    def click_email_us(self):
        self.driver.find_element(By.CSS_SELECTOR, self.email_us_css_selector).click()

    def click_close_the_form(self):
        self.driver.find_element(By.CSS_SELECTOR, self.close_the_form_css_selector).click()

    def click_articles(self):
        self.driver.find_element(By.XPATH, self.articles_xpath).click()

    def click_top_logo(self):
        self.driver.find_element(By.CSS_SELECTOR, self.top_logo_css_selector).click()

    def click_button_buy_vint1(self):
        self.driver.find_element(By.XPATH, self.button_buy_vint1_xpath).click()