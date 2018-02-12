from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Posts

# Create your tests here.


class PostTest(TestCase):
    def setUp(self):
        Posts.objects.create(
            title='this is testing posts',
            content='testing content for testing perpose'
            )

    def test_post_lists(self):
        url = reverse('posts:list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_post_details(self):
        url = reverse('posts:detail', kwargs={'slug': 'this-is-testing-posts'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_post_details_not_found(self):
        url = reverse('posts:detail', kwargs={'slug': 'this-is-testing-posts12'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    # def test_post_create_form(self):
    #   url = reverse()
