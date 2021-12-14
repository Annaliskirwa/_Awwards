from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_signup_email(name,receiver):
    # Creating message subject and sender
    subject = 'Ann-Awwwards account has been created for you.'
    sender = 'annalis.dispatchsupervisor@gmail.com'

    #passing in the context vairables
    # text_content = render_to_string('user/signup-email.txt',{"name": name})
    html_content = render_to_string('user/signup-email.html',{"name": name})

    msg = EmailMultiAlternatives(subject,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()