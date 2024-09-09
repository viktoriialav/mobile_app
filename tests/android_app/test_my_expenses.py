from mobile_app_tests.models.applications import app


def test_check_start_settings_page():
    app.my_expenses_start_pages.set_theme('Dark')
    app.my_expenses_start_pages.change_font_size(x=1, y=0)
    app.my_expenses_start_pages.make_display_form_compact(True)

    app.my_expenses_start_pages.should_have_special_settings_on_first_page(theme='Dark',
                                                                           font_size=2,
                                                                           compact=True)


def test_start_settings_pages():
    app.my_expenses_start_pages.should_have_special_text(text='My Expenses adapts to your preference', page=1)
    app.my_expenses_start_pages.open_next_page()
    app.my_expenses_start_pages.should_have_special_text(text='Your data stays in your hands', page=2)
    app.my_expenses_start_pages.open_next_page()
    app.my_expenses_start_pages.should_have_special_text(text='Let\'s set up your first account', page=3)
    app.my_expenses_start_pages.click_get_started()

    app.my_expenses_main_page.should_have_icons_and_special_text()
