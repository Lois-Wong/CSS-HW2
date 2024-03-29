import pandas as pd
import numpy as np
from helper import matrix_rater_new, matrix_category_new


# TEST
rater_1_path= "data/Milton2.csv"
rater_1_name = "Milton"
matrix_1 = matrix_rater_new(rater_1_path, rater_1_name) 
print(matrix_1)

rater_2_path = "data/Lois2.csv"
rater_2_name = "Lois" 
matrix_2 = matrix_rater_new(rater_2_path, rater_2_name) 

rater_3_path = "data/Cole2.csv"
rater_3_name = "Cole" 
matrix_3 = matrix_rater_new(rater_3_path, rater_3_name) 


def fleiss_kappa(matrix_list, category):
    # Assuming matrix_category function correctly filters matrices by category
    #create a new matrix list
    new_matrix_list = [0] * len(matrix_list)
    for i in range(len(matrix_list)):
        new_matrix_list[i] = matrix_category_new(matrix_list[i], category)
    
    # Sum matrices entry by entry
    sum_matrix = np.sum(np.array(new_matrix_list), axis=0)
    
    # print("The sum matrix looks like this:")    
    # print(sum_matrix[:5])
    
    n = len(matrix_list)  # Number of raters
    N = sum_matrix.shape[0]  # Number of subjects
    k = sum_matrix.shape[1]  # Number of categories
    # Calculate "little p"  in wiki 
    little_p = np.sum(sum_matrix, axis=0) / (N*n)  # Proportion of all ratings for each category
    
     # Calculate big P in wikipedea, denoted P or each item
    P= (np.sum(sum_matrix * (sum_matrix - 1), axis=1) / (n * (n - 1))).mean()
    #note that * is pointwise multiplication, and .mean() is the mean of the resulting array 
    
    # Calculate P_c (expected agreement by chance)
    P_c = np.sum(little_p ** 2)
    
    # Compute Fleiss' Kappa
    kappa = (P - P_c) / (1 - P_c)
    
    print(f"Fleiss' Kappa: {kappa}")
    return kappa

    
#TEST 
matrix_list_123 = [matrix_1, matrix_2, matrix_3]
# we also conssider lists of two matrices from matrix_lsit_123
# we do a for loop to select two matrices from matrix_list_123 and construct matrix_list_ij for ij in 12 13 23 
matrix_list_12 = [matrix_1, matrix_2]
matrix_list_13 = [matrix_1, matrix_3]
matrix_list_23 = [matrix_2, matrix_3]
# we now combine all possible matrices into a list
matrix_combination = [matrix_list_123, matrix_list_12, matrix_list_13, matrix_list_23] 
    
#create a list of categories and loop over them
categories = ["tone", "expertise", "encouraging", "respectful"] 
a = 1 # to keep track of the matrix_list
for matrix_list in matrix_combination:
        # print(f"Matrix list: {matrix_list}")
    
    print("This matrix is in the " + str(a) + "th position in the matrix_combination list")
    for category in categories:
        print(f"Category: {category}")
        fleiss_kappa(matrix_list, category)
    a += 1

