# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:41:53 2020

This is a test document for testing out the Intelligent Tagging API (RESTful)
    from Refinitive -> Open PermID

This one focuses on how to do entity lookups using OpenPermID.  Focusing on
    looking at three sources:
        PermID
        Yale
        IBM

@author: Levitannin
"""

from OpenPermID import OpenPermID

#   Cannot rename in the import call.
opid = OpenPermID()
#   API Initialization
opid.set_access_token("<API KEY HERE>")

#   The following is the format for looking up entity information via PermID.
#opid.lookup(id, format = 'dataframe', orient = 'row')
'''
This function will return a tuple containing a result and error string.

Parameter Name      Required               Description
    id                  yes     A query string to search for.
    format              no      Format of the output.  Possible values are:
                                    dataframe (default), json, or xml.
    orient              no      The format of the return dataframe, possible 
                                    values are row (default) or column.
'''

#   Sample looking up entity information at 1-5064690523 PermID, with all defaults
out1, err1 = opid.lookup("1-5064690523")
print(out1)

#   Call the lookup method to retrieve entity information with column parameter. (yale example)
out2, err2 = opid.lookup("1-5001419042", orient = "column")
print(out2)

#   Format the output of the retrieved information in json for IBM example
out3, err3 = opid.lookup("1-21475582828", format="json-ld")
print(out3)
