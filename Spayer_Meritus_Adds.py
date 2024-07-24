# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:56:57 2022

@author: GSantwani
"""

import pandas as pd
import time
import pyodbc
import numpy as np
from datetime import datetime
from pytz import timezone
#from string import strip

#GET USER OF WHO EXECUTED THE CODE
start = datetime.now(timezone('US/Eastern'))

filename = r"C:\Users\NKar\OneDrive - Evolent Health, Inc\Documents\Roaster load_August_2023\Meritus - 135570\Meritus_Adds.csv"
   
yyyymmdd = time.strftime('%Y%m%d')

print('Running Conversion Query for Meritus Roster')

#df = pd.read_excel(filename,sheet_name = 'Adds')
df = pd.read_csv(filename,keep_default_na=False,low_memory=False, dtype=str)

# columns that dont change
df.rename(columns={'Indiv. NPI#':'Provider NPI 1', 'Last Name':'Last Name',  'First Name':'First Name'}, inplace=True)
df.rename(columns={'M I ':'M I ', 'Degree': 'Degree', 'Gender': 'Gender','SOC SEC #':'SOC SEC #'}, inplace=True)
df.rename(columns={'Birth Date':'Birth Date','Ethnicity': 'Ethnicity','Languages':'Language Spoken','Eprep Enrolled (Y=Yes/ N=No)':'ePrep Enrolled'}, inplace=True)
df.rename(columns={'Medical Lic #':'Medical License Number','STATE':'Medical License State','Expiration Date':'Medical License Expiration Date'}, inplace=True)
df.rename(columns={'DEA #':'DEA License Number', 'DEA Exp': 'DEA License Expiration Date', 'CDS #': 'CSR License Number','CDS STATE':'CSR License State','CDS Exp':'CSR License Expiration Date'}, inplace=True)
df.rename(columns={'Taxonomy Code': 'Taxonomy Code','Speciality/Sub-Speciality':'Specialty Description'}, inplace=True)
df.rename(columns={'Board Cert.': 'Board Name','Exp Date':'Expiration Date','Lifetime Bd Certification':'Lifetime Board Cert'}, inplace=True)
df.rename(columns={' Hosp Affil':'Hospital Name','Admitting Privileges':'Admitting Privs','Delegate Committee Approval Date':'Initial Cred Date'}, inplace=True)
df.rename(columns={'Medical School':'Institution Name ','Grad Date':'End Date'}, inplace=True)
df.rename(columns={'Medicaid #':'MEDICAID ID','Medicare #':'MEDICARE ID'}, inplace=True)
df.rename(columns={'PCP/Specialist':'PCP/Specialist/Hospitalist'},inplace=True)



if [df['Residency/Fellowship Date'].isnull() == True]:
    df['Start Date-Residency'] = ''
    df['End Date-Residency'] = ''
else:
    df[['Start Date-Residency', 'End Date-Residency']] = df['Residency/Fellowship Date'].str.split('-',expand  = True)

if [df['Residency/Fellowship Date'].isnull() == True]:
    df['Start Date-Fellowship'] = ''
    df['End Date-Fellowship'] = ''
else:
    df[['Start Date-Fellowship', 'End Date-Fellowship']] = df['Residency/Fellowship Date'].str.split('-',expand  = True)


#add in blank columns
df['Medical License Issued Date']=''
df['Provider type']=''
df['DEA License State']=''
df['DEA License Issued Date']=''
df['CSR License Issued Date']=''
df['Board Specialty']=''
df['Issue Date']=''
df['Start Date']=''
df['Hosp_End_Date']=''
df['Initial/Recred Cycle']=''
df['Last Cred Approval Date']=''
df['Next Recred Due Date']=''
df['Delegated Group Entity Name']='Meritus Health'
df['Education Type']=''
df['Start Date ']=''
df['Speciality Type']=''
df['Medicaid Issuing state'] = ''
df['Medicare Issuing state'] = ''
df['Board Certification Status (Y/N)'] = ''
df['Institution Name-Intership'] = ''
df['Start Date-Internship'] = ''
df['End Date-Internship'] = ''
df['Institution Name-Residency'] = df['Residency/Fellowship']
df['Institution Name-Fellowship'] = df['Residency/Fellowship']
df['Speciality Type-Internship'] = ''
df['Speciality Type-Residency']=''
df['Speciality Type-Fellowship']=''
df['ECFMG']=''


#reorder columns
df = df[['Provider NPI 1','Last Name','First Name','M I ','Degree','Gender','SOC SEC #','Birth Date','Ethnicity','Language Spoken','ePrep Enrolled','Medical License Number','Medical License State',
'Medical License Issued Date','Medical License Expiration Date','Provider type','DEA License Number','DEA License State','DEA License Issued Date','DEA License Expiration Date','CSR License Number',
'CSR License State','CSR License Issued Date','CSR License Expiration Date','Taxonomy Code','Specialty Description','Board Name','Board Specialty','Issue Date','Expiration Date',
'Lifetime Board Cert','Hospital Name','Start Date','Hosp_End_Date','Admitting Privs','Initial/Recred Cycle','Initial Cred Date','Last Cred Approval Date','Next Recred Due Date',
'Delegated Group Entity Name','Education Type','Institution Name ','Start Date ','End Date','Speciality Type','MEDICARE ID','Medicare Issuing state','MEDICAID ID','Medicaid Issuing state','PCP/Specialist/Hospitalist','Board Certification Status (Y/N)','Institution Name-Intership','Start Date-Internship','End Date-Internship','Speciality Type-Internship',
'Institution Name-Residency','Start Date-Residency','End Date-Residency','Speciality Type-Residency','Institution Name-Fellowship','Start Date-Fellowship','End Date-Fellowship',
'Speciality Type-Fellowship','ECFMG']]


print('''Conversion is in progress;
      'Do not close the program!''')


#df = df.fillna('')
#df.to_csv('test.csv',index=False)

df_mapped = df.replace('N/A','')

#df12 = pd.read_csv(r'D:\Users\GSantwani\Desktop\MPMD Monthly Deegated Rosters\UMCMG\Python Queries\test20221115_spayer.csv',keep_default_na=False,low_memory=False, dtype=str)

print('''Fetching Data from crosswalk;
      'Do not close the program!''')

#get board from crosswalk
boardfilename = r'X:\Provider Data\MPMD\Spayer\Board Name Crosswalk_Final.xlsx'
df_boardCrosswalk = pd.read_excel(boardfilename,sheet_name='ISG Board Name')
df_boardCrosswalk.rename(columns={"ISG Board Name": "Board Name"},inplace = True)
df_boardCrosswalk.rename(columns={"Crosswalk Value FINAL": "Board Name "},inplace = True)
df_boardsMapped = pd.merge(df_mapped,df_boardCrosswalk, on='Board Name', how='left')

#get institution from crosswalk
institutionfilename = r'X:\Provider Data\MPMD\Spayer\Institution Crosswalk_FINAL.xlsx'
df_institutionCrosswalk = pd.read_excel(institutionfilename,sheet_name='EDUCATION CROSSWALK_FINAL')
df_institutionCrosswalk.rename(columns={"ISG School Name": "Institution Name "},inplace = True)
df_institutionCrosswalk.rename(columns={"Crosswalk Value FINAL": "Institution Name"},inplace = True)
df_institutionMapped = pd.merge(df_boardsMapped,df_institutionCrosswalk, on='Institution Name ', how='left')

#get specialty description from crosswalk
specialtyfilename = r'X:\Provider Data\MPMD\Spayer\Speciality Description Crosswalk_Final.xlsx'
df_specialtyCrosswalk = pd.read_excel(specialtyfilename,sheet_name='ISG Speciality Description')
df_specialtyCrosswalk.rename(columns={"Crosswalk Value FINAL":"Specialty Description "},inplace = True)
df_specialtyMapped = pd.merge(df_institutionMapped,df_specialtyCrosswalk, on='Specialty Description', how='left')

#get specialty description from crosswalk
degreefilename = r'X:\Provider Data\MPMD\Spayer\Degree Crosswalk_Final.xlsx'
df_degreeCrosswalk = pd.read_excel(degreefilename,sheet_name='Sheet1')
#df_degreeCrosswalk=df_degreeCrosswalk[1:]
df_degreeCrosswalk.rename(columns={"ISG":"Degree"},inplace = True)
df_degreeCrosswalk.rename(columns={"Spayer":"Degree "},inplace = True)
df_degreeMapped = pd.merge(df_specialtyMapped,df_degreeCrosswalk, on='Degree', how='left')

#df_degreeMapped.rename(columns={"Hosp_End_Date": "End Date"},inplace = True)

Taxo_codefilename = r'X:\Provider Data\MPMD\Spayer\Taxonomy Codes_2021.07.15.csv'
df_spec_map = pd.read_csv(Taxo_codefilename)
df_spec_map.rename(columns={"Code_ID":"Taxonomy Code"},inplace = True)
#df_spec_map["Taxonomy Code"]


Taxo_join = pd.merge(df_degreeMapped,df_spec_map,on ='Taxonomy Code', how ='left')

df_mapped_final = Taxo_join[['Provider NPI 1','Last Name','First Name','M I ','Degree ','Gender','SOC SEC #','Birth Date','Ethnicity','Language Spoken','ePrep Enrolled','Medical License Number','Medical License State',
'Medical License Issued Date','Medical License Expiration Date','Provider type','DEA License Number','DEA License State','DEA License Issued Date','DEA License Expiration Date','CSR License Number',
'CSR License State','CSR License Issued Date','CSR License Expiration Date','Taxonomy Code','description','Board Name ','Board Specialty','Issue Date','Expiration Date',
'Lifetime Board Cert','Hospital Name','Start Date','Hosp_End_Date','Admitting Privs','Initial/Recred Cycle','Initial Cred Date','Last Cred Approval Date','Next Recred Due Date',
'Delegated Group Entity Name','Education Type','Institution Name ','Start Date ','End Date','Speciality Type','MEDICARE ID','Medicare Issuing state','MEDICAID ID','Medicaid Issuing state','PCP/Specialist/Hospitalist','Board Certification Status (Y/N)','Institution Name-Intership','Start Date-Internship','End Date-Internship','Speciality Type-Internship',
'Institution Name-Residency','Start Date-Residency','End Date-Residency','Speciality Type-Residency','Institution Name-Fellowship','Start Date-Fellowship','End Date-Fellowship',
'Speciality Type-Fellowship','ECFMG']]

df_mapped_final.rename(columns={'description': 'Specialty Description','Hosp_End_Date':'End Date'},inplace = True)
df_mapped_final['SOC SEC #']=df_mapped_final['SOC SEC #'].str.replace('-','')
df_mapped_final.drop_duplicates(inplace=True)


df_mapped_final.to_excel('Meritus_' +yyyymmdd+ '_FR_spayer.xlsx',index=False)
#df_mapped_final.to_csv('UMCMG_' +yyyymmdd+ '_spayer.txt',index=None, sep='\t')

print('Conversion should be done.')

print('\nFinal output saved to drive in the folder below.')
