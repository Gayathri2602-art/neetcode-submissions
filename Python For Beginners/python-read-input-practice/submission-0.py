def add_two_numbers() -> int:
    message=input()
    a=[int(x) for x in message.split(",")]
    res=0
    for i in a:
        res+=i
    return res



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
