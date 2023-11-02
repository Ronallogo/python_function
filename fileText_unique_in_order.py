sequence = ['l', 'l', 'l', 'l', 'R', 'R', 'r', 'k', 'k', 'k', 'k', 'W', 'W', 'f', 'f', 'f',
            'f', 'f', 'h', 'h', 'I', 'I', 'I', 'I', 'U', 'U', 'U', 'U', 'A', 'h', 'h', 'h', 'F', 'F', 'F',
            'F', 'F', 'r', 'X', 'X', 'X', 'X', 'g', 'g', 'g', 'g', 'L', 'L', 'L', 'L', 'L', 'e', 'e', 'e', 'e',
            'Q', 'Q', 'Q', 'H', 'H', 'H', 'n', 'p', 'p', 'p', 'N', 'N', 'N', 'B', 'B', 'B', 'B', 'B', 'R', 'X', 'X',
            'K', 'W', 'W', 'W', 'W', 'W', 'z', 'z', 'W', 'Q', 'Q', 'Q', 'J', 'J', 'J', 'J', 'S', 'S', 'S', 'S', 'S',
            'J', 'J', 'J', 'J', 'Z', 'Z', 'Z', 'Z', 'Z', 'J', 'J', 'J', 'x', 'J', 'J', 'N', 'N', 'N', 'a', 'a', 'p', 'p', 
            'p', 'p', 'p', 'b', 'b', 'Q', 'Q', 'Z', 'Z', 'Z', 'Z', 'T', 'T', 'T', 'Z', 'Z', 'p', 'p', 'p', 'Q', 'Q',
            'Q', 'Q', 'Q', 'H', 'H', 'H', 'H', 'H', 'h', 'h', 'h', 'h', 'h']
def unique_in_order(sequence):
    copy =  [x for x in sequence[1:]]
    result = []
    for k ,  x in enumerate(sequence) :
        for l ,  y in enumerate(copy) :
            if x != y  and  k == l:
                result.append(x)  
        if k == len(sequence) - 1 :
            result.append(x)   
    print(result)
    return result

y = unique_in_order(sequence)
                
    
    
x =  ['l', 'R', 'r', 'k', 'W', 'f', 'h', 'I', 'U', 
    'A', 'h', 'F', 'r', 'X', 'g', 'L', 'e', 'Q', 
  'H', 'n', 'p', 'N', 'B', 'R', 'X', 'K', 'W', 'z', 'W', 'Q', 
  'J', 'S', 'J', 'Z', 'J', 'x', 'J', 'N', 'a',
  'p', 'b', 'Q', 'Z', 'T', 'Z', 'p', 'Q', 'H', 'h']  
    
if x == y :
    print("VALABLE")
else:
    print("NON - VALABLE")
    dif = [a for a in y if a not in x]
    print("la difference est : " , dif)