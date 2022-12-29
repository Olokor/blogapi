from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
# Create your tests here.

class Blogtest(TestCase):

    @classmethod
    def SetUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1', password='12345')
        testuser1.save()

        post_test = Post.objects.create(author='testuser1', title='Blog title', body='Blog body content')
        post_test.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Blog body content')
