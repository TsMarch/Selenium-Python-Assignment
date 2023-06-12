from test_foundation.YandexPages import SearchHelper

def test_yandex_search(browser):
    yandex_pictures_search = SearchHelper(browser)
    yandex_pictures_search.go_to_site()
    yandex_pictures_search.click_on_the_search_button()
    yandex_pictures_search.slide_to_pictures()
    yandex_pictures_search.open_first_category()
    yandex_pictures_search.check_pictures()