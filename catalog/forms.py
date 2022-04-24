from django import forms
from .models import BookInstance
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import datetime


class RenewBookModelForm(forms.ModelForm):
    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        # Проверка того,что дата не в прошлом
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check date is in range librarian allowed to change (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Не забывайте всегда возвращать очищенные данные
        return data

    class Meta:
        model = BookInstance
        fields = ['due_back', ]
        labels = {'due_back': _('Renewal date'), }
        help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).'), }

