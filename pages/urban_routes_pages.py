import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]')
    phone_number_button = (By.CSS_SELECTOR, ".np-button")
    phone_number_input = (By.ID, 'phone')
    next_button = (By.CSS_SELECTOR, ".button.full")
    confirm_field = (By.CSS_SELECTOR, ".input-container")
    confirm_button = (By.XPATH, '//button[@type="submit" and normalize-space()="Confirmar"]')
    phone_code_field = (By.ID, "code")
    payment_method = (By.CSS_SELECTOR, ".pp-button.filled")
    add_card = (By.CSS_SELECTOR, '.pp-row.disabled')
    add_card_number_field = (By.ID, 'number')
    add_code_field = (By.ID, 'code')
    confirm_card_button = (By.XPATH, '//button[@type="submit" and normalize-space()="Agregar"]')
    close_button = (By.CSS_SELECTOR, 'button.close-button.section-close')
    payment_method_value = (By.CSS_SELECTOR, ".pp-value-text")
    comment_field = (By.ID, 'comment')
    blanket_switch = (By.XPATH,'//div[contains(@class,"r-sw-container")][.//div[contains(text(),"Manta y pañuelos")]]//span[contains(@class,"slider")]')
    blanket_checkbox = (By.XPATH,'//div[contains(@class,"r-sw-container")][.//div[contains(text(),"Manta y pañuelos")]]//input[@type="checkbox"]')
    ice_cream_plus = (By.CSS_SELECTOR, ".counter-plus")
    ice_cream_value = (By.CSS_SELECTOR, ".counter-value")
    request_taxi_final_button = (By.XPATH,'//button[@type="button" and .//span[contains(text(),"Introducir un número de teléfono y reservar")]]')
    searching_car_title = (By.CSS_SELECTOR,".order-header-title")
    searching_car_time = (By.CSS_SELECTOR,".order-header-time")
    car_number = (By.CSS_SELECTOR,".order-number .number")



    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.request_taxi_button)
        )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()


    def get_comfort_icon(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.comfort_icon)
        )

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_comfort_icon_assert(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.comfort_icon_assert)
        )

    def get_phone_number_button(self):
        return WebDriverWait(self.driver, 5).until(
        expected_conditions.element_to_be_clickable(self.phone_number_button)
        )

    def click_on_phone_number_button(self):
        self.get_phone_number_button().click()

    def get_phone_number_input(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.phone_number_input)
        )

    def set_phone_number_input(self, phone_number):
        self.get_phone_number_input().send_keys(phone_number)

    def get_next_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.next_button)
        )

    def click_next_button(self):
        self.get_next_button().click()

    def get_confirm_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.confirm_field)
        )

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.confirm_button)
        )

    def click_confirm_button(self):
        self.get_confirm_button().click()

    def get_phone_code_field(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.phone_code_field
            )
        )

    def set_phone_code_field(self, code):
        self.get_phone_code_field().send_keys(code)

    def get_payment_method(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.payment_method)
        )

    def click_payment_method(self):
        self.get_payment_method().click()

    def get_add_card(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.add_card)
        )

    def click_add_card(self):
        self.get_add_card().click()

    def get_add_card_number_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.add_card_number_field)
        )

    def set_add_card_number_field(self, card_number):
        card_number_field = self.get_add_card_number_field()
        card_number_field.send_keys(card_number)
        card_number_field.send_keys(Keys.TAB)

    def get_add_code_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.add_code_field)
        )

    def set_add_code_field(self, card_code):
        self.driver.switch_to.active_element.send_keys(card_code)
        self.driver.switch_to.active_element.send_keys(Keys.TAB)


    def get_confirm_card_button(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(self.confirm_card_button)
        )

    def click_confirm_card_button(self):
        self.get_confirm_card_button().click()

    def get_close_button(self):
        def visible_close_button(driver):
            buttons = driver.find_elements(*self.close_button)

            for button in buttons:
                if button.is_displayed() and button.is_enabled():
                    return button

            return False

        return WebDriverWait(self.driver, 5).until(
            visible_close_button
        )

    def click_close_button(self):
        self.get_close_button().click()

    def get_payment_method_value(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                self.payment_method_value
            )
        )

    def get_payment_method_text(self):
        return self.get_payment_method_value().text

    def get_comment_field(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                self.comment_field
            )
        )

    def set_comment(self, comment):
        self.get_comment_field().send_keys(comment)

    def get_comment(self):
        return self.get_comment_field().get_attribute("value")

    def get_blanket_switch(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.blanket_switch
            )
        )

    def click_blanket_switch(self):
        self.get_blanket_switch().click()

    def get_blanket_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                self.blanket_checkbox
            )
        )

    def is_blanket_selected(self):
        return self.get_blanket_checkbox().is_selected()

    def get_ice_cream_plus(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(
                self.ice_cream_plus
            )
        )

    def click_ice_cream_plus(self):
        self.get_ice_cream_plus().click()

    def get_ice_cream_value(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                self.ice_cream_value
            )
        )

    def get_request_taxi_final_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.request_taxi_final_button
            )
        )

    def click_request_taxi_final_button(self):
        self.get_request_taxi_final_button().click()

    def get_searching_car_title(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.searching_car_title
            )
        )

    def get_searching_car_time(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                self.searching_car_time
            )
        )

    def get_car_number(self):
        return WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located(
                self.car_number
            )
        )