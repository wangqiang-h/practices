from abc import ABCMeta, abstractmethod
import re




class Rule(metaclass=ABCMeta):

    @abstractmethod
    def condition(self, block):
        pass

    def action(self, handler, block):
        handler.start(self.name)
        handler.feed(block)
        handler.end(self.name)
        return True


class HeaderRule(Rule):
    name = 'header'

    def condition(self, block):
        if '\n' not in block and len(block) < 70 and not block.endswith(':') and not block[0] == '-':
            return True


class TitleRule(Rule):
    name = 'title'
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeaderRule.condition(self, block)


class ListItemRule(Rule):
    name = 'listitem'

    def condition(self, block):
        if block[0] == '-':
            return True


class ListRule(Rule):
    name = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, handler, block):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.name)
            self.inside = True
        if self.inside and not ListItemRule.condition(self, block):
            handler.end(self.name)
            self.inside = False
        return False

class ParagraphRule(Rule):
    name = 'p'
    def condition(self, block):
        return True


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
