def inp():
    num_cus = int(input())
    lst_maps = []
    while num_cus != 0:
        map = {}
        for i in range(num_cus):
            line = input()
            lst = line.split(" ")
            for ele in lst[1::]:
                map.setdefault(ele, []).append(lst[0])
        lst_maps.append(map)
        num_cus = int(input())
    return lst_maps


def main():
    lst_maps = inp()
    for map_dict in lst_maps:
        dict_items = list(map_dict.items())
        dict_items.sort(key=lambda x: x[0])
        for items in dict_items:
            s = ""
            s += str(items[0]) + " "
            names = items[1]
            for name in sorted(names):
                s += name + " "
            print(s)
        print()
main()
