import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalcPage import CalcPage


@allure.severity("critical")
@allure.title("Результат вычисления")
def test_data_calc():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()))

    calc_page = CalcPage(driver)
    calc_page.open_pages()
    calc_page.delay()
    calc_page.data_entry()
    calc_page.get_result()
    calc_page.close_driver()
