import re
from ruler import *
from handler import *


class ParseBase(object):
    def __init__(self, handler, filename):
        self.handler = handler
        self.block_list_generator = self.change_to_block_list(filename)
        self.filters = []
        self.rules = []

    def add_filter(self, filter_func):
        self.filters.append(filter_func)

    def add_rule(self, rule):
        self.rules.append(rule)

    @staticmethod
    def change_to_block_list(filename):
        with open(filename) as fd:
            block_list = []
            for line in fd:
                if line.strip():
                    block_list.append(line)
                else:
                    item = ''.join(block_list).strip()
                    if item:
                        yield item
                    block_list = []
            if block_list:
                item = ''.join(block_list).strip()
                if item:
                    yield item

    def parse(self):
        for block in self.block_list_generator:
            for filter_func in self.filters:
                block = filter_func(block)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(self.handler, block)
                    if last:
                        break


class Parse(ParseBase):
    def __init__(self, handler, filename):
        super().__init__(handler, filename)
        self.add_filter(lambda x: re.sub('\*(.*)\*', '<em>\\1</em>', x))
        self.add_rule(ListRule())
        self.add_rule(TitleRule())
        self.add_rule(HeaderRule())
        self.add_rule(ListItemRule())
        self.add_rule(ParagraphRule())


p = Parse(HtmlHandler(), 'text')
p.parse()
