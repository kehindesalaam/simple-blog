from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blogsite.models import BlogPost

class LatestEntriesFeed(Feed):
    title = "Blog news"
    link = '/blog/'
    description = "Updates on changes to blog"

    def items(self):
        return BlogPost.objects.order_by('-timestamp')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:10]