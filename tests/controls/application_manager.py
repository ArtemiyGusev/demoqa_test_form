from demoqa_test_form.tests.controls.dropdown import DropDown
from demoqa_test_form.tests.controls.check_table_text import CheckTableText
from demoqa_test_form.tests.controls.datepicker import DatePicker
from demoqa_test_form.tests.controls.subject import Subject


class ApplicationManager:

    def __init__(self):
        self.drop_down = DropDown
        self.check_table_text = CheckTableText
        self.date_picker = DatePicker
        self.subject = Subject


app = ApplicationManager()
