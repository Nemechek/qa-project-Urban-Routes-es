from data import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_pages import UrbanRoutesPage
from helpers.retrive_code import retrieve_phone_code


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs",{'performance':'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_pages = UrbanRoutesPage(cls.driver)


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_pages = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_pages.set_route(address_from, address_to)
        assert routes_pages.get_from() == address_from
        assert routes_pages.get_to() == address_to


    def test_select_comfort_tariff(self):
        self.driver.get(data.urban_routes_url)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(
            data.address_from,
            data.address_to,
        )
        routes_pages.click_request_taxi_button()
        routes_pages.click_comfort_icon()
        comfort_tariff = routes_pages.get_comfort_icon_assert().text
        assert comfort_tariff == "Manta y pañuelos"


    def test_add_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(
            data.address_from,
            data.address_to,
        )
        routes_pages.click_request_taxi_button()
        routes_pages.click_on_phone_number_button()
        routes_pages.set_phone_number_input(data.phone_number)
        routes_pages.click_next_button()
        phone_code = retrieve_phone_code(self.driver)
        routes_pages.set_phone_code_field(phone_code)
        routes_pages.click_confirm_button()



    def test_add_payment_method(self):
        self.driver.get(data.urban_routes_url)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(
            data.address_from,
            data.address_to,
        )
        routes_pages.click_request_taxi_button()
        routes_pages.click_comfort_icon()
        routes_pages.click_payment_method()
        routes_pages.click_add_card()
        routes_pages.set_add_card_number_field(data.card_number)
        routes_pages.set_add_code_field(data.card_code)
        routes_pages.click_confirm_card_button()

        routes_pages.click_close_button()

        payment_method = routes_pages.get_payment_method_text()

        assert payment_method == "Tarjeta"

    def test_driver_comment(self):
        self.driver.get(data.urban_routes_url)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(
            data.address_from,
            data.address_to,
        )
        routes_pages.click_request_taxi_button()
        routes_pages.click_comfort_icon()
        routes_pages.set_comment(data.driver_comment)

        assert routes_pages.get_comment() == data.driver_comment

    def test_blanket_and_scarf(self):
        self.driver.get(data.urban_routes_url)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(
            data.address_from,
            data.address_to,
        )
        routes_pages.click_request_taxi_button()
        routes_pages.click_comfort_icon()
        routes_pages.click_blanket_switch()

        assert routes_pages.is_blanket_selected()

    def test_add_ice_cream(self):
        self.driver.get(data.urban_routes_url)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(
            data.address_from,
            data.address_to,
        )
        routes_pages.click_request_taxi_button()
        routes_pages.click_comfort_icon()
        routes_pages.click_ice_cream_plus()
        routes_pages.click_ice_cream_plus()

        ice_cream_value = routes_pages.get_ice_cream_value().text

        assert ice_cream_value == "2"

    def test_request_taxi(self):
        self.driver.get(data.urban_routes_url)
        routes_pages = UrbanRoutesPage(self.driver)
        routes_pages.set_route(
            data.address_from,
            data.address_to,
        )
        routes_pages.click_request_taxi_button()
        routes_pages.click_request_taxi_final_button()

        assert routes_pages.get_searching_car_title().text == "Buscar automóvil"
        car_number = routes_pages.get_car_number().text
        assert car_number != ""




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()