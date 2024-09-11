from datetime import date, datetime
from typing import Union

from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have, query


class MainPage:
    def __init__(self):
        self.toolbar = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/toolbar'))
        self.accountList = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/accountList'))
        self.expenses = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/viewPager'))

    def should_have_icons_and_specific_text(self, name):
        with step('Check the main page'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/MANAGE_TEMPLATES_COMMAND')).should(be.visible)
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/BUDGET_COMMAND')).should(be.visible)
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/fab')).should(be.visible)
            browser.element(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Open navigation drawer")')).should(
                be.visible)
            self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).first.should(have.exact_text(name))

    def should_have_specific_text_after_all_setting_on_start_pages(self, name, money, currency, description,
                                                                   account_type):
        with step('Check all specific options in the main menu after the third start page settings'):
            self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).first.should(have.exact_text(name))
            self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).second.should(have.text(money))
            self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).second.should(have.text(currency))

            self.toolbar.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton')).click()

            self.accountList.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text({name}).instance(1)'))
            self.accountList.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text({account_type})'))
            self.accountList.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text({description})'))

    def should_have_specific_text_in_the_expense_form_on_main_page(self, money: int, payee: str, notes: str,
                                                                    expense_datetime: Union[None | datetime]):
        money = f'{float(money):,.02f}'
        expense_date = expense_datetime.date().strftime('%b %d, %Y').split()
        expense_date[1] = expense_datetime[1][1:] if expense_date[1][0] == '0' else expense_date[1]
        expense_date = ' '.join(expense_date)


        self.expenses.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{notes} / {payee}")')).should(have.exact_text(f'{notes} / {payee}'))
        # self.expenses.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("${money}").instance(1)')).should(have.text(f'${money}'))
        self.expenses.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("${money}").instance(1)')).get(query.attribute('text'))
        self.expenses.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{expense_date}")')).should(have.exact_text(expense_date))

        self.expenses.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("${money}")')).should(have.exact_text(f'${money}'))

    def should_have_specific_text_in_details_menu(self, money: int, payee: str, notes: str,
                                                      expense_datetime: Union[None | datetime]):
        with step('Check the specific text in the detail menu for the expense'):
            money = f'{float(money):,.02f}'
            expense_datetime = expense_datetime.strftime('%A, %B %d, %Y %I:%M %p').split()
            expense_datetime[2] = expense_datetime[2][1:] if expense_datetime[2][0] == '0' else expense_datetime[2]
            expense_datetime[4] = expense_datetime[4][1:] if expense_datetime[4][0] == '0' else expense_datetime[2]
            expense_datetime = ' '.join(expense_datetime)

            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Date')).should(have.exact_text(expense_datetime))
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Amount')).should(have.exact_text(f'${money}'))
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Comment')).should(have.exact_text(notes))
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Payee')).should(have.exact_text(payee))

    def open_details_menu_for_last_expense(self):
        with step('Open details menu for the last expense'):
            self.expenses.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(3)')).click()
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Details")')).click()

    def take_current_amount_of_money(self):
        money = self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).second.get(query.attribute('text'))
        return money

    def should_have_the_same_total_amount_of_money(self, value):
        with step('Check total amount of money'):
            self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).second.should(have.text(value))

    def delete_last_expence(self):
        with step('Delete the last expense'):
            self.expenses.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(3)')).click()
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Delete")')).click()
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/buttonPanel')).element((AppiumBy.ID, 'android:id/button1')).click()


