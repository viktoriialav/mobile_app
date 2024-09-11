import allure
from allure_commons.types import Severity

import config
from my_expenses_tests.models.applications import app


@allure.feature('Test Start Pages')
@allure.label('owner', 'Viktoriia Lavrova')
class TestStartPages:
    @allure.severity(severity_level=Severity.BLOCKER)
    def test_start_settings_pages(self):
        app.start_pages.should_have_special_text(text='My Expenses adapts to your preference', page=1)

        app.start_pages.open_next_page()
        app.start_pages.should_have_special_text(text='Your data stays in your hands', page=2)

        app.start_pages.open_next_page()
        app.start_pages.should_have_special_text(text='Let\'s set up your first account', page=3)

        app.start_pages.click_get_started()
        app.main_page.should_have_icons_and_specific_text(name='Budget Book')

    @allure.severity(severity_level=Severity.NORMAL)
    def test_settings_on_first_start_page(self):
        app.start_pages.set_theme('Dark')
        app.start_pages.change_font_size(x=1, y=0)
        app.start_pages.make_display_form_compact(True)

        app.start_pages.should_have_special_settings_on_first_page(theme='Dark', font_size=2, compact=True)

    @allure.severity(severity_level=Severity.NORMAL)
    def test_settings_on_second_start_page(self):
        app.start_pages.open_next_page()
        app.start_pages.turn_on_backup_database_at_the_specified_time(config.settings.is_bstack)
        app.start_pages.open_next_page()
        app.start_pages.click_get_started()

        app.main_menu.should_have_specific_options_in_main_menu_after_second_start_page_settings()

    @allure.severity(severity_level=Severity.NORMAL)
    def test_settings_on_third_start_page(self):
        app.start_pages.open_next_page()
        app.start_pages.open_next_page()
        app.start_pages.create_label_for_budget_book('My lovely budget book')
        app.start_pages.set_opening_balance(100000)
        app.start_pages.open_more_options_on_third_page()
        app.start_pages.enter_description('The main budget book')
        app.start_pages.set_budget_book_type('Bank account')
        app.start_pages.click_get_started()

        app.main_page.should_have_specific_text_after_all_setting_on_start_pages(name='My lovely budget book',
                                                                                 money='100,000.00',
                                                                                 currency='$',
                                                                                 description='The main budget book',
                                                                                 account_type='Bank accounts')
