#!/usr/bin/python

import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    e10 = np.percentile(np.array(predictions - net_worths), 90)
    for p, a, n in zip(predictions, ages, net_worths):
        if p - n <= e10:
            cleaned_data.append((a, n, p - n))
    
    return cleaned_data



    
# import pickle
# ages = pickle.load( open("practice_outliers_ages.pkl", "r") )
# net_worths = pickle.load( open("practice_outliers_net_worths.pkl", "r") )

# ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
# net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))

# from sklearn.cross_validation import train_test_split
# ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths, test_size=0.1, random_state=42)

# from sklearn.linear_model import LinearRegression

# reg = LinearRegression()
# reg.fit(ages_train, net_worths_train)


# predictions = reg.predict(ages_train)
# cleaned_data = outlierCleaner(predictions, ages_train, net_worths_train )

# print len(cleaned_data) 

