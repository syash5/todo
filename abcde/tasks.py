from celery.registry import task
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from celery.task import Task

class Alert(Task):


    def run(self,user):
        subject, from_email, to= 'Alert,Your Task is Due' , 'sharma.yash520@gmail.com' , user.email
        html_content = render_to_string('alert.html' , {'user':user.first_name})
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


task.register(Alert)