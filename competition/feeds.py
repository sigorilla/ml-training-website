import time

import requests
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed, Enclosure
from models import Competition
from ml_training.settings import TITLE, DESCRIPTION


class RssCompetitionsFeed(Feed):
    title = TITLE
    description = DESCRIPTION
    link = '/'
    categories = ('ml', 'competitions')

    def get_object(self, request, *args, **kwargs):
        if request.user.is_staff and request.user.is_active:
            return request.user

    def author_name(self, user):
        if user:
            name = user.get_full_name()
            return name if name else None

    def author_email(self, user):
        if user:
            return user.email if user.email else None

    def items(self):
        return Competition.objects.filter(active__exact=True)[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_enclosures(self, item):
        url = item.get_image_url().replace('https://', 'http://')
        if url is None:
            return None
        headers = requests.head(url).headers
        type = header['content-type']
        if not type.startswith('image'):
            type = 'image/jpeg'
        return [Enclosure(url=url, length=headers['content-length'], mime_type=type)]

    def item_pubdate(self, item):
        return item.pub_date

    def item_updateddate(self, item):
        return item.upd_date


class AtomCompetitionsFeed(RssCompetitionsFeed):
    feed_type = Atom1Feed
    subtitle = RssCompetitionsFeed.description
