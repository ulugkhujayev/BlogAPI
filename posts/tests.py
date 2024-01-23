from django.contrib.auth import get_user_model
from django.test import TestCase


from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="myemail@gmail.com", password="verysecret"
        )
        cls.post = Post.objects.create(
            author=cls.user, title="title 1", body="Content 1"
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "title 1")
        self.assertEqual(self.post.body, "Content 1")
        self.assertEqual(str(self.post), "title 1")
