# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:41:53 2020

This is a test document for testing out the Intelligent Tagging API (RESTful)
    from Refinitive -> Open PermID

This one focuses on how to search using OpenPermID.  Focusing on looking at
    three sources:
        DarkOwl
        Yale
        IBM

@author: Levitannin
"""

from OpenPermID import OpenPermID
import json

#   Cannot rename in the import call.
opid = OpenPermID()
#   API Initialization
opid.set_access_token("<Add API Key>")

#   A function for searching an entity's PermID value from a String
#opid.search(q, entityType = 'all', format = "dataframe", start = 1, num = 5,order = 'rel')
'''
This function will return a tuple containing a result and error string.

Parameter Name      Required               Description
    q                   yes     A query string to search for.
    entityType          no      Type of entity to search for.  Possibilities are:
                                    all (default), organization, instrument, or quote
    format              no      Format of the output.  Possible values are:
                                    dataframe (default), json, or xml.
    start               no      Index of the first result returned, in the list
                                    of results ordered according to the order
                                    parameter.  Index is 1-based; default 1.
    num                 no      Maximum number of results returned to each entity
                                    (separately).  Possibilities are 5, 10, 20,
                                    50, and 100.
    order               no      Order of the search results.  Possible values:
                                    rel (relevance) -- default
                                    az  (ascending alpha)
                                    za  (descending alpha)
'''
#   Pull then individually print out entity types.
out1, err1 = opid.search('DarkOwl')
print(out1['quotes'])
print(out1['organizations'])
print(out1['instruments'])

#   Pull and print out organization focused information.
out2, err2 = opid.search('Yale', entityType = 'organization', num = 10)
print(out2)

#   Pull and print out json format of the data.
out3, err3 = opid.search('IBM', entityType = 'quote', format = 'json')
parsed = json.loads(out3)
print(json.dumps(parsed, indent = 4))
