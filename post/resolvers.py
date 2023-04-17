from .models import Post

def allPosts():
      return Post.objects.all()

def createPost(title: str, description: str) -> Post:
      post = Post(title=title, description=description)
      post.save()
      return post