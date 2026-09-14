from typing import List

def read_integers() -> List[int]:
    message=input()
    return [int(x) for x in message.split(",")]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())