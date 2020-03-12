# Website, Page, SearchEngine, Text, Title


class SearchEngine:
    def __init__(self, index, engine):
        self.index = index
        self.engine = engine

    def crawl(self, url):
        self.index.append(url)
        return self.index


class Website:
    def __init__(self, domain, protocol, cms):
        self.domain = domain
        self.protocol = protocol
        self.cms = cms

    def _create_abs_url(self, rel_url):
        abs_url = self.protocol + self.domain + rel_url
        return abs_url


class Page(Website):
    def __init__(self, title, desc, h1, rel_url):
        self.title = title
        self.desc = desc
        self.h1 = h1
        self.rel_url = rel_url


class Text:
    def __init__(self, txt, ):


class Title(Text):
    pass
