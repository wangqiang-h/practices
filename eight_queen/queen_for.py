def conflict(y, state):
    x = len(state)
    for position_x, position_y in enumerate(state):
        if position_y == y or (x - position_x) == (y - position_y) or (x-position_x) == (position_y-y):
            return True
    return False

def queens():
    for i in range(4):
        state = list()
        if not conflict(i, state):
            state.append(i)
            for i in range(4):
                if not conflict(i, state):
                    state.append(i)
                    for i in range(4):
                        if not conflict(i, state):
                            state.append(i)
                            for i in range(4):
                                if not conflict(i, state):
                                    state.append(i)
                                    print(state)
queens()
