# helper.py
import pandas as pd
import numpy as np



"""we first create a matrix for each rater, where the rows are the 40 comments and the columns are the 12 categories
we have 6 tones, 3 expertise, 2 encouraging, 3 respectful 
the 6 tones are Strongly Negative, Negative, Neutral, Positive, Strongly Positive, None
the 3 expertise are No Degree, STEM Degree, Non-STEM Degree
the 2 encouraging are Discouraging, Encouraging
the 3 respectful are Disrespectful, Respectful, Neutral """




def matrix_rater(path_of_rater, rater):
    data = pd.read_csv(path_of_rater)
    matrix = np.zeros((40, 14))  # 40 comments, 14 categories (6 tones, 3 expertise, 2 encouraging, 3 respectful)
    
    for i, row in data.iterrows():
        if i >= 40:
            break
        
        tone = row['tone']
        expertise = row['expertise']
        encouraging = row['encouraging']
        respectful = row['respectful']
        
        # Tone
        if tone == "Strongly Negative": matrix[i][0] += 1
        elif tone == "Negative": matrix[i][1] += 1
        elif tone == "Neutral": matrix[i][2] += 1
        elif tone == "Positive": matrix[i][3] += 1
        elif tone == "Strongly Positive": matrix[i][4] += 1
        elif pd.isna(tone) or tone == "None":
            matrix[i][5] += 1
            # print(f"Dataset: {path_of_rater}, Row: {i}, Tone: None")
        #in one of my dadtasets I hada "None" subcategory in Tone 
        #I would like to single out a line of code that would also print out the dataset name and the row number of the "None" subcategory
        
        
        # Expertise
        if expertise == "No Degree": matrix[i][6] += 1
        elif expertise == "STEM degree": matrix[i][7] += 1
        elif expertise == "Non-STEM degree": matrix[i][8] += 1
        
        # Encouraging
        if encouraging == "Discouraging": matrix[i][9] += 1
        elif encouraging == "Encouraging": matrix[i][10] += 1
        
        # Respectful 
        if respectful == "Disrespectful": matrix[i][11] += 1
        elif respectful == "Respectful": matrix[i][12] += 1
        elif respectful == "Neutral": matrix[i][13] += 1  
    
    # print(f"The matrix for rater {rater} is created")
    # print("The first few rows of the matrix looks like this:")
    # print(matrix[:9])
    #we can check if we have the correct matrix by summing along each rows
    #each rows should sum to 4 since there are 4 categories for each comment 
    # we create a new matrix of the sums along the rows
    # sum_matrix = np.sum(matrix, axis = 1)
    # print("The sum matrix looks like this:")
    # print(sum_matrix)
    # # this is of shape 
    # print("The shape of the sum matrix is: " + str(sum_matrix.shape))
    
    return matrix


# as we do Feliss Kappa, we restrict our attention to a particular category
# we will define a new function that takes in the matrix and the category and returns a new matrix with the category 

def matrix_category(matrix, category):
    if category == "tone":
        new_matrix = matrix[:, :6]  
    elif category == "expertise":
        new_matrix = matrix[:, 6:9] 
    elif category == "encouraging":
        new_matrix = matrix[:, 9:11]  
    elif category == "respectful":
        new_matrix = matrix[:, 11:14]  
    else:
        print("Invalid category")
        return None
    return new_matrix