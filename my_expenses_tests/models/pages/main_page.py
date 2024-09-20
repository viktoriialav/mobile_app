from datetime import datetime

from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have

from my_expenses_tests.utils.date_time import datetime_long_format, date_middle_format
from my_expenses_tests.utils.money import int_to_str


class MainPage:
    def __init__(self):
        self.toolbar = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/toolbar'))
        self.accountList = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/accountList'))
        self.expenses = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/viewPager'))
        self.template_menu_button = browser.element((AppiumBy.ID,
                                                     'org.totschnig.myexpenses:id/MANAGE_TEMPLATES_COMMAND'))

        self.last_expense = self.expenses.element((AppiumBy.ANDROID_UIAUTOMATOR,
                                                   'new UiSelector().className("android.view.View").instance(3)'))
        self.total_sum = self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).second
        self.total_sum = self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).second
        self.manage_accounts_button = self.toolbar.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton'))

    def close_notification(self):
        with step('Close the notification about button'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/viewPager')).click()

    def should_have_specific_text(self):
        with step('Check the specific text on the main page'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/viewPager')).element(
                (AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.exact_text('No Expenses Yet!'))

    def should_have_icons_and_specific_text(self, name):
        with step('Check the main page'):
            self.template_menu_button.should(be.visible)
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/BUDGET_COMMAND')).should(be.visible)
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/fab')).should(be.visible)
            self.manage_accounts_button.should(be.visible)
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'More options')).should(be.visible)
            self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).first.should(have.exact_text(name))

    def should_have_specific_text_after_all_setting_on_start_pages(self, name, money, description, account_type):
        with step('Check all specific options in the main menu after the third start page settings'):
            self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).first.should(have.exact_text(name))
            self.total_sum.should(have.text(int_to_str(money)))

            self.manage_accounts_button.click()

            self.accountList.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text({name}).instance(1)'))
            self.accountList.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text({account_type})'))
            self.accountList.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text({description})'))

    def should_have_specific_text_in_details_menu(self, money: int, expense_datetime: datetime,
                                                  payee: str, notes: str, tags: list[str]):
        with (step('Check the specific text in the detail menu for the expense')):
            expense_datetime = datetime_long_format(expense_datetime)
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Date')).should(have.exact_text(expense_datetime))

            money = int_to_str(money)
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Amount')).should(have.text(f'{money}'))

            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Comment')).should(have.exact_text(notes))
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Payee')).should(have.exact_text(payee))
            for i, tag in enumerate(tags):
                browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/TagGroup')).all(
                    (AppiumBy.CLASS_NAME, 'android.widget.Button'))[i].should(have.exact_text(tag))

    def open_details_menu_for_last_expense(self):
        with step('Open details menu for the last expense'):
            self.last_expense.click()
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Details")')).click()

    def should_have_specific_total_sum(self, value):
        with step('Check total sum'):
            self.total_sum.should(have.text(int_to_str(value)))

    def delete_last_expence(self):
        with step('Delete the last expense'):
            self.last_expense.click()
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Delete")')).click()
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/buttonPanel')).element(
                (AppiumBy.ID, 'android:id/button1')).click()

    def should_be_on_the_main_page(self):
        with step('Check the expense on the main page'):
            self.last_expense.should(be.visible)

    def should_have_specific_number_of_expenses(self, number: int, expense_datetime: datetime):
        with step('Check the number of expenses'):
            expense_date = date_middle_format(expense_datetime)
            browser.all((AppiumBy.XPATH, f'(//android.widget.TextView[@text="{expense_date}"])')).should(
                have.size(number))

    def should_have_specific_number_of_expenses_with_equal_notes_and_payer(self, number, payee, notes):
        with step('Check the number of expenses with equal notes and payee/payer'):
            browser.all((AppiumBy.XPATH, f'(//android.widget.TextView[@text="{notes} / {payee}"])')).should(
                have.size(number))
