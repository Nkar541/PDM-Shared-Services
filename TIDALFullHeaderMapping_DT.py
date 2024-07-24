# -*- coding: utf-8 -*-
"""
Created on Tues May 25 15:38:23 2021

@author: BSpotts
"""

import pandas as pd
import numpy as np
#from datetime import datetime
import pyodbc
#Opens folder with headers template.

#input('Copy the data you want to import into a copy of the Tidal Header Template, name it TidalImport.csv, and hit enter.') #User prompt
#filename = r'C:\Users\bspotts\Desktop\TidalImport.csv'

filename = r'C:\Users\AANair\OneDrive - Evolent Health, Inc\Documents\Rosters\2024\April\TH\Full.xlsx'
    
df = pd.read_excel(filename) 
#df = pd.read_csv(filename, low_memory=False) 
# columns that dont change
df.rename(columns={'NPI':'prov_npi_id', 'Last Name': 'prov_last_name', 'First Name': 'prov_first_name'}, inplace=True)
df.rename(columns={'Middle Name/Initial':'prov_middle_initial', 'Degree': 'prov_prof_desg_1', 'GENDER': 'prov_gender'}, inplace=True)
df.rename(columns={'Ethnicity': 'prov_ethnicity','Provider Language':'prov_language_1'}, inplace=True)
df.rename(columns={'Date of Birth':'prov_birth_date','Social Security Number': 'prov_soc_sec_number'}, inplace=True)
df.rename(columns={'Tax id':'tax_id_number','Group NPI':'bu_npi_id','OFFICE NAME':'bu_name'}, inplace=True)
df.rename(columns={'Office Street Address':'sl_address_1','Office Ste/Building Number':'sl_address_2','Office City':'sl_city','Office State':'sl_state'}, inplace=True)
df.rename(columns={'Office Zip Code':'sl_zip_code','Office Phone Number':'sl_phone_number','Office Fax Number':'sl_fax_number'}, inplace=True)
df.rename(columns={'Provider Type':'sl_status_code','Individual Taxonomy':'spec_specialty_id_1'}, inplace=True)
df.rename(columns={'Accepting New Patients':'sl_accept_new_patient'}, inplace=True)
df.rename(columns={'Medicaid Provider # (if not provided, provider will not be set PAR for Medicaid) ':'prov_medicaid_id','Medicare #':'prov_medicare_id'}, inplace=True)
df.rename(columns={'Federal DEA Certificate Number':'lic_dea_1_id','DEA Certificate Expiration Date':'lic_dea_1_term_date'}, inplace=True)
print('Done importing data.')
#add in blank columns
df['tax_id_number'] = df['tax_id_number'].replace("-","")
df['prov_name_suffix']=''
df['bu_address_1']=''
df['prov_language_2']=''
df['prov_language_3']=''
df['prov_language_4']=''
df['prov_language_5']=''
df['prov_language_6']=''
df['prov_language_7']=''
df['prov_language_8']=''
df['prov_language_9']=''
df['prov_language_10']=''
df['sl_show_in_dir']=''
df['prov_email_address']=''
df['prov_cultural_competency_training']=''
df['prov_dual_demo_population_training']=''
df['prov_received_date']=''
df['prov_approved_date']=''
df['bu_name']=''
df['bu_city']=''
df['bu_state']=''
df['bu_zip_code']=''
df['bu_mail_address_1']=''
df['bu_mail_city']=''
df['bu_mail_state']=''
df['bu_mail_zip_code']=''
df['bu_payment_center']=''
df['bu_business_type']='2'
df['bu_address_2']=''
df['bu_mail_address_2']=''
df['sl_county']=''
df['sl_mail_address_1']=''
df['sl_mail_address_2']=''
df['sl_mail_city']=''
df['sl_mail_state']=''
df['sl_mail_zip_code']=''
df['sl_office_manager_name']=''
df['sl_fax_number']=''
df['sl_monday_hours']='8:00 AM-5:00 PM'
df['sl_tuesday_hours']='8:00 AM-5:00 PM'
df['sl_wednesday_hours']='8:00 AM-5:00 PM'
df['sl_thursday_hours']='8:00 AM-5:00 PM'
df['sl_friday_hours']='8:00 AM-5:00 PM'
df['sl_saturday_hours']='CLOSED'
df['sl_sunday_hours']='CLOSED'
df['sl_status_code']=df['sl_status_code'].replace(["Specialist","PCP"],["N","Y"])
df['sl_min_patient_age']='0'
df['sl_max_patient_age']='120'
df['sl_offered_services']=''
df['sl_tty_service']=''
df['sl_handicap_accessible']='Y'
df['sl_accept_dev_disabilities']='Y'
df['sl_panel_capacity']=''
df['sl_termination_reason']=''
df['sl_24_operation']=''
df['sl_loc_category']=''
df['sl_translation_services']=''
df['sl_wheelchair_accessible_exam_room']=''
df['sl_wheelchair_accessible_restroom']=''
df['sl_wheelchair_ramps']=''
df['sl_accepts_hiv_aids']=''
df['sl_accepts_co_occurring_disorders']=''
df['sl_accepts_chronic_illness']=''
df['sl_accepts_physical_disabilities']=''
df['sl_accepts_serious_mental_illness']=''
df['sl_accepts_homeless_patients']=''
df['sl_accepts_visually_impaired']=''
df['sl_accepts_hearing_impaired']=''
df['sl_adjustable_exam_table']=''
df['sl_handicap_parking']='Y'
df['sl_website_url']=''
df['sl_esi_id_1']=''
df['sl_esi_id_type_1']=''
df['sl_esi_id_desc_1']=''
df['sl_esi_id_eff_date_1']=''
df['sl_esi_id_term_date_1']=''
df['sl_esi_id_2']=''
df['sl_esi_id_type_2']=''
df['sl_esi_id_desc_2']=''
df['sl_esi_id_eff_date_2']=''
df['sl_esi_id_term_date_2']=''
df['sl_esi_id_3']=''
df['sl_esi_id_type_3']=''
df['sl_esi_id_desc_3']=''
df['sl_esi_id_eff_date_3']=''
df['sl_esi_id_term_date_3']=''
df['sl_esi_id_4']=''
df['sl_esi_id_type_4']=''
df['sl_esi_id_desc_4']=''
df['sl_esi_id_eff_date_4']=''
df['sl_esi_id_term_date_4']=''
df['sl_esi_id_5']=''
df['sl_esi_id_type_5']=''
df['sl_esi_id_desc_5']=''
df['sl_esi_id_eff_date_5']=''
df['sl_esi_id_term_date_5']=''
df['sl_service_location_name']=df['Office/Practice name']
df['sl_termination_date']=''
df['spec_reporting_type_1']=''
df['spec_specialty_id_2']=''
df['spec_reporting_type_2']=''
df['spec_state_reporting_2']=''
df['spec_specialty_id_3']=''
df['spec_reporting_type_3']=''
df['spec_state_reporting_3']=''
df['spec_specialty_id_4']=''
df['spec_reporting_type_4']=''
df['spec_state_reporting_4']=''
df['spec_specialty_id_5']=''
df['spec_reporting_type_5']=''
df['spec_state_reporting_5']=''
df['cert_specialty_id_1']=''
df['cert_board_cert_date_1']=''
df['cert_cert_name_1']=''
df['cert_specialty_id_2']=''
df['cert_board_cert_date_2']=''
df['cert_board_name_2']=''
df['cert_expiration_date_2']=''
df['cert_cert_name_2']=''
df['cert_specialty_id_3']=''
df['cert_board_cert_date_3']=''
df['cert_board_name_3']=''
df['cert_expiration_date_3']=''
df['cert_cert_name_3']=''
df['aff_effective_date']=df['Original Credentialing Date']
df['aff_termination_date']='12/31/9999'
df['aff_id']=''
df['aff_contract_id']=''
df['aff_pricing_driver_1']=''
df['aff_pricing_driver_2']=''
df['aff_pricing_driver_3']=''
df['aff_cap_rate_id']=''
df['lic_medicaid_1_id']=''
df['lic_medicaid_1_eff_date']=''
df['lic_medicaid_1_term_date']=''
df['lic_state_1_id']=df['State License Number']
df['lic_state_1_state']=df['State of Licensure']
df['lic_state_1_eff_date']='1/1/2020'
df['lic_state_1_term_date']=df['License Expiration Date']
df['lic_state_2_id']=''
df['lic_state_2_state']=''
df['lic_state_2_eff_date']=''
df['lic_state_2_term_date']=''
df['lic_state_3_id']=''
df['lic_state_3_state']=''
df['lic_state_3_eff_date']=''
df['lic_state_3_term_date']=''
df['lic_dea_1_state']=df['DEA State']
df['lic_dea_1_eff_date']=''
df['lic_dea_2_id']=''
df['lic_dea_2_state']=''
df['lic_dea_2_eff_date']=''
df['lic_dea_2_term_date']=''
df['lic_dea_3_id']=''
df['lic_dea_3_state']=''
df['lic_dea_3_eff_date']=''
df['lic_dea_3_term_date']=''
df['ph_hos_rel_1_id']=''
df['ph_hos_rel_1_eff_date']=''
df['ph_hos_rel_1_term_date']=''
df['ph_hos_rel_2_id']=''
df['ph_hos_rel_2_eff_date']=''
df['ph_hos_rel_2_term_date']=''
df['ph_hos_rel_3_id']=''
df['ph_hos_rel_3_eff_date']=''
df['ph_hos_rel_3_term_date']=''
df['cert_board_name_1']=''
df['spec_state_reporting_1']=''
df['cert_expiration_date_1'] =''
print('Done adding columns.')
#reorder columns
df = df[['prov_npi_id','prov_last_name','prov_first_name','prov_middle_initial','prov_name_suffix','prov_prof_desg_1','prov_soc_sec_number',
           'prov_gender','prov_language_1','prov_language_2','prov_language_3','prov_language_4','prov_language_5','prov_language_6',
           'prov_language_7','prov_language_8','prov_language_9','prov_language_10','prov_ethnicity','prov_birth_date','prov_email_address','prov_medicare_id',
           'prov_medicaid_id','prov_cultural_competency_training','prov_dual_demo_population_training','prov_received_date','prov_approved_date',
           'tax_id_number','bu_npi_id','bu_name','bu_address_1','bu_address_2','bu_city','bu_state','bu_zip_code','bu_mail_address_1',
           'bu_mail_address_2','bu_mail_city','bu_mail_state','bu_mail_zip_code','bu_payment_center','bu_business_type','sl_address_1',
           'sl_address_2','sl_city','sl_state','sl_zip_code','sl_county','sl_mail_address_1','sl_mail_address_2','sl_mail_city','sl_mail_state',
           'sl_mail_zip_code','sl_office_manager_name','sl_phone_number','sl_fax_number','sl_monday_hours','sl_tuesday_hours','sl_wednesday_hours',
           'sl_thursday_hours','sl_friday_hours','sl_saturday_hours','sl_sunday_hours','sl_status_code','sl_accept_new_patient',
           'sl_min_patient_age','sl_max_patient_age','sl_offered_services','sl_show_in_dir','sl_tty_service','sl_handicap_accessible',
           'sl_accept_dev_disabilities','sl_panel_capacity','sl_termination_reason','sl_24_operation','sl_loc_category','sl_translation_services',
           'sl_wheelchair_accessible_exam_room','sl_wheelchair_accessible_restroom','sl_wheelchair_ramps','sl_accepts_hiv_aids',
           'sl_accepts_co_occurring_disorders','sl_accepts_chronic_illness','sl_accepts_physical_disabilities','sl_accepts_serious_mental_illness',
           'sl_accepts_homeless_patients','sl_accepts_visually_impaired','sl_accepts_hearing_impaired','sl_adjustable_exam_table',
           'sl_handicap_parking','sl_website_url','sl_esi_id_1','sl_esi_id_type_1','sl_esi_id_desc_1','sl_esi_id_eff_date_1',
           'sl_esi_id_term_date_1','sl_esi_id_2','sl_esi_id_type_2','sl_esi_id_desc_2','sl_esi_id_eff_date_2','sl_esi_id_term_date_2',
           'sl_esi_id_3','sl_esi_id_type_3','sl_esi_id_desc_3','sl_esi_id_eff_date_3','sl_esi_id_term_date_3','sl_esi_id_4','sl_esi_id_type_4',
           'sl_esi_id_desc_4','sl_esi_id_eff_date_4','sl_esi_id_term_date_4','sl_esi_id_5','sl_esi_id_type_5','sl_esi_id_desc_5',
           'sl_esi_id_eff_date_5','sl_esi_id_term_date_5','sl_service_location_name','sl_termination_date','spec_specialty_id_1',
           'spec_reporting_type_1','spec_state_reporting_1','spec_specialty_id_2','spec_reporting_type_2','spec_state_reporting_2',
           'spec_specialty_id_3','spec_reporting_type_3','spec_state_reporting_3','spec_specialty_id_4','spec_reporting_type_4',
           'spec_state_reporting_4','spec_specialty_id_5','spec_reporting_type_5','spec_state_reporting_5','cert_specialty_id_1',
           'cert_board_cert_date_1','cert_board_name_1','cert_expiration_date_1','cert_cert_name_1','cert_specialty_id_2','cert_board_cert_date_2',
           'cert_board_name_2','cert_expiration_date_2','cert_cert_name_2','cert_specialty_id_3','cert_board_cert_date_3','cert_board_name_3',
           'cert_expiration_date_3','cert_cert_name_3','aff_effective_date','aff_termination_date','aff_id','aff_contract_id','aff_pricing_driver_1',
           'aff_pricing_driver_2','aff_pricing_driver_3','aff_cap_rate_id','lic_medicaid_1_id','lic_medicaid_1_eff_date','lic_medicaid_1_term_date',
           'lic_state_1_id','lic_state_1_state','lic_state_1_eff_date','lic_state_1_term_date','lic_state_2_id','lic_state_2_state',
           'lic_state_2_eff_date','lic_state_2_term_date','lic_state_3_id','lic_state_3_state','lic_state_3_eff_date','lic_state_3_term_date',
           'lic_dea_1_id','lic_dea_1_state','lic_dea_1_eff_date','lic_dea_1_term_date','lic_dea_2_id','lic_dea_2_state','lic_dea_2_eff_date',
           'lic_dea_2_term_date','lic_dea_3_id','lic_dea_3_state','lic_dea_3_eff_date','lic_dea_3_term_date','ph_hos_rel_1_id',
           'ph_hos_rel_1_eff_date','ph_hos_rel_1_term_date','ph_hos_rel_2_id','ph_hos_rel_2_eff_date','ph_hos_rel_2_term_date',
           'ph_hos_rel_3_id','ph_hos_rel_3_eff_date','ph_hos_rel_3_term_date']]
