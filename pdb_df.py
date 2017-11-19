# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 18:08:16 2017

@author: kmeeh
"""
"""
Look through an excel file and locate all PDB ID'a
Use the ID's to find the sequence of each protein in the RCSB API database
"""
import pandas as pd
from urllib.request import urlopen
import urllib.error
import xml.etree.ElementTree as ET

#file = input("Enter Excel file name: ")

file = 'Flavin_database(01-05-11).xls'

df = pd.read_excel(file, sheet_name='total list', usecols = ['Enzyme', 'PDB'])

onlyid = df[['PDB']]

"""
Work on eliminating the loop
Multiple Structure ID's can be called by adding each id after a comma in the url.
i.e. http://www.rcsb.org/pdb/rest/customReport.xml?pdbids=1umf,1qfj,2a89&reportName=Sequence&service=wsfile&format=xml

Maybe access the PDB Series as a list or like a list.(?)

if strucid == tree.findall(.//VSequence.structureId).text
    find all VSequence.sequence under the same ID and make into list to append to the Data Frame 

"""
count = 1
while count <= 2:
    try:
        strucid = onlyid.loc[count, 'PDB']
        print("Number: ", count)
        print('Locating Structure ID: ', strucid)
        
        rcxburl = 'http://www.rcsb.org/pdb/rest/customReport.xml?pdbids='+ strucid + '&reportName=Sequence&service=wsfile&format=xml'
        
        data = urlopen(rcxburl).read()
        tree = ET.fromstring(data)
        
        firstseq = (tree.find('.//VSequence.sequence')).text
 
                
        print(lst)
                
    except urllib.error.HTTPError:
        None
    
    count += 1
