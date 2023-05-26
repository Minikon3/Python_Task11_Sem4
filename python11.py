from struct import *


def main(*args):
    s = args[0]
    d = {}
    a = unpack_from('<5sIibdQiQiIIIHQ', s)
    d['A1'] = {}
    b = unpack_from('<fHBHHIqH', s, a[1])
    d['A1']['B1'] = b[0]
    c = unpack_from('<Id', s, b[1])
    dd = unpack_from('<IHQ', s, c[0])
    d['A1']['B2'] = {'C1': {
        'D1': list(unpack_from('<' + 'B' * dd[0], s, dd[1])),
        'D2': dd[2]
    }, 'C2': c[1]}
    d['A1']['B3'] = b[2]
    d['A1']['B4'] = b[3]
    d['A1']['B5'] = list(unpack_from('<' + 'd' * b[4], s, b[5]))
    d['A1']['B6'] = b[6]
    d['A1']['B7'] = b[7]
    d['A2'] = a[2]
    d['A3'] = a[3]
    d['A4'] = a[4]
    d['A5'] = [{'E1': a[5 + i], 'E2': a[6 + i]} for i in range(0, 4, 2)]
    d['A6'] = list(unpack_from('<' + 'I' * a[9], s, a[10]))
    d['A7'] = list(unpack_from('<' + 'h' * a[11], s, a[12]))
    d['A8'] = a[13]
    return d


print(main((b'LUUBCr\x00\x00\x00%2\xcd\x98%t\xddI/+\x0e\xd1?\xefi\x83`\xd5\xec'
            b'\xed$\x1b\x88k\x81\xd4\x05\x8bL?\x06\xda\xb4\xa6\\\xb4u\x02\x00'
            b'\x00\x00\x8b\x00\x00\x00\x04\x00\x00\x00\x93\x00c\xf3\x83\xe4\xc7\x89v9'
            b'\xb1\xd5\x1d\x02\x04\x00\x00\x00D\x00\x0c5\x0eb\x8b?_\xa7H\x00'
            b"\x00\x00\xf4\x08'0\x92&\xed\xbf\xfe\x04\xbb\xab \x15\xe4?`VB\x8c\xf4\xe2"
            b'\xaa?p6\x16?V\x00\xa5\x90\xd9\x02\x00b\x00\x00\x00\xea\x1d\x02'
            b'\xf5\x9a\xeb\xfc\xa6\xb7\x95b\x89\xfeu7\xe1\xd0\x1f\\\xd7\xf1\xd4\xdc5%\x1c')))
