from funcionalitys import palete as pal, menu, __cleanup__ as clen,  __Error_Handle__
clen()
pal(True, "WellCome")

while (True):
    resp = menu()
    match resp:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 0:
            break
        case _:
            __Error_Handle__(True)
