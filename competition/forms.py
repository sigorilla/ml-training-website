from django.utils import timezone
from django.utils.translation import ugettext as _

from competition.models import Competition
from django import forms


class CreateCompetitionForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = ('title', 'content', 'link', 'image', 'start_date', 'finish_date')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'image': forms.URLInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'finish_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        super(CreateCompetitionForm, self).clean()
        start = self.cleaned_data.get('start_date')
        finish = self.cleaned_data.get('finish_date')
        now = timezone.now()
        if start < now:
            self.add_error('start_date', forms.ValidationError(_('Date must be in the future.'), code='invalid'))
        if finish < now:
            self.add_error('finish_date', forms.ValidationError(_('Date must be in the future.'), code='invalid'))
        if start >= finish:
            self.add_error('finish_date', forms.ValidationError(_('Finish date must be greater than start date.'),
                                                                code='invalid'))
        return self.cleaned_data

    def save(self, commit=True):
        self.instance.active = False
        return super(CreateCompetitionForm, self).save()

