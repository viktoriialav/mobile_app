import allure
from allure_commons.types import Severity

import config
from my_expenses_tests.models.applications import app


@allure.feature('Test start pages')
@allure.label('owner', 'Viktoriia Lavrova')
@allure.label('layer', 'ui')
class TestStartPages:
    @allure.severity(severity_level=Severity.BLOCKER)
    @allure.tag('Start page')
    def test_start_pages_titles_and_open_the_main_page(self):
        app.start_pages.should_have_specific_title(text='My Expenses adapts to your preference', page=1)

        app.start_pages.open_next_page()
        app.start_pages.should_have_specific_title(text='Your data stays in your hands', page=2)

        app.start_pages.open_next_page()
        app.start_pages.should_have_specific_title(text='Let\'s set up your first account', page=3)

        app.start_pages.click_get_started()
        app.main_page.should_have_specific_text()

    @allure.severity(severity_level=Severity.NORMAL)
    @allure.tag('Settings', 'Start page')
    def test_settings_on_first_start_page(self):
        # WHEN
        app.start_pages.set_theme('Dark')
        app.start_pages.change_font_size(x=1, y=0)
        app.start_pages.make_display_form_compact(True)

        # THEN
        app.start_pages.should_have_specific_settings_on_first_page(theme='Dark', font_size=2, compact=True)

    @allure.severity(severity_level=Severity.NORMAL)
    @allure.tag('Settings', 'Start page')
    def test_settings_on_second_start_page(self):
        # GIVEN
        app.start_pages.open_next_page()

        # WHEN
        app.start_pages.turn_on_backup_database_at_the_specified_time(config.settings.is_bstack)
        app.start_pages.open_next_page()
        app.start_pages.click_get_started()
        app.main_page.close_notification()
        app.main_menu.open()
        app.main_menu.open_settings()
        app.main_menu.open_backup_and_restore_menu_from_settings()

        # THEN
        app.main_menu.should_have_specific_options_in_main_menu_after_second_start_page_settings()

    @allure.severity(severity_level=Severity.NORMAL)
    @allure.tag('Settings', 'Start page', 'Balance')
    def test_settings_on_third_start_page(self):
        # GIVEN
        app.start_pages.open_next_page()
        app.start_pages.open_next_page()

        # WHEN
        app.start_pages.create_label_for_budget_book('My lovely budget book')
        app.start_pages.set_opening_balance(100000)
        app.start_pages.open_more_options_on_third_page()
        app.start_pages.enter_description('The main budget book')
        app.start_pages.set_budget_book_type('Bank account')
        app.start_pages.click_get_started()

        # THEN
        app.main_page.should_have_specific_text_after_all_setting_on_start_pages(name='My lovely budget book',
                                                                                 money='100000',
                                                                                 description='The main budget book',
                                                                                 account_type='Bank accounts')
