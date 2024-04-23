def print_loop():
    n = 1
    while True:
        print(f"Number # {n}.")
        n += 1


# print_loop()

numb = 1


def print_loop_rec():
    global numb
    print(f"Number # {numb}.")
    numb = numb + 1
    print_loop_rec()


print_loop_rec()
