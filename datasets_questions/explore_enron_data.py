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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
count=0
poi=["LAY KENNETH",
"SKILLING JEFFREY",
"HOWARD KEVIN",
"KRAUTZ MICHAEL",
"YEAGER SCOTT",
"HIRKO JOSEPH",
"SHELBY REX",
"BERMINGHAM DAVID",
"DARBY GILES",
"MULGREW GARY",
"BAYLEY DANIEL",
"BROWN JAMES",
"FURST ROBERT",
"FUHS WILLIAM",
"CAUSEY RICHARD",
"CALGER CHRISTOPHER",
"DESPAIN TIMOTHY",
"HANNON KEVIN",
"KOENIG MARK",
"FORNEY JOHN",
"RICE KENNETH",
"RIEKER PAULA",
"FASTOW LEA",
"FASTOW ANDREW",
"DELAINEY DAVID",
"GLISAN BEN",
"RICHTER JEFFREY",
"LAWYER LARRY",
"BELDEN TIMOTHY",
"KOPPER MICHAEL",
"DUNCAN DAVID",
"BOWEN RAYMOND",
"COLWELL WESLEY",
"BOYLE DAN",
"LOEHR CHRISTOPHER"]


qs=0
e=0
for o in enron_data:
  #  print(enron_data[o]['total_stock_value'])
    if enron_data[o]['total_stock_value'] == "NaN":
        qs = qs+1
    if enron_data[o]['email_address'] != 'NaN':
        e=e+1

print ("Quantified Salary: ", qs)
print ("Known email adrdresses: ",e)
print(len(enron_data))
print(qs/len(enron_data)*100)
#print(len (enron_data["SKILLING JEFFREY K"]))
#print(enron_data["SKILLING JEFFREY K"]["total_payments"])
