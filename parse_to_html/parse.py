import re


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


block_list = list(change_to_block_list('text'))

title_first = True
list_start = False

# print(block_list)
print('<html><body>')
for block in block_list:
    block = re.sub('\*(.*)\*', '<em>\\1</em>', block)

    if block[0] == '-':
        if not list_start:
            print('<ol>')
            list_start = True
        print('<li>')
        print(block)
        print('</li>')

    elif '\n' not in block and len(block) < 70 and not block.endswith(':'):
        if list_start:
            print('</ol>')
            list_start = False

        if title_first:
            print('<h1>')
            print(block)
            print('</h1>')
            title_first = False
        else:
            print('<h2>')
            print(block)
            print('</h2>')
    else:
        if list_start:
            print('</ol>')
            list_start = False
        print('<p>')
        print(block)
        print('</p>')

print('</body></html>')
