# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:04:57 2023

@author: NKar
"""

#!/usr/bin/env python
# coding: utf-8

# In[257]:


import pandas as pd
import time
import pyodbc
import numpy as np
from datetime import datetime
from pytz import timezone
#from string import strip
pd.set_option('display.max_columns', None)
#GET USER OF WHO EXECUTED THE CODE
start = datetime.now(timezone('US/Eastern'))

filename = r"C:\Users\NKar\OneDrive - Evolent Health, Inc\Documents\Roaster load_June_2024\LBH\spyer_add.csv"
   
yyyymmdd = time.strftime('%Y%m%d')

print('Running Conversion Query for Carrol Roster')

#df = pd.read_excel(filename,sheet_name = 'Additions')
df = pd.read_csv(filename,keep_default_na=False,low_memory=False, dtype=str,skipinitialspace=True)


# In[258]:


cols = []
count = 1
for column in df.columns:
    if column == 'Expiration Date':
        cols.append(f'Expiration Date_{count}')
        count+=1
        continue
    cols.append(column)
df.columns = cols
df = df.replace('nan', '')
df = df.fillna('')
#df['Taxonomy']= df['Taxonomy'].split('-')[0]
df['Taxonomy_new'] = df['Taxonomy'].str.split('-').str[0]
df=df.astype(str)
for col in df.columns:
    df[col]=df[col].apply(lambda x:x.strip())
df['SSN'] = df['SSN'].str.replace('-','|')
df['SSN'] = df['SSN'].str.replace('|','')
df['Title'] = df['Title'].str.replace('.','')

# columns that dont change
df1 = df.copy()
df2  = df.copy()


# In[78]:


df['DOB']


# In[79]:


df.rename(columns={'Individual NPI':'Provider NPI 1', 'Last Name':'Last Name', 'First Name':'First Name'}, inplace=True)
df.rename(columns={'Middle Initial':'M I', 'Title':'Degree','Gender':'Gender','SSN':'SOC SEC #'}, inplace=True)
df.rename(columns={'DOB':'Birth Date','Language':'Language Spoken'}, inplace=True)
df.rename(columns={'State License':'Medical License Number','Expiration Date_1':'Medical License Expiration Date'}, inplace=True)
df.rename(columns={'DEA License':'DEA License Number','Expiration Date.2':'DEA License Expiration Date', 'CDS License': 'CSR License Number','Expiration Date.1':'CSR License Expiration Date'}, inplace=True)
df.rename(columns={'Practicing Specialty':'Specialty Description','Taxonomy_new':'Taxonomy Code'}, inplace=True)
df.rename(columns={'Board Certification 1':'Board Name','From Date':'Issue Date','To Date':'Expiration Date'}, inplace=True)
df.rename(columns={'Credentialing Committee Date/Effective Date':'Initial Cred Date','Last Reappointment Date':'Last Cred Approval Date','Next Reappointment Date':'Next Recred Due Date'}, inplace=True)
df.rename(columns={'Education':'Institution Name ','To Date.3':'End Date'}, inplace=True)
df.rename(columns={'Medicaid':'MEDICAID ID','Medicare':'MEDICARE ID'}, inplace=True)
df.rename(columns={'Practitioner Type':'PCP/Specialist/Hospitalist'},inplace=True)


# In[259]:


df


# In[260]:


df['Tax ID']


# In[261]:


df['Group Name']


# In[262]:


df['Medical Field']


# In[263]:


df['From Date.3']


# In[264]:



df['Medical License Issued Date']=''
df['Provider type']=''
df['Hospital Name']=''
df['Admitting Privs']=''
df['Start Date-Residency']=df['From Date.2']
df['End Date-Residency']=df['End Date']
df['Start Date-Fellowship']=df['From Date.3']
df['End Date-Fellowship']=df['To Date.4']
df['Ethnicity']=''
df['CSR License State']=''
df['Medical License State'] = ''
df['ePrep Enrolled']=''
df['DEA License State']=''
df['DEA License Issued Date']=''
df['CSR License Issued Date']=''
df['Board Specialty']=''
df['Lifetime Board Cert']=''
df['Start Date']=''
df['End_Date_']=''
df['Initial/Recred Cycle']=''
df['Next Recred Due Date']=''
df['Delegated Group Entity Name']='LifeBridge'
df['Education Type']=''
df['Start Date ']=''
df['Speciality Type']=''
df['Medicaid Issuing state'] = ''
df['Medicare Issuing state'] = ''
df['Board Certification Status (Y/N)'] = ''
df['Institution Name-Internship'] = ''
df['Start Date-Internship'] = ''
df['End Date-Internship'] = ''
df['Institution Name-Residency'] = df['Residency']
df['Institution Name-Fellowship'] = df['Fellowship']
df['Speciality Type-Internship'] = ''
df['Speciality Type-Residency']=df['Medical Field']
df['Speciality Type-Fellowship']=df['Medical Field.1']
df['ECFMG']=''


#reorder columns
df = df[['Provider NPI 1','Last Name','First Name','M I','Degree','Gender','SOC SEC #','Birth Date','Ethnicity','Language Spoken','ePrep Enrolled','Medical License Number','Medical License State',
'Medical License Issued Date','Medical License Expiration Date','Provider type','DEA License Number','DEA License State','DEA License Issued Date','DEA License Expiration Date','CSR License Number',
'CSR License State','CSR License Issued Date','CSR License Expiration Date','Taxonomy Code','Specialty Description','Board Name','Board Specialty','Issue Date','Expiration Date',
'Lifetime Board Cert','Hospital Name','Start Date','End_Date_','Admitting Privs','Initial/Recred Cycle','Initial Cred Date','Last Cred Approval Date','Next Recred Due Date',
'Delegated Group Entity Name','Education Type','Institution Name ','Start Date ','End Date','Speciality Type','MEDICARE ID','Medicare Issuing state','MEDICAID ID','Medicaid Issuing state','PCP/Specialist/Hospitalist','Board Certification Status (Y/N)','Institution Name-Internship','Start Date-Internship','End Date-Internship','Speciality Type-Internship',
'Institution Name-Residency','Start Date-Residency','End Date-Residency','Speciality Type-Residency','Institution Name-Fellowship','Start Date-Fellowship','End Date-Fellowship',
'Speciality Type-Fellowship','ECFMG']]


# In[265]:


df


# In[266]:


df1.rename(columns={'Individual NPI':'Provider NPI 1', 'Last Name':'Last Name', 'First Name':'First Name'}, inplace=True)
df1.rename(columns={'Middle Initial':'M I','Title':'Degree','Gender':'Gender','SSN':'SOC SEC #'}, inplace=True)
df1.rename(columns={'DOB':'Birth Date','Language':'Language Spoken'}, inplace=True)
df1.rename(columns={'State License':'Medical License Number','Expiration Date_1':'Medical License Expiration Date'}, inplace=True)
df1.rename(columns={'DEA License':'DEA License Number', 'Expiration Date.2':'DEA License Expiration Date', 'CDS License': 'CSR License Number','Expiration Date.1':'CSR License Expiration Date'}, inplace=True)
df1.rename(columns={'Practicing Specialty':'Specialty Description','Taxonomy_new':'Taxonomy Code'}, inplace=True)
df1.rename(columns={'Board Certification 2':'Board Name','From Date.1':'Issue Date','To Date.1':'Expiration Date'}, inplace=True)
df1.rename(columns={'Credentialing Committee Date/Effective Date':'Initial Cred Date','Last Reappointment Date':'Last Cred Approval Date','Next Reappointment Date':'Next Recred Due Date'}, inplace=True)
df1.rename(columns={'Education':'Institution Name ','To Date.3':'End Date'}, inplace=True)
df1.rename(columns={'Medicaid':'MEDICAID ID','Medicare':'MEDICARE ID'}, inplace=True)
df1.rename(columns={'Practitioner Type':'PCP/Specialist/Hospitalist'},inplace=True)




#add in blank columns
df1['Medical License Issued Date']=''
df1['Provider type']=''
df1['Hospital Name']=''
df1['Admitting Privs']=''
df1['Start Date-Residency']=df1['From Date.2']
df1['End Date-Residency']=df1['End Date']
df1['Start Date-Fellowship']=df1['From Date.3']
df1['End Date-Fellowship']=df1['To Date.4']
df1['Ethnicity']=''
df1['CSR License State']=''
df1['Medical License State'] = ''
df1['ePrep Enrolled']=''
df1['DEA License State']=''
df1['DEA License Issued Date']=''
df1['CSR License Issued Date']=''
df1['Board Specialty']=''
df1['Lifetime Board Cert']=''
df1['Start Date']=''
df1['End_Date_']=''
df1['Initial/Recred Cycle']=''
df1['Next Recred Due Date']=''
df1['Delegated Group Entity Name']='LifeBridge'
df1['Education Type']=''
df1['Start Date ']=''
df1['Speciality Type']=''
df1['Medicaid Issuing state'] = ''
df1['Medicare Issuing state'] = ''
df1['Board Certification Status (Y/N)'] = ''
df1['Institution Name-Internship'] = ''
df1['Start Date-Internship'] = ''
df1['End Date-Internship'] = ''
df1['Institution Name-Residency'] = df1['Residency']
df1['Institution Name-Fellowship'] = df1['Fellowship']
df1['Speciality Type-Internship'] = ''
df1['Speciality Type-Residency']=df1['Medical Field']
df1['Speciality Type-Fellowship']=df1['Medical Field.1']
df1['ECFMG']=''


#reorder columns
df1 = df1[['Provider NPI 1','Last Name','First Name','M I','Degree','Gender','SOC SEC #','Birth Date','Ethnicity','Language Spoken','ePrep Enrolled','Medical License Number','Medical License State',
'Medical License Issued Date','Medical License Expiration Date','Provider type','DEA License Number','DEA License State','DEA License Issued Date','DEA License Expiration Date','CSR License Number',
'CSR License State','CSR License Issued Date','CSR License Expiration Date','Taxonomy Code','Specialty Description','Board Name','Board Specialty','Issue Date','Expiration Date',
'Lifetime Board Cert','Hospital Name','Start Date','End_Date_','Admitting Privs','Initial/Recred Cycle','Initial Cred Date','Last Cred Approval Date','Next Recred Due Date',
'Delegated Group Entity Name','Education Type','Institution Name ','Start Date ','End Date','Speciality Type','MEDICARE ID','Medicare Issuing state','MEDICAID ID','Medicaid Issuing state','PCP/Specialist/Hospitalist','Board Certification Status (Y/N)','Institution Name-Internship','Start Date-Internship','End Date-Internship','Speciality Type-Internship',
'Institution Name-Residency','Start Date-Residency','End Date-Residency','Speciality Type-Residency','Institution Name-Fellowship','Start Date-Fellowship','End Date-Fellowship',
'Speciality Type-Fellowship','ECFMG']]


# In[267]:


frames = [df,df1]
df_mapp = pd.concat(frames)


# In[268]:


print('''Conversion is in progress;
      'Do not close the program!''')


# In[82]:


df_mapped = df_mapp.replace('N/A','')


# In[35]:


print('''Fetching Data from crosswalk;
      'Do not close the program!''')


# In[269]:


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

#test specialty


#get specialty description from crosswalk


#list(df_specialtyMapped.columns)


# In[83]:


#df_specialtyMapped.to_excel('ihj' +yyyymmdd+ '_spayer.xlsx',index=False)


# In[84]:


degreefilename = r'X:\Provider Data\MPMD\Spayer\Degree Crosswalk_Final.xlsx'
df_degreeCrosswalk = pd.read_excel(degreefilename,sheet_name='Sheet1')
#df_degreeCrosswalk=df_degreeCrosswalk[1:]
df_degreeCrosswalk.rename(columns={"ISG":"Degree"},inplace = True)
df_degreeCrosswalk.rename(columns={"Spayer":"Degree "},inplace = True)
df_degreeMapped = pd.merge(df_specialtyMapped,df_degreeCrosswalk, on='Degree', how='left')

df_degreeMapped.rename(columns={"End_Date_": "End Date_hosp"},inplace = True)


# In[85]:


#sp=r"X:\Provider Data\MPMD\Spayer\Taxonomy Codes_2021.07.15.xlsx"
#df_specialtyCrosswalk = pd.read_excel(sp)
#df_specialtyCrosswalk.rename(columns={"Code_ID":"Taxonomy Code"},inplace = True)
#df_specialtyMapped = pd.merge(df_degreeMapped,df_specialtyCrosswalk, on='Taxonomy Code', how='left')


# In[86]:


#df_specialtyMapped.to_excel('ii' +yyyymmdd+ '_spayer.xlsx',index=False)


# In[88]:


df_mapped_final = df_degreeMapped[['Provider NPI 1','Last Name','First Name','M I','Degree ','Gender','SOC SEC #','Birth Date','Ethnicity','Language Spoken','ePrep Enrolled','Medical License Number','Medical License State',
'Medical License Issued Date','Medical License Expiration Date','Provider type','DEA License Number','DEA License State','DEA License Issued Date','DEA License Expiration Date','CSR License Number',
'CSR License State','CSR License Issued Date','CSR License Expiration Date','Taxonomy Code','Specialty Description','Board Name','Board Specialty','Issue Date','Expiration Date',
'Lifetime Board Cert','Hospital Name','Start Date','End Date_hosp','Admitting Privs','Initial/Recred Cycle','Initial Cred Date','Last Cred Approval Date','Next Recred Due Date',
'Delegated Group Entity Name','Education Type','Institution Name ','Start Date ','End Date','Speciality Type','MEDICARE ID','Medicare Issuing state','MEDICAID ID','Medicaid Issuing state','PCP/Specialist/Hospitalist','Board Certification Status (Y/N)','Institution Name-Internship','Start Date-Internship','End Date-Internship','Speciality Type-Internship',
'Institution Name-Residency','Start Date-Residency','End Date-Residency','Speciality Type-Residency','Institution Name-Fellowship','Start Date-Fellowship','End Date-Fellowship',
'Speciality Type-Fellowship','ECFMG']]

df_mapped_final.drop(['Specialty Description'], inplace=True, axis=1)

#df_mapped_final.rename(columns={"End Date_hosp": "End Date"},inplace = True)


# In[89]:


#df_mapped_final.to_csv('LBH_' +yyyymmdd+ '_spayer.txt',index=None, sep='\t')


# In[90]:


#df_mapped_final.to_excel('LBH_' +yyyymmdd+ '_spayer.xlsx',index=False)


# In[91]:


#df_mapped_final
df_mapped_final = df_mapped_final[df_mapped_final["Provider NPI 1"] != '']




filename = r"X:\Provider Data\MPMD\Spayer\Taxonomy CCodes_2021.07.15.csv"
df_spec_map = pd.read_csv(filename)
#df_spec_map["Code_ID"].rename
df_spec_map.rename(columns={"Code_ID":"Taxonomy Code"},inplace = True)
df_spec_map["Taxonomy Code"]


# In[110]:



# In[270]:


df_spec_map


# In[271]:


Left_join = pd.merge(df_mapped_final, 
                     df_spec_map, 
                     on ='Taxonomy Code',
                     how ='left')


# In[272]:


Left_join


# In[273]:


df_mapped_final


# In[274]:


Left_join_final = Left_join[['Provider NPI 1','Last Name','First Name','M I','Degree ','Gender','SOC SEC #',
'Birth Date','Ethnicity','Language Spoken','ePrep Enrolled','Medical License Number','Medical License State',
'Medical License Issued Date','Medical License Expiration Date','Provider type','DEA License Number',
'DEA License State','DEA License Issued Date','DEA License Expiration Date','CSR License Number',
'CSR License State','CSR License Issued Date','CSR License Expiration Date','Taxonomy Code',
'description','Board Name','Board Specialty','Issue Date','Expiration Date',
'Lifetime Board Cert','Hospital Name','Start Date','End Date_hosp','Admitting Privs','Initial/Recred Cycle','Initial Cred Date',
'Last Cred Approval Date','Next Recred Due Date',
'Delegated Group Entity Name','Education Type','Institution Name ','Start Date ','End Date','Speciality Type','MEDICARE ID',
'Medicare Issuing state','MEDICAID ID','Medicaid Issuing state','PCP/Specialist/Hospitalist','Board Certification Status (Y/N)',
'Institution Name-Internship','Start Date-Internship','End Date-Internship','Speciality Type-Internship',
'Institution Name-Residency','Start Date-Residency','End Date-Residency',
'Speciality Type-Residency','Institution Name-Fellowship','Start Date-Fellowship','End Date-Fellowship',
'Speciality Type-Fellowship','ECFMG']]

Left_join_final.rename(columns={"description": "Specialty Description"},inplace = True)
Left_join_final.rename(columns={"End Date_hosp": "End Date"},inplace = True)


# In[275]:


Left_join_final.to_excel('LBH_'+yyyymmdd+'_Spayer.xlsx',index=False)


# In[ ]:




