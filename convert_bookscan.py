import pandas as pd
import xlrd

FILEPATH = r'G:\Public\National Accounts\WeeklyBestsellerImports\Temp\Bookscan.csv'
SAVEPATH = r'G:\Public\National Accounts\WeeklyBestsellerImports\~Bookscan.xlsx'
INPUT_COLUMNS = [u'ISBN-13', u'Title', u'Author', u'Imprint', u'Publisher',
       u'Publish Date', u'Bisac', u'Bisac Description', u'Format', u'Price',
       u'TW Total', u'YTD Total', u'TW Retail/Club',
       u'YTD Retail/Club', u'TW Mass Merchandisers/Other',
       u'YTD Mass Merchandisers/Other', u'TW Non-Traditional',
       u'YTD Non-Traditional']
OUTPUT_COLUMNS = [0,1,10,11]


def clean_isbn(isbn13):
    """Changes ISBN-13 values from '="ISBN13"' to 'ISBN13'"""

    return isbn13.replace('"','').replace('=','')


def remove_paren(column):
    """Removes '(week-ending date)' for week-to-week consistency"""

    if column.find('(') > -1:
        return column[:column.find('(')]
    else:
        return column


input_df = pd.DataFrame(pd.read_csv(FILEPATH, skiprows=[0],
                                    converters={"ISBN-13": clean_isbn}))
input_df.rename(columns=lambda x: remove_paren(x), inplace=True)
print(input_df.columns)

# Create lists to populate later if there are any errors
missing_columns = []
new_columns = []

for column in input_df.columns:
    if not column in INPUT_COLUMNS:
        new_columns.append(column)
    
for column in INPUT_COLUMNS:
    if not column in input_df.columns:
        missing_columns.append(column)

if not missing_columns and not new_columns:
    print(input_df.ix[:,OUTPUT_COLUMNS].head(5))

else:
    if missing_columns:
        print("MISSING COLUMNS")
        for column in missing_columns:
            print(column)
    if new_columns:
        print("NEW COLUMNS")
        for column in new_columns:
            print(column)
