import smtplib

from django.http import HttpResponse
from django.template import loader
from decouple import config

from .models import Email


def index(request):
    print(request.method)
    if request.method == 'POST':
        emails = dict(request.POST)['email']
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        send_email(emails=emails, subject=subject, body=body)

    email_list = Email.objects.all()
    template = loader.get_template('emailer/index.html')
    context = {
            'email_list': email_list
            }
    return HttpResponse(template.render(context, request))


def send_email(emails=None, subject=None, body=None):
    if emails and subject and body:

        # Gmail Sign In
        gmail_sender = config('EMAIL', cast=str)
        gmail_password = config('PASSWORD', cast=str)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_password)

        for email in emails:
            email_body = '\r\n'.join(
                    [
                        f'To: {email}',
                        f'From: {gmail_sender}',
                        f'Subject: {subject}',
                        '', body,
                        ]
                    )

            try:
                server.sendmail(gmail_sender, [email], email_body)
                print(f'email sent to {email}')
            except Exception:
                print(f'error sending email to {email}')

        server.quit()
