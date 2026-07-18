from django.test import TestCase
from .models import Counter
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class CounterModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username="alice",
            password="password123",
        )
        self.client.force_login(self.user)

    def test_create_counter_if_missing(self):
        self.assertFalse(
            Counter.objects.filter(user=self.user).exists()
        )

        response = self.client.get(reverse("button"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Counter.objects.filter(user=self.user).exists()
        )
        
    def test_counter_already_exists(self):
        obj = Counter.objects.create(
            user=self.user,
            count=5,
        )

        response = self.client.get(reverse("button"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Counter.objects.filter(user=self.user).exists()
        )
        self.assertEqual(
            Counter.objects.filter(user=self.user).count(),
            1,
        )
        obj.refresh_from_db()
        self.assertEqual(obj.count, 5)

class IncrementTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="alice",
            password="password123",
        )
        self.client.force_login(self.user)

    def test_exists_counter_post_increment(self):
        obj = Counter.objects.create(
            user=self.user,
            count=5,
        )
    
        response = self.client.post(reverse("click"))
    
        self.assertEqual(response.status_code, 302)

        obj.refresh_from_db()
        self.assertEqual(obj.count, 6)

    def test_nonexist_counter_post_increment(self):
        response = self.client.post(reverse("click"))
    
        self.assertEqual(response.status_code, 302)

        obj = Counter.objects.filter(user=self.user)
        self.assertTrue(obj.exists())
        self.assertEqual(obj.count(), 1)
