import pandas as pd
import xlrd

FILEPATH = r'Apple_925-101_2017.xlsx'

input_df = pd.DataFrame(pd.read_excel(FILEPATH,dtype={u'ISBN':object}))

starting_columns = [u'Title', u'Author', u'Units', u'Publisher Proceeds',
       u'Currency of Proceeds', u'Customer Price', u'Customer Currency',
       u'Country Code', u'Product Type Identifier', u'Pre-Order',
       u'Promo Code', u'ISBN', u'Apple Identifier', u'Vendor Identifier',
       u'Vendor Offer Code', u'Publisher', u'Imprint', u'Download Date (PST)',
       u'Order Id', u'Postal Code', u'Customer Identifier',
       u'Report Date (Local)', u'Sales/Return', u'Institution',
       u'Street Address 1', u'Street Address 2', u'Street Address 3', u'City',
       u'State', u'Institution Postal Code', u'Institution Country',
       u'Version', u'Category']

ending_columns = [u'Title',u'Units']

dropped_columns = list(set(starting_columns) - set(ending_columns))

output_df = input_df.groupby([u'ISBN'])[ending_columns].sum()
print(output_df.columns)
#output_df = output_df.drop(dropped_columns)

print(output_df.head(50))
#print(dropped_columns)