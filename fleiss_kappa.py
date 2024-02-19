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

def fleiss_kappa(matrix_list, category):
    # Assuming matrix_category function correctly filters matrices by category
    #create a new matrix list
    new_matrix_list = [0] * len(matrix_list)
    for i in range(len(matrix_list)):
        new_matrix_list[i] = matrix_category(matrix_list[i], category)
    
    # Sum matrices entry by entry
    sum_matrix = np.sum(np.array(new_matrix_list), axis=0)
    
    # print("The sum matrix looks like this:")    
    # print(sum_matrix[:5])
    
    n = len(matrix_list)  # Number of raters
    N = sum_matrix.shape[0]  # Number of subjects
    k = sum_matrix.shape[1]  # Number of categories
    
    little_p = np.sum(sum_matrix, axis=0) / (N*n)  # Proportion of all ratings for each category
    
    # Calculate P_i for each item
    P= (np.sum(sum_matrix * (sum_matrix - 1), axis=1) / (n * (n - 1))).mean()
    #note that * is pointwise multiplication, and .mean() is the mean of the resulting array 
    
    # Calculate P_e (expected agreement by chance)
    P_c = np.sum(little_p ** 2)
    
    # Compute Fleiss' Kappa
    kappa = (P - P_c) / (1 - P_c)
    
    print(f"Fleiss' Kappa: {kappa}")
    return kappa

    
#TEST 
matrix_list = [matrix_1, matrix_2]
#create a list of categories and loop over them
categories = ["tone", "expertise", "encouraging", "respectful"] 
for category in categories:
    print(f"Category: {category}")
    fleiss_kappa(matrix_list, category)

