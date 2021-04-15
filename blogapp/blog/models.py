from django.db import models
from django.urls import reverse  # 1
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50) # 2
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.') # 3
    description = models.CharField('DESCIPTION', max_length=50, blank=True, help_text='simple description text.') # 4
    content = models.TextField('CONTENT') # 5
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True) # 6
    modify_dt = models.DateTimeField("MODIFY DATE", auto_now=True) # 7
    tags = TaggableManager(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="OWNER", blank=True, null=True)

    class Meta:  # 8
        verbose_name = 'post' # 9
        verbose_name_plural = 'posts' # 10
        db_table = 'blog_posts' # 11
        ordering = ('-modify_dt',) # 12

    def __str__(self): # 13
        return self.title

    def get_absolute_url(self): # 14
        return reverse("blog:post_detail", args=(self.slug,))

    def get_previous(self): # 15
        return self.get_previous_by_modify_dt()

    def get_next(self): # 16
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


    
    
