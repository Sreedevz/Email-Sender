from django.core.mail import send_mail
from django.test import TestCase

class EmailTest(TestCase):
    def test_send_email(self):
        send_mail(
            subject='CI/CD Email Test',
            message='This is a test email from Django CI/CD pipeline.',
            from_email='www.devmon346@gmail.com',         # 🔁 Replace this
            recipient_list=['sreedevz346@example.com'],  # 🔁 Replace this
            fail_silently=False,
        )
