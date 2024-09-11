from datetime import datetime

from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, query, have


class NewExpense:
    def __init__(self):
        pass
    def open_new_expense(self):
        with step('Create a nex expense'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/fab')).click()
        self.close_notification()

    def close_notification(self):
        with step('Close the notification about button'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/edit_container')).click()

    def click_button_save_and_create(self):
        with step('Click "Save and create"'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/SAVE_AND_NEW_COMMAND')).click()

    def click_button_save_as_template(self):
        with step('Click "Save as template"'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/CREATE_TEMPLATE_COMMAND')).click()

    def enter_title_for_template(self, value):
        with step('Enter a title for a template'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Title')).click()
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Title')).type(value)
            browser.driver.hide_keyboard()

    def set_plan_for_template(self, value):
        with step('Select a plan for the template'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Recurrence')).click()
            browser.all((AppiumBy.ID, 'android:id/text1')).element_by(have.exact_text(value))

    def set_is_that_expense_or_income(self, value):
        temp = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/TaType')).get(query.attribute('content-desc'))
        temp = temp.split()[-1]
        if value != temp:
            with step(f'Set that it is {value}'):
                browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/TaType')).click()

    def enter_amount_of_money(self, value):
        with step('Enter amount of money'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/AmountEditText')).click()
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/AmountEditText')).type(value)
            browser.driver.hide_keyboard()

    def enter_payee_or_payer_name(self, value):
        with step('Enter the name of payee or payer'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Payee')).click().type(value)
            browser.driver.hide_keyboard()

    def enter_notes(self, value):
        with step('Enter notes'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Comment')).click().type(value)
            browser.driver.hide_keyboard()

    def click_button_save_data_and_close_form(self):
        with step('Click button "Save the data and close the form"'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/fab')).click()


    def take_info_about_date_and_time(self):
        date = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/DateButton')).get(query.attribute('text'))
        time = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/TimeButton')).get(query.attribute('text'))
        return datetime.strptime(f'{date} {time}', '%m/%d/%y %I:%M %p')


