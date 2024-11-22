
n = int(input())
text = ""
history = []

for i in range(n):
    multi_input = input().rstrip().split()
    q = int(multi_input[0])
    
    if q == 1:
        s = multi_input[1]
        history.append(text)
        text += s
    elif q == 2:
        s = multi_input[1]
        history.append(text)
        n = int(s)
        text = text[:-n]
    elif q == 3:
        s = int(multi_input[1])
        print(text[s - 1])
    elif q == 4:
        if history:
            text = history.pop()
