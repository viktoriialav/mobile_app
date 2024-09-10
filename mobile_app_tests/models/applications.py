from mobile_app_tests.models.pages import my_expenses


class ApplicationManager:
    def __init__(self):
        self.my_expenses_start_pages = my_expenses.start_pages.StartPages()
        self.my_expenses_main_page = my_expenses.main_page.MainPage()
        self.my_expenses_main_menu = my_expenses.main_menu.MainMenu()


app = ApplicationManager()
