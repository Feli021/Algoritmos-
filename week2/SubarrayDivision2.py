# Two children, Lily and Ron, want to share a chocolate bar. The bar consists of squares, and each square has an integer value on it.

#Lily wants to give Ron a contiguous segment of the chocolate bar that satisfies the following conditions:

#The length of the segment is equal to Ron’s birth month.

#The sum of the integers in the segment is equal to Ron’s birth day.

#Your task is to determine how many different ways Lily can choose such a segment.



def birthday(s, d, m):
    # 's' is the list of integers 
    # 'd' is the target sum 
    # 'm' is the number of elements in the segment     

    numeros = s 

    somas = []  

    # Loop through all possible starting points for a segment of length 'm'
    for i in range(len(numeros) - m + 1):
        grupo = numeros[i:i+m]  # Get a contiguous segment of length 'm'
        soma_grupo = sum(grupo)  # Calculate the sum of the segment

        if soma_grupo == d:  # Check if the segment sum equals the birth day
            somas.append(soma_grupo)  # Store it if it matches

    return len(somas)  # Return the count of valid segments
