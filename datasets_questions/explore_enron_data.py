#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

with open("../final_project/final_project_dataset.pkl", "r") as f:
    enron_data = pickle.load(f)

print len(enron_data[enron_data.keys()[0]].keys())

pois = [k for k,v in enron_data.items() if v["poi"] == True]

print len(pois)

# print enron_data["PRENTICE JAMES"]['total_stock_value']

# print enron_data["COLWELL WESLEY"]['from_this_person_to_poi']

# print enron_data["SKILLING JEFFREY K"]['exercised_stock_options']

# print enron_data["LAY KENNETH L"]['total_payments']
# print enron_data["SKILLING JEFFREY K"]['total_payments']
# print enron_data["FASTOW ANDREW S"]['total_payments']

salaries = [k for k,v in enron_data.items() if v["salary"] != 'NaN']
print len(salaries)

email_addresses = [k for k,v in enron_data.items() if v["email_address"] != 'NaN']
print len(email_addresses)

total_payments_nan = [k for k,v in enron_data.items() if v["total_payments"] == 'NaN']

poi_total_payments = []
for k,v in enron_data.items():
    if v["poi"] == True:
        if v["total_payments"] == 'NaN':
            poi_total_payments.append(k)


print len(total_payments_nan)
print len(poi_total_payments)
print len(enron_data.keys())
