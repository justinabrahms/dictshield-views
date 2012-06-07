class View(object):

    def __init__(self, document):
        self.document = document


class WhitelistView(View):

    def __getattr__(self, field):
        if field in self.fields:
            return getattr(self.document, field)
        else:
            raise AttributeError("%r object has no attribute %r"
                % (self.__class__.__name__, field))
