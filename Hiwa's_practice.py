'''
this program developed by
Mohammad Rasoul Azizi (AMR Hiwa)
November 2022
'''
# called the numpy package
import numpy as np

# define a function to create a bandad matrix with a
#        special dimantion and random elements
def banded_matrix() -> np.array:

    # getting dimantion from user
    dimension = int(input("Enter your dimension : "))
    
    # create a eye unit matrix
    A = np.eye(dimension)
    
    # choose a random number from [0, dimension//2] for bandwidth up and show it.
    bandwith_up = np.random.randint(1, dimension//2)
    print("bandwith up : ", bandwith_up)

    # choose a random number from [0, dimension//2] for bandwidth down and show it.
    bandwith_down = np.random.randint(1, dimension//2)
    print("bandwith down : ", bandwith_down)

    # set random values for main diameter
    A += np.diag(np.random.randint(1, 9, dimension))

    # condition for checking that bandwidth up is zero or not
    # if bandwidth is not zero , change the diameters by random elements
    if bandwith_up != 0:
        for i in range(1, bandwith_up + 1):
            # This command replaces a list with random elements of diameter n greater than the original diameter
            A += np.diag(np.random.randint(1, 9, dimension-i), i)

    # condition for checking that bandwidth up is zero or not
    # if bandwidth is not zero , change the diameters by random elements
    if bandwith_down != 0:
        for i in range(1, bandwith_down + 1):
            # this command replace a list with random elements with n diameter below main diameter
            A += np.diag(np.random.randint(1, 9, dimension-i), -i)

    # return the our matrix, dimension, bandwidth up, bandwidth down to main program
    return A, dimension, bandwith_up, bandwith_down

# here we define a function to transform a bandad matrix to band storage gaxpy
def band_storage_gaxpy(A: np.array, dimension: int, bandwidth_up:int, bandwidth_down:int) -> np.array:

    # we need to know about many of non-zero diameter of bandad matrix
    ls = range(-bandwidth_down, bandwidth_up+1)
    
    # for knowing about nonezero diameter we show them
    print(f"list of nonzero diameter: {list(ls)}")

    # we make a empty list to storage non-zero diameters  
    diameters_list = []

    # We create a circle with non-zero diameters to specify its members
    for count in ls:

        # now we must to storage elements
        temp = [None] * dimension

        # We create a nested loop to compare the representations inside the matrix
        for i in range(dimension):
            for j in range(dimension):
                if j == i + count:
                    temp[i] = A[i][j]

        # Finally, we add all the regions of each non-zero diameter as a row into a list
        diameters_list.append(temp)
    
    # send a final result to the main program body
    return diameters_list

# the all data that we need them calculate with banded_matrix method and storage them in many Variable
the_matrix, dimension, bandwidth_up, bandwidth_down = banded_matrix()

# show the first bandad matrix that the computer made it
print(f"\nfirst matrix is :\n\n{the_matrix}\n")

# getting the all non-zero diameter of our banded matrix by 'band_storage_gaxpy' method
list_of_diameter = band_storage_gaxpy(the_matrix, dimension, bandwidth_up, bandwidth_down)

# create a matrix with all non-zero diameter that we got
bsg_matrix = np.array(list_of_diameter[::-1])

# show the final result
print(f"\nThe our band storage gaxpy is : \n\n{bsg_matrix}")

