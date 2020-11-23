from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class InfoForm(forms.Form):
    github = forms.CharField(label="GitHub Repository", max_length=1024,
                             widget=forms.TextInput(attrs={"placeholder":
                                                           "Enter the URL "
                                                           "to a GitHub "
                                                           "Repository"}))

    replit = forms.CharField(label="Repl.it Repl", max_length=1024,
                             widget=forms.TextInput(attrs={"placeholder":
                                                           "Enter the URL to a "
                                                           "Repl.it Repl"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "/"

        self.helper.add_input(Submit("submit", "Submit"))
