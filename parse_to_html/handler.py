class HtmlHandler(object):
    def callback(self, mark, name, *args):
        method = getattr(self, mark + name, None)
        if callable(method):
            method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def start_header(self):
        print('<h2>')

    def end_header(self):
        print('</h2>')

    def start_title(self):
        print('<h1>')

    def end_title(self):
        print('</h1>')

    def start_listitem(self):
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_list(self):
        print('<ol>')

    def end_list(self):
        print('</ol>')

    def start_p(self):
        print('<p>')

    def end_p(self):
        print('</p>')

    def feed(self, block):
        print(block)
