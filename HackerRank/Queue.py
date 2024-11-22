import sys
import os


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    t = int(input())
    queue_list = []
    for i in range(t):
        inp = input().split(" ")
        if inp[0] == '1':
            queue_list.append(inp[1])
        elif inp[0] == '2':
            queue_list.pop(0)
        elif inp[0] == '3':
            fptr.write(queue_list[0] + '\n')

    fptr.close()
