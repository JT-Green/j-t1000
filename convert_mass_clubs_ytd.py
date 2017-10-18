import pandas as pd
import numpy as np

FILEPATH = r'G:\Public\National Accounts\WeeklyBestsellerImports\Temp\MassClubYTD.xlsx'
SAVEPATH = r'G:\Public\National Accounts\WeeklyBestsellerImports\~MassClubYTD.xlsx'

INITIAL_COLUMNS = ['\n\nItem#', '\n\nISBN', '\n\nEAN', '\n\nTitle', '\n\nAuthor',
       '\n\nMSRP', '\nParent Vendor\nName', '\nParent Vendor\nCode',
       '\n\nVendor', '\nVendor\nCode', '\nOn Sale\nDate', '\n\nAGENCY',
       '\n\nChain', '\n\nChannel', 'Romeoville WH\nAvail \nUnits',
       'Romeoville WH\nOn Order \nUnits', 'Salem WH\nAvail \nUnits',
       'Salem WH \nOn Order\nUnits', 'Clearfield WH\nAvail \nUnits',
       'Clearfield WH\nOn Order \nUnits', 'Denton WH\nAvail \nUnits',
       'Denton WH\nOn Order\nUnits', 'Atlanta WH\nAvail \nUnits',
       'Atlanta WH\nOn Order \nUnits', 'Indy WH\nAvail \nUnits',
       'Indy WH \nOn Order\nUnits', 'Ogden WH\nAvail \nUnits',
       'Ogden WH \nOn Order\nUnits', 'Other WH\nAvail \nUnits',
       'Other WH \nOn Order\nUnits', '\nLTD \nStores', '\nOutbound\nUnits',
       '\nReturns\nUnits', '\nNet \nUnits', '\nPOS \nUnits',
       '\nOutbound\nMSRP$', '\nReturns\nMSRP$', '\nNet \nMSRP$',
       '\nPOS \nMSRP$', '\nOutbound \nConsumer$', '\nReturns \nConsumer$',
       '\nNet \nConsumer$', '\nPOS \nConsumer$']
DESIRED_COLUMNS = ['\n\nChain', '\nPOS \nUnits']

CLUBS_CODES = ['BJ WHOLESALE CLUB', 'COSTCO WHOLESALE', 'SAMS CLUB', "SAM'S CLUB"]
MASS_CODES = ['TARGET','WAL-MART']


def mass_club_conv(chain_code):
    if chain_code in CLUBS_CODES:
        return "Clubs"
    if chain_code in MASS_CODES:
        return "Mass"


initial_df = pd.DataFrame(pd.read_excel(FILEPATH, skiprows=3, index_col=2,
                                        converters={'\n\nChain': mass_club_conv}))
initial_df.index.names = ['EAN']
initial_df.index = initial_df.index.map(str)

middle_df = initial_df[DESIRED_COLUMNS]

clubs_df = middle_df[middle_df['\n\nChain'] == 'Clubs'].drop('\n\nChain', axis=1).groupby('EAN').sum()
clubs_df.columns = ['ClubsYTD']

mass_df = middle_df[middle_df['\n\nChain'] == 'Mass'].drop('\n\nChain', axis=1).groupby('EAN').sum()
mass_df.columns = ['MassYTD']

output_df = pd.DataFrame()
output_df['EAN'] = initial_df.index.values
output_df = output_df.set_index('EAN')
output_df = output_df[~output_df.index.duplicated(keep='first')]

output_df = output_df.join(clubs_df).join(mass_df)

writer = pd.ExcelWriter(SAVEPATH)
output_df.to_excel(writer)
writer.save()
