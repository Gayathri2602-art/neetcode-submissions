from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    length=len(word)
    my_dict={}
    my_list=[] #["h","e","l","l","o"]
    for i in word:
        count=0
        my_list.append(i)
        for k in word: 
            if i ==k:
                count+=1
        my_dict[i]=count
    return my_dict
        





# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))