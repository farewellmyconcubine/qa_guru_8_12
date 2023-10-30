from qa_guru_8_12.pages.registration_page import RegistrationPage
import allure


@allure.title('Success student registration')
def test_student_registration_form():
    registration_page = RegistrationPage()

    with allure.step('Open registration page'):
        registration_page.open()

    with allure.step('Fill the form'):
        registration_page.fill_first_name('Ivan')
        registration_page.fill_last_name('Petrov')
        registration_page.fill_email('ivanpetrov@example.com')
        registration_page.choose_gender('Male')
        registration_page.fill_mobile_number('7999111223')
        registration_page.fill_date_of_birth('2001', 'May', '15')
        registration_page.choose_subject('English')
        registration_page.choose_hobbie('Reading')
        registration_page.select_picture('cat_image.jpg')
        registration_page.fill_adress('Sovetskaya street, 15')
        registration_page.fill_state('NCR')
        registration_page.fill_city('Delhi')

    with allure.step('Submit form'):
        registration_page.submit_form()

    with allure.step('Check results'):
        registration_page.should_have_registered(
            'Ivan Petrov',
            'ivanpetrov@example.com',
            'Male',
            '7999111223',
            '15 May,2001',
            'English',
            'Reading',
            'cat_image.jpg',
            'Sovetskaya street, 15',
            'NCR Delhi')
