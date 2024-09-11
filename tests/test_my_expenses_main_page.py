import allure
from allure_commons.types import Severity

from my_expenses_tests.models.applications import app


@allure.feature('Test addition of expenses')
@allure.label('owner', 'Viktoriia Lavrova')
class TestAdditionExpenses:
    @allure.severity(severity_level=Severity.CRITICAL)
    def test_add_one_new_expense_and_check_it_on_main_page(self):
        # TODO Fix problem with checking of money
        app.start_pages.skip_all_start_pages()
        app.new_expense.open_new_expense()

        app.new_expense.set_is_that_expense_or_income('Income')
        app.new_expense.enter_amount_of_money(1000)
        expense_datetime = app.new_expense.take_info_about_date_and_time()
        app.new_expense.enter_payee_or_payer_name('Dad')
        app.new_expense.enter_notes('Present')
        app.new_expense.click_button_save_data_and_close_form()

        app.main_page.should_have_specific_text_in_the_expense_form_on_main_page(money=1000, payee='Dad',
                                                                                 notes='Present',
                                                                                 expense_datetime=expense_datetime)

    def test_add_one_new_expense_and_check_it_in_details_menu(self):
        app.start_pages.skip_all_start_pages()
        app.new_expense.open_new_expense()

        app.new_expense.set_is_that_expense_or_income('Income')
        app.new_expense.enter_amount_of_money(1000)
        expense_datetime = app.new_expense.take_info_about_date_and_time()
        app.new_expense.enter_payee_or_payer_name('Dad')
        app.new_expense.enter_notes('Present')
        app.new_expense.click_button_save_data_and_close_form()
        app.main_page.open_details_menu_for_last_expense()

        app.main_page.should_have_specific_text_in_details_menu(money=1000, payee='Dad', notes='Present',
                                                                expense_datetime=expense_datetime)

    def test_work_of_button_save_and_create(self):
        # TODO Finish
        app.start_pages.skip_all_start_pages()

    @allure.severity(severity_level=Severity.CRITICAL)
    def test_delete_last_expense(self):
        app.start_pages.skip_all_start_pages()
        start_total_money = app.main_page.take_current_amount_of_money()
        app.new_expense.open_new_expense()

        app.new_expense.set_is_that_expense_or_income('Income')
        app.new_expense.enter_amount_of_money(1000)
        app.new_expense.click_button_save_data_and_close_form()
        app.main_page.delete_last_expence()

        app.main_page.should_have_the_same_total_amount_of_money(start_total_money)

    @allure.severity(severity_level=Severity.CRITICAL)
    def test_add_some_new_expenses(self):
        # TODO Finish
        app.start_pages.skip_all_start_pages()
        app.new_expense.open_new_expense()

        app.new_expense.set_is_that_expense_or_income('Income')
        app.new_expense.enter_amount_of_money(10000)
        app.new_expense.enter_payee_or_payer_name('UNI')
        app.new_expense.enter_notes('Scholarship')


    @allure.severity(severity_level=Severity.NORMAL)
    def test_add_template_with_current_date(self):
        # TODO Finish
        app.start_pages.skip_all_start_pages()
        app.new_expense.open_new_expense()

        app.new_expense.click_button_save_as_template()
        app.new_expense.enter_title_for_template('Politech scholarship')

        app.new_expense.set_is_that_expense_or_income('Income')
        app.new_expense.enter_amount_of_money(2000)
        app.new_expense.enter_payee_or_payer_name('UNI')
        app.new_expense.enter_notes('Usual scholarship')

        app.new_expense.set_plan_for_template('Monthly')

        app.new_expense.click_create_new_expense()

    @allure.severity(severity_level=Severity.NORMAL)
    def test_add_template_with_future_date(self):
        # TODO Finish
        app.start_pages.skip_all_start_pages()
