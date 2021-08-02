def sum_rec_chk(n):
    if n < 2:
        return 1
    else:
        print(f'n + sum_rec_chk({n}-1): {n} + {n-1}')
        return n + sum_rec_chk(n-1)


print(sum_rec_chk(20))

