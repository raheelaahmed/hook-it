from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=email,
                    recipient_list=['patattern.hookit@gmail.com'],
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found in form input')

            form.save()

            messages.success(request,
                             "Your message has been sent successfully!")

            return redirect('contact')

    else:
        form = ContactForm()

        context = {
            'form': form,
        }

    return render(request, 'contact_us/contact.html', context)
