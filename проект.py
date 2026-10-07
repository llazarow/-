x = 0
y = 0


while True:
    key = input()

    if key == "w":
        y += 1
    elif key == "s":
        y -= 1
    elif key == "a":
        x -= 1
    elif key == "d":
        x += 1
    elif key == "q":
        break
    else:
        print('error')
        continue

    print({x}, {y})