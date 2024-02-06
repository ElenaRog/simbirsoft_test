import os
from selene.support.shared import browser
from selene import have, be

from tests.conftest import RES_DIR
from classes.user_registration import Student


class RegistrationPage:

    @staticmethod
    def open():
        browser.open('/automation-practice-form')

    @staticmethod
    def register(student: Student):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.last_name)
        browser.element('#userEmail').type(student.email)
        browser.element(f'//*[contains(@id, "gender-radio") and '
                        f'@value="{student.gender.value}"]/following-sibling::*[1]').click()
        browser.element('#userNumber').type(student.number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(student.date_of_birth.month)
        browser.element('.react-datepicker__year-select').send_keys(student.date_of_birth.year)
        browser.element(
            f'.react-datepicker__day--0{student.date_of_birth.day}:not(.react-datepicker__day--outside-month)').click()
        browser.element('#subjectsInput').type(student.subject).press_enter()
        browser.all('.custom-checkbox').element_by(have.exact_text(student.hobbies.value)).click()
        browser.element('#uploadPicture').locate().send_keys(
            os.path.join(RES_DIR, student.picture)
        )
        browser.element('#currentAddress').type(student.address)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(student.state)
        ).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(student.city)
        ).click()
        browser.element('#submit').should(be.visible).click()

    @staticmethod
    def should_have_registered(student: Student):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{student.first_name} {student.last_name}',
                student.email,
                student.gender.female.value,
                student.number,
                student.date_of_birth.bday,
                student.subject,
                student.hobbies.sports.value,
                student.picture,
                student.address,
                f'{student.state} {student.city}'
            )
        )
