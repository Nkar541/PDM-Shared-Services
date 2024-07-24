# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:25:06 2022

@author: AANair
"""

import pandas as pd
import time

filename = r'C:\Users\AANair\OneDrive - Evolent Health, Inc\Documents\Rosters\2024\April\TH\Tidal Health full recd 04252024.xlsx'

yyyymmdd = time.strftime('%Y%m%d')

print('Running Conversion Query for TH Roster')
#df = pd.read_excel(filename, sheet_name='Add', dtype=str)

df = pd.read_excel(filename)#,sheet_name='Add')
df = df.astype(str).replace('nan','')


#df = df.replace('nan', '')
#df =df.fillna('')
df['Languages'] = df['Languages'].apply(lambda x: x.replace('&',','))

df['Languages']=df['Languages'].str.split('[,]')
df = df.explode('Languages').reset_index(drop=True)
df = df.replace('Pending','')
df = df.replace('pending','')
#trim space from all columns
df=df.astype(str)
for col in df.columns:
    df[col]=df[col].apply(lambda x:x.strip())
 
# Specialty 1 and Specialty 2 to one column
df['Speciality/Sub-Speciality']=df['Speciality/Sub-Speciality'].str.split('[/]')
df = df.explode('Speciality/Sub-Speciality').reset_index(drop=True)
df['Speciality/Sub-Speciality']=df['Speciality/Sub-Speciality'].str.split('[&]')
df = df.explode('Speciality/Sub-Speciality').reset_index(drop=True)


#trim space from all columns
df=df.astype(str)
for col in df.columns:
    df[col]=df[col].apply(lambda x:x.strip())
    

# columns that dont change
df.rename(columns={'Indiv. NPI#':'Provider NPI 1','Eprep Enrolled (Y=Yes/ N=No)':'ePrep Enrolled'}, inplace=True)
df.rename(columns={'Degree': 'Degree_Roster'}, inplace=True)
df.rename(columns={'Languages':'Language Spoken'}, inplace=True)
df.rename(columns={'Medical Lic #':'Medical License Number','STATE.1':'Medical License State','Expiration Date':'Medical License Expiration Date'}, inplace=True)
df.rename(columns={'DEA #':'DEA License Number', 'DEA Exp': 'DEA License Expiration Date', 'CDS #': 'CSR License Number','STATE':'CSR License State','CDS Exp':'CSR License Expiration Date'}, inplace=True)
#df.rename(columns={'Speciality/Sub-Speciality':'Specialty Description'}, inplace=True)
df.rename(columns={'Board Cert.': 'BoardName_Roster', 'Lifetime Bd Certification': 'Lifetime Board Cert','Exp Date':'Expiration Date'}, inplace=True)
df.rename(columns={' Hosp Affil':'HospitalName_Roster','Admitting Privileges':'Admitting Privs'}, inplace=True)
df.rename(columns={'Medical School':'InstitutionName_Roster','Grad Date':'End Date_Inst'}, inplace=True)
df.rename(columns={'Residency/Fellowship':'Institution Name-Fellowship_Roster'}, inplace=True)
df.rename(columns={'PCP/Specialist':'PCP/Specialist/Hospitalist', 'Medicaid #':'MEDICAID ID', 'Medicare #':'MEDICARE ID'}, inplace=True)
df.rename(columns={'Delegate Committee Approval Date':'Initial Cred Date'}, inplace=True)




#add in blank columns

df['Medical License Issued Date']=''
df['DEA License State']=''
df['DEA License Issued Date']=''
df['CSR License Issued Date']=''
df['Board Specialty']=''
df['Issue Date']=''
df['Board Certification Status (Y/N)']=''
df['Start Date_Hosp']=''
df['End Date_Hosp']=''
df['Next Recred Due Date']=''
df['Initial/Recred Cycle']=''
df['Last Cred Approval Date']=''
df['Delegated Group Entity Name']='TidalHealth Care'
df['Education Type']=''
df['Start Date_Inst']=''
df['Speciality Type']=''
df['Medicare Issuing state']=''
df['Medicaid Issuing state']=''
df['Institution Name-Internship']=''
df['Start Date-Internship']=''
df['End Date-Internship']=''
df['Speciality Type-Internship']=''
df['Start Date-Residency']=''
df['Speciality Type-Residency']=''
df['Start Date-Fellowship']=''
df['Speciality Type-Fellowship']=''
df['ECFMG']=''
df['Provider type'] = df.loc[:, 'Degree_Roster']
df['Institution Name-Residency_Roster'] = df.loc[:, 'Institution Name-Fellowship_Roster']


if [df['Residency/Fellowship Date'] != '']:
    df[['Start Date-Fellowship', 'End Date-Fellowship']] = df['Residency/Fellowship Date'].str.split('-', 1, expand=True)
    df['Start Date-Residency'] = df.loc[:, 'Start Date-Fellowship']
    df['End Date-Residency'] = df.loc[:, 'End Date-Fellowship']
else:
    df[['Start Date-Fellowship', 'End Date-Fellowship']] = ''

#reorder columns
df = df[['Provider NPI 1','Last Name','First Name','M I ','Degree_Roster','Gender','SOC SEC #','Birth Date','Ethnicity','Language Spoken','ePrep Enrolled','Medical License Number','Medical License State',
'Medical License Issued Date','Medical License Expiration Date','Provider type','DEA License Number','DEA License State','DEA License Issued Date','DEA License Expiration Date','CSR License Number',
'CSR License State','CSR License Issued Date','CSR License Expiration Date','Taxonomy Code',
'BoardName_Roster','Board Specialty','Issue Date','Expiration Date',
'Lifetime Board Cert','HospitalName_Roster','Start Date_Hosp','End Date_Hosp','Admitting Privs','Initial/Recred Cycle','Initial Cred Date','Last Cred Approval Date','Next Recred Due Date',
'Delegated Group Entity Name','Education Type','InstitutionName_Roster','Start Date_Inst','End Date_Inst','Speciality Type','MEDICARE ID','Medicare Issuing state','MEDICAID ID','Medicaid Issuing state',
'Institution Name-Internship', 'Start Date-Internship', 'End Date-Internship', 'Speciality Type-Internship',
'Institution Name-Residency_Roster', 'Start Date-Residency', 'End Date-Residency', 'Speciality Type-Residency',
'Institution Name-Fellowship_Roster','Start Date-Fellowship','End Date-Fellowship','Speciality Type-Fellowship', 
'PCP/Specialist/Hospitalist','ECFMG','Board Certification Status (Y/N)']]


# columns that dont change

#get board from crosswalk
boardfilename = r'W:\Provider Data\MPMD\Spayer\Board Name Crosswalk_Final.xlsx'
df_boardCrosswalk = pd.read_excel(boardfilename,sheet_name='ISG Board Name')
df_boardCrosswalk.rename(columns={"ISG Board Name": "BoardName_Roster"},inplace = True)
df_boardCrosswalk.rename(columns={"Crosswalk Value FINAL": "Board Name"},inplace = True)
df_boardsMapped = pd.merge(df,df_boardCrosswalk, on='BoardName_Roster', how='left')

#get institution from crosswalk
institutionfilename = r'W:\Provider Data\MPMD\Spayer\Institution Crosswalk_FINAL.xlsx'
df_institutionCrosswalk = pd.read_excel(institutionfilename,sheet_name='EDUCATION CROSSWALK_FINAL')
df_institutionCrosswalk.rename(columns={"ISG School Name": "InstitutionName_Roster"},inplace = True)
df_institutionCrosswalk.rename(columns={"Crosswalk Value FINAL": "Institution Name"},inplace = True)
df_institutionMapped = pd.merge(df_boardsMapped,df_institutionCrosswalk, on='InstitutionName_Roster', how='left')

#get residency from crosswalk
df_ResidencyCrosswalk = pd.read_excel(institutionfilename,sheet_name='EDUCATION CROSSWALK_FINAL')
df_ResidencyCrosswalk.rename(columns={"ISG School Name": "Institution Name-Residency_Roster"},inplace = True)
df_ResidencyCrosswalk.rename(columns={"Crosswalk Value FINAL": "Institution Name-Residency"},inplace = True)
df_ResidencyMapped = pd.merge(df_institutionMapped,df_ResidencyCrosswalk, on='Institution Name-Residency_Roster', how='left')


#get fellowship from crosswalk
df_fellowshipCrosswalk = pd.read_excel(institutionfilename,sheet_name='EDUCATION CROSSWALK_FINAL')
df_fellowshipCrosswalk.rename(columns={"ISG School Name": "Institution Name-Fellowship_Roster"},inplace = True)
df_fellowshipCrosswalk.rename(columns={"Crosswalk Value FINAL": "Institution Name-Fellowship"},inplace = True)
df_fellowshipMapped = pd.merge(df_ResidencyMapped,df_fellowshipCrosswalk, on='Institution Name-Fellowship_Roster', how='left')

#get specialty description from crosswalk
specialtyfilename = r'W:\Provider Data\MPMD\Spayer\Taxonomy Codes_2021.07.15.xlsx'
df_specialtyCrosswalk = pd.read_excel(specialtyfilename)
df_specialtyCrosswalk.rename(columns={"Code_ID": "Taxonomy Code"},inplace = True)
df_specialtyCrosswalk.rename(columns={"description":"Specialty Description"},inplace = True)
df_specialtyMapped = pd.merge(df_fellowshipMapped,df_specialtyCrosswalk, on='Taxonomy Code', how='left')

#get degree from crosswalk
degreefilename = r'W:\Provider Data\MPMD\Spayer\Degree Crosswalk_Final.xlsx'
df_degreeCrosswalk = pd.read_excel(degreefilename,sheet_name='DEGREE_CROSSWALK')
df_degreeCrosswalk.rename(columns={"ISG":"Degree_Roster"},inplace = True)
df_degreeCrosswalk.rename(columns={"Spayer":"Degree"},inplace = True)
df_degreeMapped = pd.merge(df_specialtyMapped,df_degreeCrosswalk, on='Degree_Roster', how='left')

#get hospital from crosswalk
hospfilename = r'W:\Provider Data\MPMD\Spayer\Institution Crosswalk_FINAL.xlsx'
df_hospCrosswalk = pd.read_excel(hospfilename,sheet_name='HOSPITAL CROSSWALK_FINAL')
df_hospCrosswalk.rename(columns={"Hospital Name":"HospitalName_Roster"},inplace = True)
df_hospCrosswalk.rename(columns={"Crosswalk Value FINAL":"Hospital Name"},inplace = True)
df_hospMapped = pd.merge(df_degreeMapped,df_hospCrosswalk, on='HospitalName_Roster', how='left')

#rename hospital dates and institution dates
df_hospMapped.rename(columns={'Start Date_Inst':'Start Date ','End Date_Inst':'End Date '}, inplace=True)
df_hospMapped.rename(columns={'Start Date_Hosp':'Start Date','End Date_Hosp':'End Date'}, inplace=True)



#reorder columns
df_mapped_final = df_hospMapped[['Provider NPI 1','Last Name','First Name','M I ','Degree','Gender','SOC SEC #','Birth Date','Ethnicity','Language Spoken','ePrep Enrolled','Medical License Number','Medical License State',
'Medical License Issued Date','Medical License Expiration Date','Provider type','DEA License Number','DEA License State','DEA License Issued Date','DEA License Expiration Date','CSR License Number',
'CSR License State','CSR License Issued Date','CSR License Expiration Date', 'Taxonomy Code','Specialty Description','Board Name','Board Specialty','Issue Date','Expiration Date',
'Lifetime Board Cert','Hospital Name','Start Date','End Date','Admitting Privs','Initial/Recred Cycle','Initial Cred Date','Last Cred Approval Date','Next Recred Due Date',
'Delegated Group Entity Name','Education Type','Institution Name','Start Date ','End Date ','Speciality Type','MEDICARE ID','Medicare Issuing state','MEDICAID ID','Medicaid Issuing state',
'PCP/Specialist/Hospitalist', 'Board Certification Status (Y/N)',
'Institution Name-Internship', 'Start Date-Internship', 'End Date-Internship', 'Speciality Type-Internship',
'Institution Name-Residency', 'Start Date-Residency', 'End Date-Residency', 'Speciality Type-Residency',
'Institution Name-Fellowship','Start Date-Fellowship','End Date-Fellowship','Speciality Type-Fellowship', 'ECFMG']]

df_mapped_final['SOC SEC #']=df_mapped_final['SOC SEC #'].astype(str).str[0:9]

df_mapped_final.drop_duplicates(inplace=True)

df_mapped_final.to_excel('TH_' +yyyymmdd+ '_spayer.xlsx',index=False)
df_mapped_final.to_csv('TH_' +yyyymmdd+ '_spayer.csv',index=False)
df_mapped_final.to_csv('TH_' +yyyymmdd+ '_spayer.txt',index=None, sep='\t')

