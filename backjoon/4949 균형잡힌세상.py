import sys

while True:
    string = sys.stdin.readline()
    if string== ".":
        break
    else:
        stack = []
        check = True
        for word in string:
            if word == '(' or word == '[':
                stack.append(word)
            elif word == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    check = 0
                    break
            elif word == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    check = 0
                    break
    if not stack and check == 1:
        print('yes')
    else:
        print('no')
            

