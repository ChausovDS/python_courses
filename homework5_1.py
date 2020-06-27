i = 32
while i <= 127:
    string = ''
    for j in range(10):
        string += f'{i} - {chr(i)} '
        i += 1
        if i > 127:
            break
    print(string)
