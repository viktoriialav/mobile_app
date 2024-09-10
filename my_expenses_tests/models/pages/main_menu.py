from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class MainMenu:
    def open(self):
        with step('Open the main menu'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'More options')).click()

    def open_settings(self):
        with step('Open Settings menu'):
            browser.all((AppiumBy.ID, 'org.totschnig.myexpenses:id/title')).element_by(
                have.exact_text('Settings')).click()

    def open_backup_and_restore_menu_from_settings(self):
        with step('Open Backup/Restore menu'):
            browser.all((AppiumBy.ID, 'android:id/title')).element_by(have.exact_text('Backup / Restore')).click()

    def should_have_specific_options_in_main_menu_after_second_start_page_settings(self):
        with step('Check all specific options in the main menu after the second start page settings'):
            self.open()
            self.open_settings()
            self.open_backup_and_restore_menu_from_settings()
            browser.all((AppiumBy.ID, 'android:id/title')).element_by(have.exact_text('Auto-backup time')).should(
                be.enabled)
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                             'new UiSelector().className("android.widget.LinearLayout").instance(27)')).should(
                be.enabled)
