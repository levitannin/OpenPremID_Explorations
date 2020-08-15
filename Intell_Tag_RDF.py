# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:41:53 2020

This is a test document for testing out the Intelligent Tagging API (RESTful)
    from Refinitive -> Open PermID

This one focuses on how do intelligent tagging with OpenPermID.  Samples used
    below were pulled from Darknet Webscraping, per Ambly.

JSON format didn't work.  Looking into RDFlib, SPARQL Protocol and RDF Query 
    Langauge, 

@author: Levitannin
"""

from OpenPermID import OpenPermID
import rdflib
import json

#   Cannot rename in the import call.
opid = OpenPermID()
#   API Initialization
opid.set_access_token("<API KEY>")

#   The following is the format for passing text and intelligently tagging it using calais.
#opid.calais(text, language = 'English', contentType = 'raw', outputFormat = 'json')
'''
This function will return a tuple containing a result and error string.  Result
    could be a JSON, RDF, or N-Triples string depending on the output Format parameter.

Parameter Name      Required               Description
    text                yes     Content to be tagged.  Can be raw text, html, xml, or pdf.
    langauge            no      Identify the language of the text; currently possible are:
                                    English (default)
                                    Chinese
                                    French
                                    German
                                    Japanese
                                    Spanish
    contentType         no      Indicates the content type of the input text.
                                Possible values:
                                    raw (default)
                                    html
                                    xml
                                    pdf
    outputFormat        no      Defines the output response format.  Possibles:
                                    json (Default)
                                    rdf
                                    n3
'''
#   Handle and email removed from pulled text.
scrapedText = """
SamsungstoreSamsungstoreBuy original Samsung products from retailerwithout VAT and taxes!
develop free websiteWe are back!Important notice! 
We are ready to take your orders, delivery only within Europe! 
Smaller delays can happen during the shipment.Only original items
We order everything directly from Samsung wholesalers, you will receive only new, 
original, unopened productsFastFast, safe shipping currently to Europe only. 
Shipping takes 2-5 days. Shipping is free.
SecureWe are trusted sellers since 2013 on deepweb. 
We need only your name a delivery address.
PaymentWe accept any kind of cryptocurrency.
Escrow is accepted.
Best selling items**Only examples, we can order any other 
Samsung itemsProductPrice (in EUR)Galaxy S20 4G 128Gb539 -Galaxy S20 5G 
128Gb599 -Galaxy S20+ 5G 128gb659 -Galaxy S20 Ultra 5G 128gb799 -Galaxy Z Flip 
256gb889 -Galaxy Tab S6 Lite LTE 64Gb269 -Galaxy S10 4G 128Gb389 -Galaxy S10+ 
4G 128Gb449 -Galaxy S10e 4G 128Gb299 -Galaxy Note10+ 4G 256Gb629 -Galaxy Book 
S 256Gb659 Samsungstore - 2020
"""

#   json does not return necessary tagging space; i.e.: Social Tag.  Needed to
#       use rdf format which is rdf/xml format.
out1, err1 = opid.calais(scrapedText, outputFormat = "rdf")

#   This area is to test how to use the RDFlib to parse RDF file formats.
#create graph object    
graph = rdflib.Graph()

#parse graph
graph.parse(out1, format = 'xml')

#convert to a json file and write to "test.json"
graph.serialize("test.json", format = 'json-ld')

#open json file to pull things out of
with open("test.json", "r") as f:
  
    json_file = json.load(f)
    final_list = []
    #go through each top level json object
    #pull out the values we want
    for x in json_file:
        if x["@type"][0] == 'http://s.opencalais.com/1/type/tag/SocialTag':
            hash_value = x["http://s.opencalais.com/1/pred/socialtag"][0]["@id"] 
            text = x["http://s.opencalais.com/1/pred/name"][0]["@value"]
            final_list.append([hash_value, text]) 
