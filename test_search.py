from test_foundation.YandexPages import SearchHelper

SEARCH_INPUT = "Тензор"
WANTED_URL = "https://tensor.ru/"

def test_yandex_search(browser):
    yandex_tensor_search = SearchHelper(browser)
    yandex_tensor_search.go_to_site()
    yandex_tensor_search.enter_word(SEARCH_INPUT + "\n")
    yandex_tensor_search.check_urls(WANTED_URL)

  