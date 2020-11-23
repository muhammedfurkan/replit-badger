from django.views.generic import FormView
from app.forms import *
from django.http import *
from django.shortcuts import render


class HomeView(FormView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        form = InfoForm()
        context = {"form": form}
        return context

    def post(self, request, *args, **kwargs):
        form_data = InfoForm(request.POST)

        if form_data.is_valid():
            form_data = form_data.cleaned_data
            github_username, github_repo = form_data["github"].lstrip("https://").rstrip("/").split("/")[1:]
            markdown = f"[![Run on Repl.it](https://repl.it/badge/github/{github_username}/{github_repo})]" \
                       f"({form_data['replit']})"

            context = {"form": InfoForm(), "markdown": markdown, "request": request}
            return render(request, template_name="home.html", context=context)
