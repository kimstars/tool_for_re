def hextoText(h):
    return bytes.fromhex(h).decode('utf-8')

h = input()

print(hextoText(h))

# P0rt