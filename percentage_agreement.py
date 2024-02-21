
import pandas as pd
import numpy as np
from helper import matrix_rater, matrix_category 


# TEST
rater_1_path= "data/Milton.csv"
rater_1_name = "Milton"
matrix_1 = matrix_rater(rater_1_path, rater_1_name) 

rater_2_path = "data/Lois.csv"
rater_2_name = "Lois" 
matrix_2 = matrix_rater(rater_2_path, rater_2_name) 

rater_3_path = "data/cole.csv"
rater_3_name = "Cole" 
matrix_3 = matrix_rater(rater_3_path, rater_3_name) 

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

## we can extend this to any number of raters by using the following function
def percentage_agreement_multiple_raters(matrix_list, category):
    """INPUT: matrix_list is a list matrices for each rater , category is the category of the matrix
    OUTPUT: percentage agreement"""
    #initialize the count
    new_matrix_list = [0] * len(matrix_list)
    for i in range(len(matrix_list)):
        new_matrix_list[i] = matrix_category(matrix_list[i], category)
    
    count = 0
     #let k be the number of categories , this is the number of the columns of the matrix 
    k = new_matrix_list[0].shape[1]
    #let N be number of comments, this is the number of rows of the matrix 
    N = new_matrix_list[0].shape[0]
    #iterate through the matrix 
    for i in range(N):
        for j in range(k):
            if all(new_matrix_list[k][i][j] == new_matrix_list[k+1][i][j] for k in range(len(matrix_list)-1)):
                count += 1
    #compute the percentage agreement 
    percentage_agreement = count/(N*k)
    print("The percentage agreement between the raters is: " + str(percentage_agreement))
    return percentage_agreement

#Let us test this function 
# let us create a matrix list from matrix_1 and matrix_2


matrix_list_123 = [matrix_1, matrix_2, matrix_3]
# we also conssider lists of two matrices from matrix_lsit_123
# we do a for loop to select two matrices from matrix_list_123 and construct matrix_list_ij for ij in 12 13 23 
matrix_list_12 = [matrix_1, matrix_2]
matrix_list_13 = [matrix_1, matrix_3]
matrix_list_23 = [matrix_2, matrix_3]
# we now combine all possible matrices into a list
matrix_combination = [matrix_list_12, matrix_list_13, matrix_list_23] 
    
#create a list of categories and loop over them
categories = ["tone", "expertise", "encouraging", "respectful"] 
a = 1 # to keep track of the matrix_list
for matrix_list in matrix_combination:
        # print(f"Matrix list: {matrix_list}")
    
    print("This matrix is in the " + str(a) + "th position in the matrix_combination list")
    for category in categories:
        print(f"Category: {category}")
        percentage_agreement_multiple_raters(matrix_list,category)
    a += 1

