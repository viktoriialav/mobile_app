from my_expenses_tests.models import pages


class ApplicationManager:
    def __init__(self):
        self.start_pages = pages.start_pages.StartPages()
        self.main_page = pages.main_page.MainPage()
        self.main_menu = pages.main_menu.MainMenu()
        self.new_expense = pages.new_expense.NewExpense()


app = ApplicationManager()
