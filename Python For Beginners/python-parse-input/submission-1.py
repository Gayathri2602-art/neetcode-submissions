from typing import List

def read_integers() -> List[int]:
    message=input()
    list_=[]
    for x in message.split(","):
        list_.append(int(x))
    return list_
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())