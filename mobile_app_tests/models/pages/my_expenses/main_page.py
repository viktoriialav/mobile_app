from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have


class MainPage:
    def should_have_icons_and_special_text(self):
        with step('Check the main page'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/MANAGE_TEMPLATES_COMMAND')).should(be.visible)
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/BUDGET_COMMAND')).should(be.visible)
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/fab')).should(be.visible)
            browser.element(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Open navigation drawer")')).should(
                be.visible)
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/toolbar')).all(
                (AppiumBy.CLASS_NAME, 'android.widget.TextView')).first.should(have.exact_text('Budget Book'))