n = input("Въведи число: ")
a = int(input("Въведи начална бройна система: "))
b = int(input("Въведи крайна бройна система: "))

d = 0
for x in n:
    d = d * a + ord(x) - ord('0')

r = ""
while d:
    x = d % b
    r = chr(x + ord('0')) + r
    d //= b

print("Резултат:", r)
