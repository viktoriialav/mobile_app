from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, command


class StartPages:
    def __init__(self):
        self.font_size = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/font_size'))

    def set_theme(self, value):
        with step('Set a theme'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/themeSpinner')).click()
            browser.all((AppiumBy.ID, 'android:id/text1')).element_by(have.exact_text(value)).click()

    def check_page_theme(self, value):
        with step('Check the page theme'):
            browser.element((AppiumBy.ID, 'android:id/text1')).should(have.exact_text(value))

    def change_font_size(self, x: int, y: int):
        with step('Change font size'):
            self.font_size.perform(command.drag_and_drop_by_offset(x, y))

    def check_font_size(self, value):
        with step('Check a page font size'):
            self.font_size.should(have.exact_text(str(float(value))))
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/font_size_display_name')).should(
                have.exact_text(f'System default + {value * 10}%'))

    def make_display_form_compact(self, value: bool):
        if value:
            with step('Make the display form compact'):
                browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                                 'new UiSelector().className("android.widget.CheckBox").instance(0)')).click()

    # def check_display_form(self):
    #     with step('Check display form'):
    #         browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/design_preview')).element((
    #             AppiumBy.ANDROID_UIAUTOMATOR,
    #             'new UiSelector().className("android.view.View").instance(0)')).element((
    #             AppiumBy.ANDROID_UIAUTOMATOR,
    #             'new UiSelector().className("android.view.View").instance(0)')).should(
    #             have.exact_text('9/9/24'))

    def should_have_special_settings_on_first_page(self, theme, font_size, compact):
        self.check_page_theme(theme)
        self.check_font_size(font_size)
        # if compact:
        #     self.check_display_form()

    def open_next_page(self):
        with step('Open next page'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/suw_navbar_next')).click()

    def click_get_started(self):
        with step('Click \'Get started\''):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/suw_navbar_done')).click()

    def should_have_special_text(self, text, page=0):
        with step(f'Check the text {'on the ' * bool(page) + str(page) + ' page' * bool(page)}'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/suw_layout_title')).should(
                have.exact_text(text))
