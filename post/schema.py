import graphene
from graphene_django import DjangoObjectType
from post.models import Post

class PostType(DjangoObjectType):
      class Meta:
            model = Post
            fields = ("id", "name", "description")

class Query(graphene.ObjectType):
      """
      Queries for the Post model
      """
      posts = graphene.List(PostType)
      
      def resolve_posts(self, info, **kwargs):
            return Post.objects.all()

schema = graphene.Schema(query=Query)