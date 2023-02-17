from django.test import Client, TestCase
from django.urls import reverse
from alert.models import User
from .models import Alert

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.alert = Alert.objects.create(content='Test alert', state='Test state', lga='Test LGA', user=self.user, category='Test category')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_notification_view(self):
        response = self.client.get(reverse('notification'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'notification.html')

    def test_all_alerts_view(self):
        response = self.client.get(reverse('all_alerts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_alerts.html')

    def test_new_alert_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('new_alert'), {'content': 'New alert', 'state': 'New state', 'lga': 'New LGA', 'category': 'New category'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('all_alerts'))

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_register_view(self):
        response = self.client.post(reverse('register'), {'username': 'newuser', 'email': 'newuser@test.com', 'password': 'newpass', 'confirmation': 'newpass'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
