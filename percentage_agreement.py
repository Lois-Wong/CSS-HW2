
import pandas as pd
import numpy as np
from helper import matrix_rater, matrix_category 


# TEST
rater_1_path= "/Users/miltonlin/Documents/GitHub/CSS-HW2/data/Milton.csv"
rater_1_name = "Milton"
matrix_1 = matrix_rater(rater_1_path, rater_1_name) 

rater_2_path = "/Users/miltonlin/Documents/GitHub/CSS-HW2/data/Lois.csv"
rater_2_name = "Lois" 
matrix_2 = matrix_rater(rater_2_path, rater_2_name) 


# we can first compute percentage agreement of the any number of raters
# this is given by checking each entry of the matrix and see if they are the same for all raters. 
# we will define this for two raters here 

def percentage_agreement(matrix_1, matrix_2): 
    """INPUT: matrix_1 and matrix_2 are the 40x14 matrices for rater 1 and rater 2 
    OUTPUT: percentage agreement"""
    #initialize the count
    count = 0
    #let k be the number of categories , this is the number of the columns of the matrix 
    k = matrix_1.shape[1]
    #let N be number of comments, this is the number of rows of the matrix 
    N = matrix_1.shape[0]
    #iterate through the matrix 
    for i in range(N):
        for j in range(k):
            if matrix_1[i][j] == matrix_2[i][j]:
                count += 1
    #compute the percentage agreement 
    percentage_agreement = count/(N*k)
    print("The percentage agreement between rater 1 and rater 2 is: " + str(percentage_agreement))
    return percentage_agreement

#TEST   
percentage_agreement(matrix_1, matrix_2) 

## we can extend this to any number of raters by using the following function
def percentage_agreement_multiple_raters(matrix_list):
    """INPUT: matrix_list is a list of 40x12 matrices for each rater 
    OUTPUT: percentage agreement"""
    #initialize the count
    count = 0
     #let k be the number of categories , this is the number of the columns of the matrix 
    k = matrix_1.shape[1]
    #let N be number of comments, this is the number of rows of the matrix 
    N = matrix_1.shape[0]
    #iterate through the matrix 
    for i in range(N):
        for j in range(k):
            if all(matrix_list[k][i][j] == matrix_list[k+1][i][j] for k in range(len(matrix_list)-1)):
                count += 1
    #compute the percentage agreement 
    percentage_agreement = count/(N*k)
    print("The percentage agreement between the raters is: " + str(percentage_agreement))
    return percentage_agreement

#Let us test this function 
# let us create a matrix list from matrix_1 and matrix_2
matrix_list = [matrix_1, matrix_2] 
percentage_agreement_multiple_raters(matrix_list) 

