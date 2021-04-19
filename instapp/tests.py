from django.test import TestCase

from .models import Profile, Post, Comment, Follow, User

class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='Freddie')
        self.profile = Profile.objects.create(user = self.user,bio = 'Artist')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)

    def test_find_profile(self):
        self.profile.save()
        profile = Profile.find_profile('Freddie')
        self.assertTrue(len(profile) > 0)

class PostTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='Freddie')
        self.profile = Profile.objects.create(user = self.user,bio = 'Artist')

        self.post = Post.objects.create(user = self.user,profile = self.profile,caption ="Fascinating",like = 0)

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_get_posts(self):
        self.post.save()
        post = Post.get_posts()
        self.assertTrue(len(post) == 1)



class CommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='Freddie')

        self.comment= Comment.objects.create(user = self.user, comment='Awesomeee!!' )

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_get_comment(self):
        self.comment.save()
        comment = Comment.get_comment()
        self.assertTrue(len(comment) == 1)

