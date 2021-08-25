
def count_chars(string):
    string = string.lower()
    count = 0
    dict = {"count": count}
    for x in string:
        if x == " ":
            count +=0
        else:
            count +=1
            dict.update({"count": count})
    return dict


example = "Hello, world!"
for char, count in count_chars(example).items():
    print(f'{char:3}{count:10}')
    sortStr = "".join(sorted(example.lower()))
print(sortStr)

ex2 = "YOLO"
print(sorted(ex2,key=ex2.count,reverse=True))



 






