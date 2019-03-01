class Rule():

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
