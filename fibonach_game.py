# Fibonachi

def fib_upto(upto):
    new_num, first_num = 0, 0
    sec_num = 1

    while new_num < upto:
        new_num = first_num + sec_num
        print(first_num)
        first_num = sec_num
        sec_num = new_num

fib_upto(100)
print()