df = df.fillna('')
#df['tax_id_number'] = df['tax_id_number'].str.replace("-","")
df['sl_accept_new_patient'] = df['sl_accept_new_patient'].replace(["No","Yes"],["N","Y"])
df['sl_show_in_dir'] = df['sl_show_in_dir'].replace(["No","Yes"],["N","Y"])
df['prov_gender']=df['prov_gender'].replace(["Female","Male"],["F","M"])

#df.to_csv('MPMD_Provider_'+yyyymmdd+'_Tidal_01.csv',index=False)
#Copy header mapped file to df_mapped
df_mapped = df.copy()

#Connect to MPMD Extract 
cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=aldprddbmpmd02.chicago.local;"
                          "Database=MPMDAPP;"
                          "Trusted_Connection=yes;")
cursor = cnxn.cursor()
sql ='''
	select DISTINCT 
p.hippa_id as prov_npi_id
, bu.business_name as aldera_bu_name
, bti.tax_id_number as tax_id_number
, bu.npi_id as bu_npi_id
, ll.address_1 as bu_address_1
, l.address_1 as sl_address_1
, cast(aff.termination_date as date) as aff_termination_date_y

from MPMDAPP.dbo.provider_link sl with (nolock)

left outer join MPMDAPP.dbo.provider p with (nolock) on (sl.provider_gid = p.provider_gid) and (p.record_status = 'a')

left outer join MPMDAPP.dbo.business_units bu with (nolock) on (sl.business_gid = bu.business_gid) and (bu.record_status = 'a')

left outer join MPMDAPP.dbo.Business_Tax_Relation btr with (nolock) on (bu.business_gid = btr.business_gid) and (btr.record_status = 'a')

left outer join MPMDAPP.dbo.Business_Tax_Info bti with (nolock) on (btr.business_tax_gid = bti.business_tax_gid) and (bti.record_status = 'a')

left outer join MPMDAPP.dbo.locations l with (nolock) on (sl.location_gid = l.location_gid) and (l.record_status = 'a')

left outer join MPMDAPP.dbo.locations ll with (nolock) on (bu.payment_location_gid = ll.location_gid) and (ll.record_status = 'a') --and (bu.record_status = 'a')

left outer join MPMDAPP.dbo.Provider_Affiliations aff with (nolock) on (sl.provider_gid = aff.provider_gid) and (sl.business_gid = aff.business_gid) and (sl.location_gid = aff.location_gid) and (aff.record_status = 'a')

'''

