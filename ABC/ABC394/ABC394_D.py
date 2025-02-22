# (, ), [, ], <, >

import queue

Q = queue.LifoQueue()

S = list(input())


for i in range(len(S)):
    if S[i] in ("(", "[", "<"):
        Q.put(S[i])
    else:
        if Q.qsize() == 0:
            print("No")
            exit()
        else:
            s = Q.get()

            if s + S[i] in ("()", "[]", "<>"):
                continue
            else:
                print("No")
                exit()                


if Q.qsize() == 0:
    print("Yes")
else:
    print("No")
