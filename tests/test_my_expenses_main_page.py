import allure
from allure_commons.types import Severity

from my_expenses_tests.models.applications import app


@allure.feature('Test addition of expenses')
@allure.label('owner', 'Viktoriia Lavrova')
class TestAdditionExpenses:
    @allure.severity(severity_level=Severity.CRITICAL)
    def test_general_options_on_main_page(self):
        app.start_pages.skip_all_start_pages()
        app.main_page.close_notification()

        app.main_page.should_have_icons_and_specific_text(name='Budget Book')

    @allure.severity(severity_level=Severity.CRITICAL)
    def test_add_one_new_expense_and_check_it_on_main_page(self):
        app.start_pages.skip_all_start_pages()
        app.main_page.close_notification()
        app.new_expense.open_new_expense()
        app.new_expense.close_notification()

        app.new_expense.set_is_that_expense_or_income('Income')
        app.new_expense.enter_amount_of_money(1000)
        app.new_expense.click_button_save_data_and_close_form()

        app.main_page.should_be_on_the_main_page()
        app.main_page.should_have_specific_total_sum(1000)

    @allure.severity(severity_level=Severity.NORMAL)
    def test_fill_whole_form_of_new_expense_and_check_info_in_details_menu(self):
        app.start_pages.skip_all_start_pages()
        app.main_page.close_notification()
        app.new_expense.open_new_expense()
        app.new_expense.close_notification()

        app.new_expense.set_is_that_expense_or_income('Income')
        app.new_expense.enter_amount_of_money(1000)
        expense_datetime = app.new_expense.get_info_about_date_and_time()
        app.new_expense.enter_payee_or_payer_name('Dad')
        app.new_expense.enter_notes('Present')
        app.new_expense.add_tag('Birth')
        app.new_expense.add_tag('Parents')
        app.new_expense.click_button_save_data_and_close_form()
        app.main_page.open_details_menu_for_last_expense()

        app.main_page.should_have_specific_text_in_details_menu(money=1000, payee='Dad', notes='Present',
                                                                tags=['Birth', 'Parents'],
                                                                expense_datetime=expense_datetime)

    @allure.severity(severity_level=Severity.CRITICAL)
    def test_add_some_new_expenses(self):
        app.start_pages.skip_all_start_pages()
        app.main_page.close_notification()
        app.new_expense.open_new_expense()
        app.new_expense.close_notification()

        app.new_expense.set_is_that_expense_or_income('Income')
        app.new_expense.enter_amount_of_money(300)
        expense_datetime = app.new_expense.get_info_about_date_and_time()
        app.new_expense.click_button_save_data_and_close_form()

        app.new_expense.open_new_expense()
        app.new_expense.set_is_that_expense_or_income('Income')
        app.new_expense.enter_amount_of_money(200)
        app.new_expense.click_button_save_data_and_close_form()

        app.new_expense.open_new_expense()
        app.new_expense.set_is_that_expense_or_income('Expense')
        app.new_expense.enter_amount_of_money(150)
        app.new_expense.click_button_save_data_and_close_form()

        app.main_page.should_have_specific_total_sum(350)
        app.main_page.should_have_specific_number_of_expenses(number=3, expense_datetime=expense_datetime)

    @allure.severity(severity_level=Severity.CRITICAL)
    def test_delete_last_expense(self):
        app.start_pages.skip_all_start_pages()
        app.main_page.close_notification()
        app.new_expense.open_new_expense()
        app.new_expense.close_notification()

        app.new_expense.set_is_that_expense_or_income('Income')
        app.new_expense.enter_amount_of_money(1000)
        app.new_expense.click_button_save_data_and_close_form()
        app.main_page.delete_last_expence()

        app.main_page.should_have_specific_total_sum(0)

    @allure.severity(severity_level=Severity.NORMAL)
    def test_button_save_and_create(self):
        app.start_pages.skip_all_start_pages()
        app.main_page.close_notification()
        app.new_expense.open_new_expense()
        app.new_expense.close_notification()

        app.new_expense.click_button_save_and_create()
        app.new_expense.set_is_that_expense_or_income('Income')
        app.new_expense.enter_amount_of_money(20)
        app.new_expense.enter_payee_or_payer_name('Bank')
        app.new_expense.enter_notes('Cashback')
        app.new_expense.click_button_save_data_and_close_form()

        app.new_expense.enter_amount_of_money(30)
        app.new_expense.click_button_save_data_and_close_form()
        app.new_expense.click_button_close_expense_form()

        app.main_page.should_have_specific_total_sum(50)
        app.main_page.should_have_specific_number_of_expenses_with_equal_notes_and_payer(number=2, payee='Bank',
                                                                                         notes='Cashback')
