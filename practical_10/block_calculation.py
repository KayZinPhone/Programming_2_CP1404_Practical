def block(row):
    if row<=0:
        return 0
    return row+block(row-1)


print(block(6))