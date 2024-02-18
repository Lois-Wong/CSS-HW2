import pandas as pd
import numpy as np

"""we first create a matrix for each rater, where the rows are the 40 comments and the columns are the 12 categories
we have 5 tones, 3 expertise, 2 encouraging, 2 respectful 
the 5 tones are Strongly Negative, Negative, Neutral, Positive, Strongly Positive
the three expertise are No Degree, STEM Degree, Non-STEM Degree
the two encouraging are Discouraging, Encouraging
the two respectful are Disrespectful, Respectful """




def matrix_rater(path_of_rater, rater):
    """INPUT: path_of_rater: the path of the csv file of the rater , name of rater, rater 
    OUTPUT: matrix: a 40x12 matrix filled with zeros, where the rows are the 40 comments and the columns are the 12 categories"""
    
    # Read the CSV file; pandas automatically skips the header
    data = pd.read_csv(path_of_rater)
    # Create a 40x12 matrix filled with zeros
    matrix = np.zeros((40, 12))
    # Iterate over rows of the dataset
    for i, row in data.iterrows():
        # Ensure we do not go beyond the first 40 entries
        if i >= 40:
            break
        
        #we have 5 tones, 3 expertise, 2 encouraging, 2 respectful 
        # the 5 tones are Strongly Negative, Negative, Neutral, Positive, Strongly Positive
        tone = row['tone']
        if tone == "Strongly Negative":
            matrix[i][0] += 1
        elif tone == "Negative":
            matrix[i][1] += 1
        elif tone == "Neutral":
            matrix[i][2] += 1  
        elif tone == "Positive":
            matrix[i][3] += 1
        elif tone == "Strongly Positive":
            matrix[i][4] += 1
        
        
        expertise = row['expertise']
        if expertise == "No Degree":
            matrix[i][5] += 1
        elif expertise == "STEM Degree":
            matrix[i][6] += 1
        elif expertise == "Non-STEM Degree":
            matrix[i][7] += 1
        
        encouraging = row['encouraging']
        if encouraging == "Discouraging":
            matrix[i][8] += 1
        elif encouraging == "Encouraging":
            matrix[i][9] += 1
        
        respectful = row['respectful']
        if respectful == "Disrespectful":
            matrix[i][10] += 1
        elif respectful == "Respectful":
            matrix[i][11] += 1
    
    # Notification that the matrix creation is complete
    print("The matrix for rater " + rater + " is created")
    #see the first few rows 
    print("The first few rows of the matrix looks like this: ") 
    print(matrix[:5]) 
    return matrix

# TEST
rater_1_path= "/Users/miltonlin/Documents/GitHub/CSS-HW2/Milton.csv"
rater_1_name = "Milton"
matrix_1 = matrix_rater(rater_1_path, rater_1_name) 
rater_2_path = "/Users/miltonlin/Documents/GitHub/CSS-HW2/Lois.csv"
rater_2_name = "Lois" 
matrix_2 = matrix_rater(rater_2_path, rater_2_name) 
