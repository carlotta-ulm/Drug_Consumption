import numpy as np
import pandas as pd


def process_data(path, path_to_save, userborder):
    '''Import datafram and process it so it can be used for modeling'''
    
    df = pd.read_excel(path)
    
    # Create drugs list and change classes to integers
    drugs = df.columns[13:]
    for d in drugs:
        df[drug] = df[drug].str.replace("CL", "").astype("int")
    
    # Binarize the Gender to male=1, female=0
    df.Gender = df.Gender.replace(0.48246, 0)
    df.Gender = df.Gender.replace(-0.48246, 1)
    df.Gender = df.Gender.astype(int)
    
    # Categorize age values into corresponding age-ranges
    age_conv = [(-0.95197, "18-24"), (-0.07854, "25-34"),  
                (0.49788, "35-44"), (1.09449, "45-54"), 
                (1.82213, "55-64"), (2.59171, "65+")]
    for t in age_conv:
        df.Age.replace(t[0], t[1], inplace=True)
     
    # Categorize Age, Education, Country and Ethnicity and
    # create Dummies variables for them
    df['Education'] = df['Education'].apply(education)
    
    df.Ethnicity = df.Ethnicity.apply(ethnicity_transform)
    
    df['Country'] = df['Country'].apply(country)
    
    drugs_bin = [drug + '_bin' for drug in drugs]
    
    df = df.merge(pd.get_dummies(df.Age, drop_first=True, prefix="age"),
                  left_index=True,right_index=True)
    df.drop("Age", axis=1, inplace=True)
    
    df = df.merge(pd.get_dummies(df.Education, drop_first=True, prefix="edu"), 
                  left_index=True, right_index=True)
    df.drop("Education", axis=1, inplace=True)
        
    df = df.merge(pd.get_dummies(df.Country, drop_first=True, prefix="country"), 
                  left_index=True, right_index=True)
    df.drop("Country", axis=1, inplace=True)  
    
    df = df.merge(pd.get_dummies(df.Ethnicity, drop_first=True, prefix="ethn"), 
                  left_index=True, right_index=True)
    df.drop("Ethnicity", axis=1, inplace=True)
    
    
    # Bin study participants into user, and non-user by seperating
    # them by given "border"
    for i in range(len(drugs)):
        df[drugs_bin[i]] = df[drugs[i]].apply(users, args=(userborder,))
        
    df.query("Semer == 0", inplace=True)
    df.drop("Semer", axis=1, inplace=True)
    df.drop("Semer_bin", axis=1, inplace=True)
    
    df.drop("ID", axis=1, inplace=True)
    
    
    return df
    
def education(e):
    if e == -2.43591:
        return 'before_16'
    elif e == -1.73790:
        return 'at_16'
    elif e == -1.43719:
        return 'at_17'
    elif e == -1.22751:
        return 'at_18'
    elif e == -0.61113:
        return 'some_college'
    elif e == -0.05921:
        return 'diploma'
    elif e == 0.45468:
        return 'university_degree'
    elif e == 1.16365:
        return 'masters_degree'
    else:
        return 'doctorate degree'

    
def ethnicity_transform(e):
    if e==-0.50212:
        return "asian"
    elif e==-1.10702:
        return "black"
    elif e==1.90725:
        return "black-asian"
    elif e==0.12600:
        return "white-asian"
    elif e==-0.22166:
        return "white-black"
    elif e==0.11440:
        return "other"
    elif e==-0.31685:
        return "white"
    
    
def country(c):
    if c == -0.09765:
        return 'australia'
    elif c == 0.24923:
        return 'canada'
    elif c == -0.46841:
        return 'new_zealand'
    elif c == -0.28519:
        return 'other'
    elif c == 0.21128:
        return 'republic_of_ireland'
    elif c == 0.96082:
        return 'uk'
    elif c == -0.57009:
        return 'usa'
    
def users(u, user_border):
    if u <= user_border:
        return 0
    else:
        return 1