from tests.controls.application_manager import app
from selene.support.shared.jquery_style import s, ss
from env import *
from tests.helper.acceptance_test_modul import url_open_size, add_file


def test_case_practice_form():
    url_open_size('/automation-practice-form')

    s('//*[@id="firstName"]').type('Jack')
    s('//*[@id="lastName"]').type('Shepard')
    s('//*[@id="userEmail"]').type('Jack@mail.ru')
    s('//*[@id="userNumber"]').type('4815162342')
    s('//*[@id="currentAddress"]').type('Oceanic')

    app.subject(s(subjects_input)).select_element_in_list('g', select_element_in_subject)

    app.date_picker(s(date_of_birth_input)).select_date_in_datepicker()

    s(gender_select_male).click()

    s(hobbies_select_sports).click()

    app.drop_down(s(list_state)).select_element_in_dropdown(element_in_list_state)

    app.drop_down(s(list_city)).select_element_in_dropdown(element_in_list_city)

    add_file(send_picture_button, file_name=file_name)

    s(send_data).click()

    app.check_table_text(ss(table_name)).check_expected_result_in_table(*expected_result_in_table)
