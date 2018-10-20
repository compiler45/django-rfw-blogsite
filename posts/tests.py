from django.contrib.auth.models import User
from django.test import TestCase

from posts.models import Post

# Create your tests here.


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # make a user and a blog post

        test_user = User.objects.create(
            username='testuser', password='abc123'
        )
        test_user.save()

        test_post = Post.objects.create(
            author=test_user, title='Blog title',
            body='Body content...'
        )

        test_post.save()

        cls.test_user = test_user
        cls.test_post = test_post

    def test_blog_post_is_stored_with_correct_attributes(self):
        post = Post.objects.get(id=1)
        self.assertEquals(post.author, self.test_user)
        self.assertEquals(post.title, self.test_post.title)
        self.assertEquals(post.body, self.test_post.body)

