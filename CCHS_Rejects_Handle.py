# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 18:24:09 2024

@author: AANair
"""


import pandas as pd
 
# Assuming your Excel file is named 'your_file.xlsx' and the sheet name is 'Sheet1'
excel_file_path = r'C:\Users\AANair\Downloads\NPI_Spec.xlsx'
df = pd.read_excel(excel_file_path, sheet_name='Sheet1')
df=df.drop_duplicates()
# Create a new column to identify groups of NPIs
df['Group'] = (df['prov_npi_id'] != df['prov_npi_id']).cumsum()
print(df['Group'])
 
# Pivot the DataFrame to get NPIs and specialties in separate columns
df_pivot = df.pivot_table(index='Group', columns='prov_npi_id', values='spec_specialty_id_1',aggfunc=lambda x:','.join(x))
 
df_transposed=df_pivot.T.reset_index()
df_transposed.columns=['NPI','Specialty']
 
# Reset index and drop the 'Group' column
#df_pivot.reset_index(drop=True, inplace=True)

# Save the modified DataFrame back to Excel if needed
df_transposed.to_excel('output_file.xlsx', index=False)