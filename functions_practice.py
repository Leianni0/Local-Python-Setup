def hello():
    print("Hello! Welcome!")

def pack(sandwhich, chips, cookie):
    return [sandwhich, chips, cookie]

def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        print("First I eat", lunch_items[0])
        for item in lunch_items[1:]:
            print("Next I eat", item)

hello()
packed_lunch = pack("sandwich", "chips", "cookie")
eat_lunch(packed_lunch)
