from datetime import date

from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, command


class StartPages:
    def __init__(self):
        self.font_size = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/font_size'))
        self.all_options = browser.all((AppiumBy.ID, 'android:id/text1'))

    def set_theme(self, value):
        with step('Set a theme'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/themeSpinner')).click()
            self.all_options.element_by(have.exact_text(value)).click()

    def check_page_theme(self, value):
        with step('Check the page theme'):
            browser.element((AppiumBy.ID, 'android:id/text1')).should(have.exact_text(value))

    def change_font_size(self, x: int, y: int):
        with step('Change font size'):
            self.font_size.perform(command.drag_and_drop_by_offset(x, y))

    def check_font_size(self, value):
        with step('Check the page font size'):
            self.font_size.should(have.exact_text(str(float(value))))
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/font_size_display_name')).should(
                have.exact_text(f'System default + {value * 10}%'))

    def make_display_form_compact(self, value: bool):
        if value:
            with step('Make the display form compact'):
                browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().className("android.widget.CheckBox").instance(0)')).click()

    def check_display_form(self):
        with step('Check the display form'):
            temp = date.today()
            temp = f'{temp.month}/{temp.day}/{temp.year % 100}'
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{temp}")')).should(
                have.exact_text(temp))

    def should_have_specific_settings_on_first_page(self, theme, font_size, compact):
        with step('Check the first page settings'):
            self.check_page_theme(theme)
            self.check_font_size(font_size)
            if compact:
                self.check_display_form()

    def open_next_page(self):
        with step('Open next page'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/suw_navbar_next')).with_(timeout=15).click()

    def click_get_started(self):
        with step('Click \'Get started\''):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/suw_navbar_done')).click()

    def should_have_specific_title(self, text, page=0):
        with step(f'Check the text {'on the ' * bool(page) + str(page) + ' page' * bool(page)}'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/suw_layout_title')).should(
                have.exact_text(text))

    def turn_on_backup_database_at_the_specified_time(self, value):
        with step('Turn on backup database at the specific time'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/auto_backup')).click()
            if not value:
                browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')).click()

    def create_label_for_budget_book(self, value):
        with step('Create a label for a new budget book'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Label')).click().type(value)

    def set_opening_balance(self, value):
        with step('Set an opening balance value'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/AmountEditText')).click().type(str(value))

    def open_more_options_on_third_page(self):
        with step('Open more options on the third page'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/MoreOptionsButton')).click()

    def enter_description(self, value):
        with step('Create a description for a new budget boook'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/Description')).click().type(value)

    def set_budget_book_type(self, value):
        with step('Set a budget book type'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/AccountType')).click()
            self.all_options.element_by(have.exact_text(value)).click()

    def skip_all_start_pages(self):
        with step('Skip all start pages to open the main page'):
            self.open_next_page()
            self.open_next_page()
            self.click_get_started()
