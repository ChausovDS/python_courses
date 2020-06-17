def ascii(i, terminate):
    string = ''
    for n in range(10):
        string += f'{i+n} - {chr(i+n)} '
        if i+n == terminate:
            return string
    print(string)
    return ascii(i+10, terminate)


print(ascii(32, 128))
