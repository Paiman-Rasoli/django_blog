import graphene
from graphene_django import DjangoObjectType
from post.models import Post
from . import resolvers

class PostType(DjangoObjectType):
      class Meta:
            model = Post
            fields = ("id", "title", "description")

class Query(graphene.ObjectType):
      """
      Queries for the Post model
      """
      posts = graphene.List(PostType)
      
      
      def resolve_posts(self,info, **kwargs):
            return resolvers.allPosts()
      
# mutations
class CreatePost(graphene.Mutation):
      class Arguments:
            title = graphene.String(required=True, description="The title of the post")
            description = graphene.String()
      
      post = graphene.Field(PostType)
      ok = graphene.Boolean()
      
      def mutate(self, info, title, description):
            post = resolvers.createPost(title, description)
            return CreatePost(ok=True, post=post)
      
class Mutation(graphene.ObjectType):
      post = CreatePost.Field()
      
      
schema = graphene.Schema(query=Query, mutation=Mutation)