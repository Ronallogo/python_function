
n = 1234

def count_bits(n):
    result = []
    copy = n
    bitPositive = 0
    bitNegative = 0
    while copy > 0 :
        x = copy % 2
        if x > 0 : bitPositive+= 1
        else : bitNegative += 1
        copy //= 2
        result.append(x)
    result.reverse()
    print(result)
    print(f'bit positif = {bitPositive} et bit negattive = {bitNegative}')
    
        
  
count_bits(n)