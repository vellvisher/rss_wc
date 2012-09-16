import feedparser, sys
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def stripTags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

d = feedparser.parse(sys.argv[1])
wc = 0
for post in d.entries:
    wc += len(stripTags(post.summary).split())
print wc
