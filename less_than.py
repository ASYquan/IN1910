
def less_than(original,n):
    lst = [i for i in original if i<n ]
    return lst

original = [1,2,3,4,5]

for n in range(5):
    if len(less_than(original,n)) == 0:
        print("tom")
    else:
        print(f"Liste av tall som er mindre enn {n}: {less_than(original, n)}")
