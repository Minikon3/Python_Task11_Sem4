def main(x):
    match x[4]:
        case 1975:
            match x[1]:
                case 1992:
                    return 9
                case 1961:
                    return 10
        case 1977:
            match x[2]:
                case 'GAMS':
                    match x[0]:
                        case 'PHP':
                            return 8
                        case 'KICAD':
                            match x[3]:
                                case 1971:
                                    return 7
                                case 2018:
                                    return 6
                                case 1973:
                                    return 5
                case 'SWIFT':
                    match x[0]:
                        case 'PHP':
                            match x[1]:
                                case 1961:
                                    return 4
                                case 1992:
                                    return 3
                        case 'KICAD':
                            match x[3]:
                                case 1971:
                                    return 2
                                case 2018:
                                    return 1
                                case 1973:
                                    return 0

print(main(['KICAD', 1961, 'GAMS', 1971, 1977]))