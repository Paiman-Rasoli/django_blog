from django.test import TestCase
from post.models import Post

class TestPostModel(TestCase):
      def test_post_has_title(self):
            post = Post.objects.create(title="Paiman")
            self.assertTrue(len(post.title) > 0)            
