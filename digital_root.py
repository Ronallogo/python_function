n = 10


def digital_root(n):
    copy_int = n
    while copy_int > 9 :
        copy_srt = str(copy_int)
        element = [ int(x) for x in copy_srt]
        copy_int = sum(element)
        

digital_root(n)