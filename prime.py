def prime(num):
    i = 2
    listofnumbers = [1]
    # Find the prime numbers in the range of num
    if isinstance(num, int): # check if num is an integer
        if num > 0: # check if num is a positive integer
            for x in range(1, num + 1): # choose x between 1 and num
                while i <= x:
                    quotient = x / i
                    remainder = x // i
                    if quotient == remainder:
                        listofnumbers = listofnumbers.append('x')
                    i = i + 1
    return num_list
                
                
                
                
    
            
        
