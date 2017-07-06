# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from forms import ContactForm
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.core.urlresolvers import reverse


def register(request):
    return render(request, "form/register.html")


def home(request):
    form_class = ContactForm
    return render(request, "index.html", {
        'form': form_class
    })


def contact(request):
    # new logic!
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission from: " + contact_email,
                content,
                contact_email,
                ['TO_EMAIL@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect(reverse('contact_success'))
        return redirect(reverse("/"), {"alert": "Invalid form data was given. Please try again."})
    return redirect(reverse("/"), {"alert": "Invalid request was made. Please try again."})


def contact_success(request):
    return HttpResponse('<script> \
                            window.setTimeout(function(){ \
                            window.location.href = "redirect_url"; \
                            }, 3000); \
                        </script>'
                        'Success! Thank you for your message. <br/>'
                        'Redirecting in 3 seconds')
