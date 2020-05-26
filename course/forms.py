from django import forms
from django.forms import TextInput, Textarea, NumberInput, widgets, formset_factory
from djrichtextfield.widgets import RichTextWidget
from jsoneditor.forms import JSONEditor
from jsonfield.forms import JSONFormField

from course.models import MultipleChoiceQuestion, DIFFICULTY_CHOICES, CheckboxQuestion, JavaQuestion, QuestionCategory


class ProblemCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['difficulty'].widget.attrs.update({'class': 'form-control'})
        self.fields['difficulty'].initial = "EASY"

    # max_submission_allowed = forms.IntegerField(
    #     widget=NumberInput(attrs={
    #         'class': 'form-control',
    #     })
    # )

    title = forms.CharField(
        label="Question Name",
        widget=TextInput(attrs={
            'class': 'form-control'
        })
    )

    text = forms.CharField(
        label='Question',
        widget=RichTextWidget(field_settings='advanced')
    )

    answer = forms.CharField(
        initial="",
        widget=forms.HiddenInput(attrs={
            'class': 'form-control',
        })
    )

    # tutorial = forms.CharField(
    #     widget=RichTextWidget(field_settings='advanced')
    # )


class ChoiceProblemCreateForm(ProblemCreateForm):
    variables = JSONFormField(
        initial='[{}]',
        widget=forms.HiddenInput(),
        help_text="""
        It should be an array with each element a set of variables to choose.
        A valid example:
        [
            {
                "x" : 1,
                "y" : 2,
            },
            {
                "x" : 5,
                "y" : 8,
            }
        ]
        """
    )

    choices = JSONFormField(
        widget=forms.HiddenInput(),
        initial='{}',
        help_text="""
        It should be an object of choices.
        A valid example:
        {
            "a" : "{{x}} is odd and {{y}} is odd",
            "b" : "{{x}} is even and {{y}} is odd",
            "c" : "{{x}} is odd and {{y}} is even",
            "d" : "{{x}} is even and {{y}} is even"
        }
        """
    )


class ProblemFilterForm(forms.Form):
    query = forms.CharField(
        label='Search',
        required=False,
        widget=widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search in the problem set...',
        })
    )

    difficulty = forms.ChoiceField(
        required=False,
        choices=[('', 'All')] + DIFFICULTY_CHOICES,
        widget=widgets.Select(attrs={
            'class': 'form-control',
        })
    )

    category = forms.ModelChoiceField(
        required=False,
        empty_label='All',
        queryset=QuestionCategory.objects.filter(parent__isnull=True).all(),
        widget=widgets.Select(attrs={
            'class': 'form-control',
        })
    )

    solved = forms.ChoiceField(
        required=False,
        choices=[('', 'All'), ('Solved', 'Solved'), ('Partially Correct', 'Partially Correct'),
                 ('Unsolved', 'Unsolved'), ('Wrong', 'Wrong'),
                 ('Unopened', 'Unopened')],
        widget=widgets.Select(attrs={
            'class': 'form-control',
        })
    )


class CheckboxQuestionForm(ChoiceProblemCreateForm):
    class Meta:
        model = CheckboxQuestion
        fields = (
            'title', 'difficulty', 'category', 'text', 'answer', 'variables', 'choices', 'visible_distractor_count')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['answer'].help_text = '\nPlease write the correct choices in this format.\nexample: [\'a\', \'b\']'

    def clean(self):
        data = super().clean()
        data['visible_distractor_count'] = 999 if data['distractor_count'] == 'All' else int(data['distractor_count'])
        return data

    visible_distractor_count = forms.IntegerField(
        initial=999,
        widget=forms.HiddenInput()
    )

    distractor_count = forms.ChoiceField(
        choices=[('All', 'All'), ('2', '2'), ('3', '3')],
        initial='All',
        widget=forms.RadioSelect(),
    )


class MultipleChoiceQuestionForm(ChoiceProblemCreateForm):
    class Meta:
        model = MultipleChoiceQuestion
        fields = (
            'title', 'difficulty', 'category', 'text', 'answer', 'variables', 'choices', 'visible_distractor_count')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['answer'].help_text = '\nPlease only write the name of the correct choice'

    def clean(self):
        data = super().clean()
        data['visible_distractor_count'] = 999 if data['distractor_count'] == 'All' else int(data['distractor_count'])
        return data

    visible_distractor_count = forms.IntegerField(
        initial=999,
        widget=forms.HiddenInput()
    )

    distractor_count = forms.ChoiceField(
        choices=[('All', 'All'), ('2', '2'), ('3', '3')],
        initial='All',
        widget=forms.RadioSelect()
    )


class JavaQuestionForm(ProblemCreateForm):
    class Meta:
        model = JavaQuestion
        fields = (
            'title', 'difficulty', 'category', 'text', 'test_cases')
        exclude = ('answer',)

    answer = None

    test_cases = JSONFormField(
        widget=JSONEditor(),
        help_text="""
        It should be an array if test_cases each element need to have input and outpur.
        A valid example:
        [
            {
                "input": "2",
                "output": "Even"
            },
            {
                "input": "3",
                "output": "Odd"
            }
        ]
        """
    )


class ChoiceForm(forms.Form):
    text = forms.CharField(
        label='Answer',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.empty_permitted = False
