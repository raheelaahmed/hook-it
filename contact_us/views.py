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

            # Save contact information to the database (optional)
            form.save()

            # Set success message using Django's messages framework
            messages.success(request, "Your message has been sent successfully!")

            # Redirect to avoid form resubmission on refresh
            return redirect('contact')  # Make sure the 'contact' URL name matches

    else:
        form = ContactForm()

    return render(request, 'contact_us/contact.html', {'form': form})  # Ensure the template path is correct
