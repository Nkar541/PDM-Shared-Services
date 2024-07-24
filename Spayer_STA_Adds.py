
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:20:44 2022

@author: AANair
"""

import pandas as pd
import time

filename = r"C:\Users\NKar\OneDrive - Evolent Health, Inc\Documents\Roaster load_August_2023\STA - 135678 & 135658\spayer_adds_sta.xlsx"
   
yyyymmdd = time.strftime('%Y%m%d')
#gender = [['M', 'Male'], ['F', 'Female']]
#dfGender = pd.DataFrame(gender, columns=['Gender_Roster', 'Gender'])

print('Running Conversion Query for STA Roster')
df = pd.read_excel(filename, dtype=str)

df = df.replace('nan', '')
df =df.fillna('')
df['Languages'] = df['Languages'].apply(lambda x: x.replace('&',','))

df['Languages']=df['Languages'].str.split('[,]')
df = df.explode('Languages').reset_index(drop=True)

#trim space from all columns
df=df.astype(str)
for col in df.columns:
    df[col]=df[col].apply(lambda x:x.strip())
 

# columns that dont change
df.rename(columns={'Individual NPI':'Provider NPI 1'}, inplace=True)
df.rename(columns={'MI':'M I ', 'Degree': 'Degree_Roster', 'Sex': 'Gender','SSN':'SOC SEC #'}, inplace=True)
df.rename(columns={'DOB':'Birth Date','Languages':'Language Spoken'}, inplace=True)
df.rename(columns={'MD License':'Medical License Number','MD License Exp Date':'Medical License Expiration Date'}, inplace=True)
df.rename(columns={'DEA License':'DEA License Number', 'DEA Exp Date': 'DEA License Expiration Date', 'CDS License': 'CSR License Number','CDS Exp Date':'CSR License Expiration Date'}, inplace=True)
#df.rename(columns={'Taxonomy': 'Taxonomy Code'}, inplace=True)
df.rename(columns={'Specialty':'SpecialtyDescription_Roster'}, inplace=True)
df.rename(columns={'Board Certification': 'BoardName_Roster', 'Cert Date': 'Issue Date','Cert Exp Date':'Expiration Date'}, inplace=True)
df.rename(columns={'Hospital':'HospitalName_Roster'}, inplace=True)
df.rename(columns={'Medical School':'InstitutionName_Roster'}, inplace=True)
df.rename(columns={'PCP/Specialist/Hospital-Based':'PCP/Specialist/Hospitalist', 'Medicaid #':'MEDICAID ID','Medicare #':'MEDICARE ID'}, inplace=True)
df.rename(columns={'Appt Date':'Initial Cred Date','Reapp Date':'Last Cred Approval Date'}, inplace=True)
if 'Taxonomy' in df.columns:
    df.rename(columns={'Taxonomy': 'Taxonomy Code'}, inplace=True)


#add in blank columns
df['Language Spoken']='English'
df['Ethnicity']=''
df['ePrep Enrolled']=''
df['Medical License State']=''
df['Medical License Issued Date']=''
df['DEA License State']=''
df['DEA License Issued Date']=''
df['CSR License State']=''
df['CSR License Issued Date']=''
df['Board Specialty']=''
df['Lifetime Board Cert']=''
df['Board Certification Status (Y/N)']=''
df['Start Date_Hosp']=''
df['End Date_Hosp']=''
df['Admitting Privs']=''
df['Initial/Recred Cycle']=''
df['Next Recred Due Date']=''
df['Delegated Group Entity Name']='St Agnes'
df['Education Type']=''
df['Start Date_Inst']=''
df['End Date_Inst']=''
df['Speciality Type']=''
df['Medicare Issuing state']=''
df['Medicaid Issuing state']=''
df['Institution Name-Internship']=''
df['Start Date-Internship']=''
df['End Date-Internship']=''
df['Speciality Type-Internship']=''
df['Institution Name-Residency']=''
df['Start Date-Residency']=''
df['Speciality Type-Residency']=''
df['End Date-Residency']=''
df['Institution Name-Fellowship']=''
df['Start Date-Fellowship']=''
df['Speciality Type-Fellowship']=''
df['End Date-Fellowship']=''
df['ECFMG']=''
df['Provider type'] = df.loc[:, 'Degree_Roster']
df['SOC SEC #'] = df['SOC SEC #'].str.replace("-","")
#reorder columns when taxonomy column available (for adds)
if 'Taxonomy Code' in df.columns:
    df = df[['Provider NPI 1','Last Name','First Name','M I ','Degree_Roster','Gender','SOC SEC #','Birth Date','Ethnicity','Language Spoken','ePrep Enrolled','Medical License Number','Medical License State',
    'Medical License Issued Date','Medical License Expiration Date','Provider type','DEA License Number','DEA License State','DEA License Issued Date','DEA License Expiration Date','CSR License Number',
    'CSR License State','CSR License Issued Date','CSR License Expiration Date', 'Taxonomy Code','SpecialtyDescription_Roster','BoardName_Roster','Board Specialty','Issue Date','Expiration Date',
    'Lifetime Board Cert','Board Certification Status (Y/N)','HospitalName_Roster','Start Date_Hosp','End Date_Hosp','Admitting Privs','Initial/Recred Cycle','Initial Cred Date','Last Cred Approval Date','Next Recred Due Date',
    'Delegated Group Entity Name','Education Type','InstitutionName_Roster','Start Date_Inst','End Date_Inst','Speciality Type','MEDICARE ID','Medicare Issuing state','MEDICAID ID','Medicaid Issuing state',
    'Institution Name-Internship', 'Start Date-Internship', 'End Date-Internship', 'Speciality Type-Internship',
    'Institution Name-Residency', 'Start Date-Residency', 'End Date-Residency', 'Speciality Type-Residency',
    'Institution Name-Fellowship','Start Date-Fellowship','End Date-Fellowship','Speciality Type-Fellowship', 
    'PCP/Specialist/Hospitalist','ECFMG']]
else:
    df = df[['Provider NPI 1','Last Name','First Name','M I ','Degree_Roster','Gender','SOC SEC #','Birth Date','Ethnicity','Language Spoken','ePrep Enrolled','Medical License Number','Medical License State',
    'Medical License Issued Date','Medical License Expiration Date','Provider type','DEA License Number','DEA License State','DEA License Issued Date','DEA License Expiration Date','CSR License Number',
    'CSR License State','CSR License Issued Date','CSR License Expiration Date', 'SpecialtyDescription_Roster','BoardName_Roster','Board Specialty','Issue Date','Expiration Date',
    'Lifetime Board Cert','Board Certification Status (Y/N)','HospitalName_Roster','Start Date_Hosp','End Date_Hosp','Admitting Privs','Initial/Recred Cycle','Initial Cred Date','Last Cred Approval Date','Next Recred Due Date',
    'Delegated Group Entity Name','Education Type','InstitutionName_Roster','Start Date_Inst','End Date_Inst','Speciality Type','MEDICARE ID','Medicare Issuing state','MEDICAID ID','Medicaid Issuing state',
    'Institution Name-Internship', 'Start Date-Internship', 'End Date-Internship', 'Speciality Type-Internship',
    'Institution Name-Residency', 'Start Date-Residency', 'End Date-Residency', 'Speciality Type-Residency',
    'Institution Name-Fellowship','Start Date-Fellowship','End Date-Fellowship','Speciality Type-Fellowship', 
    'PCP/Specialist/Hospitalist','ECFMG']]
#df = pd.merge(df,dfGender, on='Gender_Roster', how='left')

#get board from crosswalk
boardfilename = r'X:\Provider Data\MPMD\Spayer\Board Name Crosswalk_Final.xlsx'
df_boardCrosswalk = pd.read_excel(boardfilename,sheet_name='ISG Board Name')
df_boardCrosswalk.rename(columns={"ISG Board Name": "BoardName_Roster"},inplace = True)
df_boardCrosswalk.rename(columns={"Crosswalk Value FINAL": "Board Name"},inplace = True)
df_boardsMapped = pd.merge(df,df_boardCrosswalk, on='BoardName_Roster', how='left')

#get institution from crosswalk
institutionfilename = r'X:\Provider Data\MPMD\Spayer\Institution Crosswalk_FINAL.xlsx'
df_institutionCrosswalk = pd.read_excel(institutionfilename,sheet_name='EDUCATION CROSSWALK_FINAL')
df_institutionCrosswalk.rename(columns={"ISG School Name": "InstitutionName_Roster"},inplace = True)
df_institutionCrosswalk.rename(columns={"Crosswalk Value FINAL": "Institution Name"},inplace = True)
df_institutionMapped = pd.merge(df_boardsMapped,df_institutionCrosswalk, on='InstitutionName_Roster', how='left')



#get degree from crosswalk
degreefilename = r'X:\Provider Data\MPMD\Spayer\Degree Crosswalk_Final.xlsx'
df_degreeCrosswalk = pd.read_excel(degreefilename,sheet_name='DEGREE_CROSSWALK')
df_degreeCrosswalk.rename(columns={"ISG":"Degree_Roster"},inplace = True)
df_degreeCrosswalk.rename(columns={"Spayer":"Degree"},inplace = True)
df_degreeMapped = pd.merge(df_institutionMapped,df_degreeCrosswalk, on='Degree_Roster', how='left')

#get hospital from crosswalk
hospfilename = r'X:\Provider Data\MPMD\Spayer\Institution Crosswalk_FINAL.xlsx'
df_hospCrosswalk = pd.read_excel(hospfilename,sheet_name='HOSPITAL CROSSWALK_FINAL')
df_hospCrosswalk.rename(columns={"Hospital Name":"HospitalName_Roster"},inplace = True)
df_hospCrosswalk.rename(columns={"Crosswalk Value FINAL":"Hospital Name"},inplace = True)
df_hospMapped = pd.merge(df_degreeMapped,df_hospCrosswalk, on='HospitalName_Roster', how='left')

#rename hospital dates and institution dates
df_hospMapped.rename(columns={'Start Date_Inst':'Start Date ','End Date_Inst':'End Date '}, inplace=True)
df_hospMapped.rename(columns={'Start Date_Hosp':'Start Date','End Date_Hosp':'End Date'}, inplace=True)

#get specialty description from crosswalk
taxonomyfilename = r'X:\Provider Data\MPMD\Spayer\Taxonomy Codes_2021.07.15.xlsx'
df_taxonomyCrosswalk = pd.read_excel(taxonomyfilename)
df_taxonomyCrosswalk.rename(columns={"Code_ID": "Taxonomy Code"},inplace = True)
df_taxonomyCrosswalk.rename(columns={"description":"Specialty Description"},inplace = True)

if 'Taxonomy Code' in df.columns:
    df_taxonomyMapped = pd.merge(df_hospMapped,df_taxonomyCrosswalk, on='Taxonomy Code', how='left')
    
else:
    #get specialty description from crosswalk
    specialtyfilename = r'X:\Provider Data\MPMD\Spayer\HC-KKI-STA Speciality Description Crosswalk_Final.xlsx'
    df_specialtyCrosswalk = pd.read_excel(specialtyfilename)
    df_specialtyCrosswalk.rename(columns={"Specialty Description": "SpecialtyDescription_Roster"},inplace = True)
    df_specialtyCrosswalk.rename(columns={"Crosswalk Value FINAL":"Specialty Description"},inplace = True)
    df_specialtyMapped = pd.merge(df_hospMapped,df_specialtyCrosswalk, on='SpecialtyDescription_Roster', how='left')

    #get Taxonomy Code_Roster
    df_taxonomyMapped = pd.merge(df_specialtyMapped,df_taxonomyCrosswalk, on='Specialty Description', how='left')


#reorder columns
df = df_taxonomyMapped[['Provider NPI 1','Last Name','First Name','M I ','Degree','Gender','SOC SEC #','Birth Date','Ethnicity','Language Spoken','ePrep Enrolled','Medical License Number','Medical License State',
'Medical License Issued Date','Medical License Expiration Date','Provider type','DEA License Number','DEA License State','DEA License Issued Date','DEA License Expiration Date','CSR License Number',
'CSR License State','CSR License Issued Date','CSR License Expiration Date', 'Taxonomy Code','Specialty Description','Board Name','Board Specialty','Issue Date','Expiration Date',
'Lifetime Board Cert','Hospital Name','Start Date','End Date','Admitting Privs','Initial/Recred Cycle','Initial Cred Date','Last Cred Approval Date','Next Recred Due Date',
'Delegated Group Entity Name','Education Type','Institution Name','Start Date ','End Date ','Speciality Type','MEDICARE ID','Medicare Issuing state','MEDICAID ID','Medicaid Issuing state',
'PCP/Specialist/Hospitalist', 'Board Certification Status (Y/N)',
'Institution Name-Internship', 'Start Date-Internship', 'End Date-Internship', 'Speciality Type-Internship',
'Institution Name-Residency', 'Start Date-Residency', 'End Date-Residency', 'Speciality Type-Residency',
'Institution Name-Fellowship','Start Date-Fellowship','End Date-Fellowship','Speciality Type-Fellowship', 'ECFMG']]


df.to_csv('STA_' +yyyymmdd+ '_spayer.csv',index=False)
df.to_csv('STA_' +yyyymmdd+ '_spayer.txt',index=None, sep='\t')
