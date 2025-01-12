import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.ShopPage import ShopPage


@allure.severity("blocker")
@allure.title("Покупка в магазине")
@allure.description("Товары в корзине")
def test_data_shop():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    shop_page = ShopPage(driver)
    shop_page.open_pages()
    shop_page.authorization()
    shop_page.click_submit()
    shop_page.add_product()
    shop_page.go_to_cart()
    shop_page.checkout()
    shop_page.data_entry()
    shop_page.continue_click()
    shop_page.get_total()
    shop_page.click_finish()
    shop_page.close_driver()