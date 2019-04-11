def conflict(y, state):
    x = len(state)
    for position_x, position_y in enumerate(state):
        if position_y == y or (x - position_x) == (y - position_y) or (x-position_x) == (position_y-y):
            return True
    return False


# def queens(num=4, state=()):
#     if len(state) == num -1:
#         for i in range(num):
#             if not conflict(i, state):
#                 yield (i,)
#     else:
#         for i in range(num):
#             if not conflict(i, state):
#                 for result in queens(num, state + (i,)):
#                     yield (i,) + result

def queens(num=4, state=()):
    if len(state) == num:
        yield state
    else:
        for i in range(num):
            if not conflict(i, state):
                yield from queens(num, state + (i,))
print(list(queens(4)))


