from django.test import TestCase

# Создайте ваши тесты здесь

import datetime
from django.utils import timezone
from catalog.forms import RenewBookModelForm


class RenewBookFormTest(TestCase):

    def test_renew_form_date_field_label(self):
        form = RenewBookModelForm()
        self.assertTrue(
            form.fields['due_back'].label is None or form.fields['due_back'].label == 'Renewal date')

    def test_renew_form_date_field_help_text(self):
        form = RenewBookModelForm()
        self.assertEqual(form.fields['due_back'].help_text, 'Enter a date between now and 4 weeks (default 3).')

    def test_renew_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form_data = {'due_back': date}
        form = RenewBookModelForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_date_too_far_in_future(self):
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form_data = {'due_back': date}
        form = RenewBookModelForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        date = datetime.date.today()
        form_data = {'due_back': date}
        form = RenewBookModelForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_renew_form_date_max(self):
        date = timezone.now() + datetime.timedelta(weeks=4)
        form_data = {'due_back': date}
        form = RenewBookModelForm(data=form_data)
        self.assertTrue(form.is_valid())
