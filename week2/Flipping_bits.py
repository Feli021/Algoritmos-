def flippingBits(n):
    # Write your code here
    
    # Represents the number with 32 bits
    format(n & 0xFFFFFFFF, '032b')
    
    # Inverts all bits and converts it to an integer
    invertido = ~n & 0xFFFFFFFF
    return invertido
    
