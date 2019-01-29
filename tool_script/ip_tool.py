
def ip2int(ip):
    item_list = ip.split('.')
    x = 0
    for item in item_list:
        x = 256 * x + int(item)

    return x


def int2ip(integer):
    integer = int(integer)
    item_list = []
    while integer > 0:
        item_list.append(str(integer % 256))
        integer = integer / 256

    item_list.reverse()
    return '.'.join(item_list)


