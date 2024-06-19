from lesson_12 import StudentRegistrationForm, UserStudent
# from config import browser as b

def test_form(setup_browser):
    alexey_user = UserStudent()
    reg_form = StudentRegistrationForm(browser=setup_browser)
    reg_form.open()
    reg_form.register(alexey_user)
    reg_form.close()
    reg_form.should_registered_user(alexey_user)