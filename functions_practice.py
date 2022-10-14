def hello():
    print("Hello")

def pack(x, y, z):
    return[x, y, z]

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        for item in range(0, len(list)):
            if item == 0:
                print(f"First I eat {list[item]}")
            else:
                print(f"Next I eat {list[item]}")

hello()
print(pack("a", "b", "c"))
eat_lunch(["bread", "egg"])