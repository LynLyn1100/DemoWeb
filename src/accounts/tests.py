from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestViews(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/profile.html')

    def test_contact_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/contact.html')

    def test_profile_view_post(self):
        self.client.login(username='testuser', password='testpassword')
        data = {'first_name': 'John', 'last_name': 'Doe', 'username': 'johndoe'}
        response = self.client.post(reverse('profile'), data)
        self.assertEqual(response.status_code, 200)  # or 302 if you're redirecting after form submission
        # Add additional assertions here based on the behavior of your view

    # Add more test cases as needed
