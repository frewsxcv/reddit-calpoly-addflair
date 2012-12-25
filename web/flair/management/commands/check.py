#!/usr/bin/env python2

from reddit import Reddit
from django.core.management.base import BaseCommand, CommandError
import register.calpoly as calpoly
from register.models import User
from flair.flairclient import FlairClient
from settings import REDDIT_USERNAME, REDDIT_PASSWORD


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        messages = get_messages()
        for m in messages:
            if get_subject(m) == 'Add Flair':
                try:
                    conf_num = int(get_conf_num(m))
                except ValueError:
                    continue
                else:
                    author = m[u'data'][u'author']
                    author = author.lower()
                    message_sent = m[u'data'][u'created']
                    try:
                        user = User.objects.get(username=author)
                    except User.DoesNotExist:
                        continue
                    if conf_num == user.confirm_num and \
                            message_sent > user.message_sent:
                        user.confirmed = True
                        user.message_sent = message_sent
                        add_flair(author, user.major, user.year)
                        user.save()


def get_subject(message):
    return message[u'data'][u'subject']


def get_conf_num(message):
    body = message[u'data'][u'body']
    return body.split('\n')[1].split(' ')[-1]


def get_messages():
    r = Reddit(user_agent='calpoly-flair')
    r.login(user=REDDIT_USERNAME, password=REDDIT_PASSWORD)
    inbox = r.get_inbox()
    return inbox.get_messages()


def add_flair(user, major, year):
    major_full = calpoly.majors()[major]
    for college, majors in calpoly.colleges.items():
        if major in majors:
            css_class = college
    client = FlairClient()
    client.log_in()
    client.flair('calpoly', user, major_full + ' - ' + str(year), css_class)

