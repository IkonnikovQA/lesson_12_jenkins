import os
import allure
from selene import be, have, command, by
from lesson_12 import UserStudent


class StudentRegistrationForm:
    def __init__(self, browser):
        self.b = browser
        self.table_responsive = self.b.all('.table-responsive tr')

    @allure.step('Открываем форму для регистрации')
    def open(self):
        self.b.open('automation-practice-form')
        self.b.should(have.title('DEMOQA'))
        self.b.element('[class="main-header"]').should(have.text('Practice Form'))

    @allure.step('Заполняем форму для регистрации')
    def register(self, user: UserStudent):
        self.b.element('#firstName').should(be.blank).click().type(user.first_name)
        self.b.element('#lastName').should(be.blank).click().type(user.last_name)
        self.b.element('#userEmail').should(be.blank).click().type(user.email)
        self.b.element('[for="gender-radio-1"]').click()
        self.b.element('#userNumber').should(be.blank).click().type(user.phone)
        self.b.element('#dateOfBirthInput').click()
        self.b.element('[class="react-datepicker__year-select"]').click().type(user.year_birthday).click()
        self.b.element('[class="react-datepicker__month-select"]').click().type(user.month_birthday).click()
        self.b.element(f'[class="react-datepicker__day react-datepicker__day--{user.day_birthday}"]').click()
        self.b.element('#subjectsInput').type(user.subject).press_enter()
        self.b.element(f'//label[contains(text(), "Sports")]').click()
        self.b.element('#uploadPicture').send_keys(os.path.abspath(user.path_for_picture))
        self.b.element('#currentAddress').should(be.blank).click().type(user.address)
        self.b.element(by.xpath('//div[@id = "state"]//input')).send_keys(user.state).press_tab()
        self.b.element('#react-select-3-input').type(user.state).press_enter()
        self.b.element('#react-select-4-input').type(user.city).press_enter()
        self.b.element('#submit').perform(command.js.click)

    @allure.step('Закрываем модальное окно')
    def close(self):
        self.b.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    # def close_modal_window(self):
    #     self.b.element('[id="closeLargeModal"]').click()

    @allure.step('Проверяем данные пользователя в таблице')
    def should_registered_user(self, user: UserStudent):
        full_name = f'{user.first_name} {user.last_name}'
        self.b.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        self.b.all('.table-responsive>table>tbody>tr').should(have.size(10))
        self.b.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                user.email,
                user.gender,
                user.phone,
                f'{user.day_birthday[1:]} {user.month_birthday},{user.year_birthday}',
                user.subject,
                f'{user.hobby}',
                user.name_image,
                user.address,
                f'{user.state} {user.city}'
            )
        )