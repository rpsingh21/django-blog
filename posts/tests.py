from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Posts


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        Posts.objects.create(
            user=self.user,
            title='this is testing posts',
            content='testing content for testing purpose'
        )

    def test_post_lists(self):
        url = reverse('posts:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_details(self):
        url = reverse(
            'posts:detail',
            kwargs={'slug': 'this-is-testing-posts'}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_details_not_found(self):
        url = reverse(
            'posts:detail',
            kwargs={'slug': 'this-is-testing-posts12'}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
