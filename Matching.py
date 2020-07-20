# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:41:53 2020

This is a test document for testing out the Intelligent Tagging API (RESTful)
    from Refinitive -> Open PermID

This one focuses on how to do record matching using OpenPermID.  Focusing on
    looking at two types:
      organizations
      persons

@author: Levitannin
"""

from OpenPermID import OpenPermID
import pandas as pd

#   Cannot rename in the import call.
opid = OpenPermID()
#   API Initialization
opid.set_access_token("<API KEY HERE>")

#   The following is the format for record matching, where a person, 
#       organization, instrument, or quote can be matched.
#opid.match(data, dataType = 'Organization', numberOfMatchesPerRecord = 1, raw_output = False)
'''
This function will return a tuple containing a result and error string.

Parameter Name      Required               Description
    yes                 yes     A CSV string or dataframe for matching.
    dataType            no      Type of entitty to search for.  Possible values:
                                    Person
                                    Organization (Default)
                                    Instrument
                                    Quotation
    numberOfMatchesPerRecord
                        no      Number of possible matches to output for each 
                                    record in the input.  Maximum is 5.  
                                    Default is 1.
    raw_output          no      Boolean value set to retrieve a result as a 
                                    JSON string instead of dataframe.
'''

#   Sample of data on organization for matching:
organization = """
LocalID,Standard Identifier,Name,Country,Street,City,PostalCode,State,Website
1,,Apple,US,"Apple Campus, 1 Infinite Loop",Cupertino,95014,California,
2,,Apple,,,,,,
3,,Teva Pharmaceutical Industries Ltd,IL,,Petah Tikva,,,
4,,Tata Sky,IN,,,,,
5,RIC:IBM.N|Ticker:IBM,,,,,,,
6,Ticker:MSFT,,,,,,,
7,LEI:INR2EJN1ERAN0W5ZP974,,,,,,,
8,Ticker:FB&&Exchange:NSM,,,,,,,
9,Ticker:AAPL&&MIC:XNGS,,,,,,,
"""
#   Default match call.
out1, err1 = opid.match(organization)
print(out1)

#   Add persons to the columns of the p dataframe above.
person = pd.DataFrame(columns = ['LocalID',
                                 'FirstName',
                                 'MiddleName',
                                 'PreferredName',
                                 'LastName',
                                 'CompanyPermID',
                                 'CompanyName',
                                 'NamePrefix',
                                 'NameSuffix'])

#   Adding a person to the person dataframe as outlined by the columns above:
person = person.append(pd.Series(['1','Satya','','','Nadella','','Microsoft Corp','',''], 
                                 index = person.columns), ignore_index = True)
person = person.append(pd.Series(['2','Satya','','','Nadella','4295907168','','',''], 
                                 index = person.columns), ignore_index = True)
person = person.append(pd.Series(['3','Martin','','','Jetter','','International Business Machines Corp','',''], 
                                 index = person.columns), ignore_index = True)
person = person.append(pd.Series(['4','Bill','','','Gates','','Microsoft Corp','',''], 
                                 index = person.columns), ignore_index = True)

out2, err2 = opid.match(person, dataType='Person')
print(out2)

#   Creation of quotation data for matching
quotation="""
LocalID,Standard Identifier
1,RIC:IBM.N|Ticker:IBM
2,Ticker:MSFT
3,RIC:IBM.N&&Ticker:IBM
"""
out3, err3 = opid.match(quotation, dataType = 'Quotation', raw_output = True)
print(out3)
