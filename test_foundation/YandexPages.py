from BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexSeacrhLocators:
    YANDEX_SEARCH_FIELD = (By.ID, "text")
    FIRST_SEARCH_RESULT = (By.XPATH, "/html/body/main/div[2]/div[2]/div/div[1]/ul/li[1]/div/div[1]/a")
    OTHER_ICONS_BTN = (By.CSS_SELECTOR, ".services-suggest__icons-more")
    PICTURES_ICON_BTN = (By.CSS_SELECTOR, "a[aria-label=Картинки]")
    SUGGESTIONS_POPUP = (By. CLASS_NAME, "mini-suggest__popup-content")


class YandexPicturesLocators:
    FIRST_SUGGESTED_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item.PopularRequestList-Item_pos_0")
    INPUT_TEXT = (By.CLASS_NAME, "input__control.mini-suggest__input")
    FIRST_PICTURE = (By.CLASS_NAME, "serp-item.serp-item_pos_0")
    PICTURE_URL_CHECK = (By.CLASS_NAME, "Button2.Button2_size_m.Button2_type_link.Button2_view_action.Button2_width_max.MMViewerButtons-OpenImage")
    PICTURES_NEXT_BTN = (By.CLASS_NAME, "CircleButton.CircleButton_type_next")
    PICTURES_PREV_BTN = (By.CLASS_NAME, "CircleButton.CircleButton_type_prev")
    


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.YANDEX_SEARCH_FIELD)
        assert search_field, "Поле поиска не найдено"
        search_field.click() 
        assert self.find_element(YandexSeacrhLocators.SUGGESTIONS_POPUP), "Таблица с подсказками не появилась"
        search_field.send_keys(word)
       
    
    def click_on_the_search_button(self):
        self.find_element(YandexSeacrhLocators.YANDEX_SEARCH_FIELD).click()

    def slide_to_pictures(self):
        self.find_element(YandexSeacrhLocators.OTHER_ICONS_BTN).click()
        self.find_element(YandexSeacrhLocators.PICTURES_ICON_BTN).click()
        self.switch_window()
        assert self.get_current_url() == 'https://yandex.ru/images/', "URL не совпадает" 
    
    def open_first_category(self):
        self.find_element(YandexPicturesLocators.FIRST_SUGGESTED_CATEGORY).click()
        assert self.find_element(
                    YandexPicturesLocators.FIRST_SUGGESTED_CATEGORY ).get_attribute("data-grid-text") == self.find_element(
                    YandexPicturesLocators.INPUT_TEXT).get_attribute("value"), "Категории ввода и поиска разные"
        

    def check_pictures(self):        
        self.find_element(YandexPicturesLocators.FIRST_PICTURE).click()
        first_check = self.find_element(YandexPicturesLocators.PICTURE_URL_CHECK).get_attribute('href')
        print(first_check)
        self.find_element(YandexPicturesLocators.PICTURES_NEXT_BTN).click()
        second_picture = self.find_element(YandexPicturesLocators.PICTURE_URL_CHECK).get_attribute('href')
        print(second_picture)
        assert second_picture != first_check, "Первая картинка от второй не отличается"
        self.find_element(YandexPicturesLocators.PICTURES_PREV_BTN).click()
        second_check = self.find_element(YandexPicturesLocators.PICTURE_URL_CHECK).get_attribute('href')
        assert first_check == second_check, "Первая картинка изменилась"


    def check_urls(self, url):
        search_result = self.find_element(YandexSeacrhLocators.FIRST_SEARCH_RESULT).get_attribute("href")
        assert search_result == url, "Первая ссылка ведет не на сайт tensor.ru, а на сайт {}".format(search_result)


