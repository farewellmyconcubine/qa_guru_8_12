from selene import have
from selene.support.shared import browser

import conftest
from qa_guru_8_12 import resources


class RegistrationPage:
    browser = conftest.browser_setup

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def choose_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_mobile_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def choose_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def choose_hobbie(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def select_picture(self, image_name):
        browser.element('#uploadPicture').send_keys(resources.path(image_name))
        return self

    def fill_adress(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def fill_state(self, name):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def fill_city(self, name):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def submit_form(self):
        browser.element('#submit').click()
        return self

    def should_have_registered(self, full_name, email, gender, phone_number, date, subject, hobbie, image, address,
                               state_and_city):
        browser.element('.table').all('tr td:nth-child(2)').should(have.texts
            (
            full_name,
            email,
            gender,
            phone_number,
            date,
            subject,
            hobbie,
            image,
            address,
            state_and_city
        ))
