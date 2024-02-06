from classes.registration_page import RegistrationPage
from classes.user_registration import Student, Gender, Hobbies, Birthday
import allure
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'elenarog')
@allure.feature('Silicium')
@allure.story('Test task from SimbirSoft')
def test_student_registration():
    student = Student(
        first_name='Elena',
        last_name='Rogozina',
        email='elenarog@mail.ru',
        gender=Gender.female,
        number='5554678578',
        date_of_birth=Birthday('27 June,1997'),
        subject='Biology',
        hobbies=Hobbies.sports,
        picture='image.png',
        address='Baker st. 221B',
        state='Uttar Pradesh',
        city='Agra')

    registration_page = RegistrationPage()
    with allure.step('Открытие страницы регистрации'):
        registration_page.open()

    with allure.step('Заполнение формы данными'):
        registration_page.register(student)

    with allure.step('Проверка корректности выведенных значений'):
        registration_page.should_have_registered(student)
