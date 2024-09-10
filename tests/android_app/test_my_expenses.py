import config
from mobile_app_tests.models.applications import app


def test_start_settings_pages():
    app.my_expenses_start_pages.should_have_special_text(text='My Expenses adapts to your preference', page=1)
    app.my_expenses_start_pages.open_next_page()
    app.my_expenses_start_pages.should_have_special_text(text='Your data stays in your hands', page=2)
    app.my_expenses_start_pages.open_next_page()
    app.my_expenses_start_pages.should_have_special_text(text='Let\'s set up your first account', page=3)
    app.my_expenses_start_pages.click_get_started()

    app.my_expenses_main_page.should_have_icons_and_specific_text(name='Budget Book')


def test_settings_on_first_start_page():
    app.my_expenses_start_pages.set_theme('Dark')
    app.my_expenses_start_pages.change_font_size(x=1, y=0)
    app.my_expenses_start_pages.make_display_form_compact(True)

    app.my_expenses_start_pages.should_have_special_settings_on_first_page(theme='Dark', font_size=2, compact=True)


def test_settings_on_second_start_page():
    app.my_expenses_start_pages.open_next_page()
    app.my_expenses_start_pages.turn_on_backup_database_at_the_specified_time(config.settings.is_bstack)
    app.my_expenses_start_pages.open_next_page()
    app.my_expenses_start_pages.click_get_started()

    app.my_expenses_main_menu.should_have_specific_options_in_main_menu_after_second_start_page_settings()


def test_settings_on_third_start_page():
    app.my_expenses_start_pages.open_next_page()
    app.my_expenses_start_pages.open_next_page()
    app.my_expenses_start_pages.create_label_for_budget_book('My lovely budget book')
    app.my_expenses_start_pages.set_opening_balance(100000)
    app.my_expenses_start_pages.open_more_options_on_third_page()
    app.my_expenses_start_pages.create_description('The main budget book')
    app.my_expenses_start_pages.set_budget_book_type('Bank account')
    app.my_expenses_start_pages.click_get_started()

    app.my_expenses_main_page.should_have_specific_text_after_all_setting_on_start_pages(
        name='My lovely budget book',
        money='100,000.00',
        currency='$',
        description='The main budget book',
        type='Bank accounts'
    )
