from datetime import datetime

from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, query, have

from my_expenses_tests.utils.date_time import date_and_time_in_datetime_form


class NewExpense:
    def __init__(self):
        self.add_smth = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/fab'))
        self.navigate_up = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Navigate up'))

    def open_new_expense(self):
        with step('Create a nex expense'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/fab')).click()

    def close_notification(self):
        with step('Close the notification about button'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/edit_container')).click()

    def click_button_save_and_create(self):
        with step('Click "Save and create"'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/SAVE_AND_NEW_COMMAND')).click()

    def click_button_save_as_template(self):
        with step('Click "Save as template"'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/CREATE_TEMPLATE_COMMAND')).click()

    def set_is_that_expense_or_income(self, value):
        with step(f'Set that it is {value}'):
            temp = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/TaType')).get(query.attribute('content-desc'))
            temp = temp.split()[-1]
            if value != temp:
                    browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/TaType')).click()

    def enter_amount_of_money(self, value):
        with step('Enter amount of money'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/AmountEditText')).click().type(value)

    def enter_payee_or_payer_name(self, value):
        with step('Enter the name of payee or payer'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Payee')).click().type(value)
            # browser.driver.hide_keyboard()

    def enter_notes(self, value):
        with step('Enter notes'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Comment')).click().type(value)

    def click_button_save_data_and_close_form(self):
        with step('Click button "Save the data and close the form"'):
            self.add_smth.click()

    def get_info_about_date_and_time(self):
        with step('Get information about date and time of the expense'):
            date = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/DateButton')).get(query.attribute('text'))
            time = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/TimeButton')).get(query.attribute('text'))
            return date_and_time_in_datetime_form(date, time)

    def add_tag(self, value):
        with step('Add a tag'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/TagSelection')).click()
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/tag_edit')).click().type(value)
            self.add_smth.click()

    def click_button_close_expense_form(self):
        with step('Close the expense form'):
            self.navigate_up.click()
