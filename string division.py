def devideString(string,n):
    size = len(string)
    if size%n != 0:
        return
    part_size = string/n
    k = 0
    for i in string:
        if k%part_size == 0:
            print("\n"),
        print(i),
        k += 1
string = "praveen"
devideString(string,5)
