def conflict(y, state):
    x = len(state)
    for position_x, position_y in enumerate(state):
        if position_y == y or (x - position_x) == (y - position_y) or (x - position_x) == (position_y - y):
            return True
    return False


def queens(num, state):
    # state 记录之前行选择的位置
    if len(state) == num:
        print(state)
        return True
    else:
        # 遍历一行可能的位置
        for i in range(num):
            if not conflict(i, state):
                state.append(i)
                if queens(num, state):
                    # return True  #遇到一个解，就退出了
                    state.pop()
                else:
                    # 根据递归的结果，这个位置错误的。
                    state.pop()
        # 这一行都没有合适的位置
        return False


queens(4, [])