aldera = pd.read_sql(sql,cnxn)
cursor.close()
cnxn.close()



#Check if Triad + SLs + BU on header mapped file (Roster) are already available in Aldera
df_mapped["concat"] = df_mapped['prov_npi_id'].astype(str)+"_"+df_mapped['tax_id_number'].astype(str)+"_"+df_mapped['bu_npi_id'].astype(str)+ "_"+ df_mapped['sl_address_1'].str[:4].str.lower() + "_" + df_mapped['bu_address_1'].str[-6:]

aldera['concat']= aldera['prov_npi_id'].astype(str)+"_"+aldera['tax_id_number'].astype(str)+"_"+aldera['bu_npi_id'].astype(str)+ "_"+ aldera['sl_address_1'].str[:4].str.lower() + "_" + aldera['bu_address_1'].str[-6:]

aldera_con = aldera[['concat','aff_termination_date_y']]

df_mapped_aldera = pd.merge(df_mapped,aldera_con,on=['concat'],how='left')
df_mapped_aldera['Flag_1_if_available'] = np.where(df_mapped_aldera['aff_termination_date_y'].isnull(), '0','1')

df_mapped_aldera.to_csv('Mapped_cnmc10.csv',index=False)
print('\nHeader file triad check is complete and file saved to drive')
input('Press Enter to continue')

