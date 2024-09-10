from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be, have


class MainPage:
    def __init__(self):
        self.toolbar = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/toolbar'))
        self.accountList = browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/accountList'))

    def should_have_icons_and_specific_text(self, name):
        with step('Check the main page'):
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/MANAGE_TEMPLATES_COMMAND')).should(be.visible)
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/BUDGET_COMMAND')).should(be.visible)
            browser.element((AppiumBy.ID, 'org.totschnig.myexpenses:id/fab')).should(be.visible)
            browser.element(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Open navigation drawer")')).should(
                be.visible)
            self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).first.should(have.exact_text(name))

    def should_have_specific_text_after_all_setting_on_start_pages(self, name, money, currency, description, type):
        with step('Check all specific options in the main menu after the third start page settings'):
            self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).first.should(have.exact_text(name))
            self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).second.should(have.text(money))
            self.toolbar.all((AppiumBy.CLASS_NAME, 'android.widget.TextView')).second.should(have.text(currency))

            self.toolbar.element((AppiumBy.CLASS_NAME, 'android.widget.ImageButton')).click()

            self.accountList.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text({name}).instance(1)'))
            self.accountList.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text({type})'))
            self.accountList.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text({description})'))

