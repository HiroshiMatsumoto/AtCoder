text = input()
if 'a' not in text:
    print(-1)

else:
    idx = text[::-1].index('a')
    print(len(text) - idx)