# Connect to Language codes from SSMS

cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=hpsprddb01.chicago.local\gemini;"
                          "Database=ProviderSandbox;"
                         "Trusted_Connection=yes;")
cursor = cnxn.cursor()
sql_language = '''SELECT  [Code]
      ,[Description]
      ,[New_Code]
  FROM [ProviderSandbox].[Reference].[MPMD.Language]
'''

aldera_language = pd.read_sql(sql_language,cnxn)
aldera_language.drop(columns =["Code"] , inplace =True)

aldera_language.rename(columns={"Description": "prov_language_1"},inplace = True)

df_mapped_aldera['prov_language_1']= df_mapped_aldera['prov_language_1'].str.lower()
aldera_language['prov_language_1']= aldera_language['prov_language_1'].str.lower()

#perform join on languages
df_mapped_language = pd.merge(df_mapped_aldera,aldera_language, on='prov_language_1', how='left')
df_mapped_language.rename(columns={"New_Code": "Languages_code"},inplace = True)

df_mapped_language['var3'] = ''
df_mapped_language['var3'] = np.where(df_mapped_language['Languages_code'].isnull(), df_mapped_language['prov_language_1'],df_mapped_language['Languages_code'])
df_mapped_language['prov_language_1'] = df_mapped_language['var3']
df_mapped_language.drop(['var3','Languages_code'],axis=1,inplace = True)
df_l = df_mapped_language.copy()


print('Language encoding is done!')

#BU Name standardization from Aldera Extract
df_l = df_l.astype(str).replace('nan','')


#Replacing BU NAME from df with Aldera with NPI2 and TIN combo
select_bu_columns = aldera[['tax_id_number','bu_npi_id','aldera_bu_name']]
aldera_bu = select_bu_columns.copy()
aldera_bu.drop_duplicates(inplace = True)

print('\nJoining aldera data with dataframe')
alderaJoin = pd.merge(df_l,aldera_bu, on=['tax_id_number','bu_npi_id'],  how='left')


alderaJoin['bu_name'] = alderaJoin['aldera_bu_name']
del alderaJoin['aldera_bu_name']
alderaJoin.to_csv('Tidal.csv',index=False)
#print('\nMapping of Bu name is complete and file saved to drive')

