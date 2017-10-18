import pandas as pd
import numpy as np

FILEPATH = r'G:\Public\National Accounts\WeeklyBestsellerImports\Temp\MassClub.xlsx'
SAVEPATH = r'G:\Public\National Accounts\WeeklyBestsellerImports\~MassClub.xlsx'

INITIAL_COLUMNS = ['\n\nAgency', '\nMaster \nChain Code',
                   '\nMaster \nChain Name','\n\nChain Code', '\n\nChain Name',
                   'Saturday \nWeek Ending\nDate','\n\nEAN', '\n\nTitle',
                   '\nMktg\nCode', '\nProg\nCode','\nBusiness\nChannel',
                   '\nVendor\nCode', '\nVendor\nName','\nPOS \nUnits',
                   '\nPOS \nConsumer $', 'Chain \nOn Hand\nUnits**']
DESIRED_COLUMNS = ['\n\nChain Code', '\nPOS \nUnits',
                   'Chain \nOn Hand\nUnits**']

CLUBS_CODES = ['BJ','CW','SA']
MASS_CODES = ['AQ','BR','DH','GA','GE','HB','JJ','KO','KZ','MJ','NA','RA','SE','SF','SY','TR','TX',"WC","WF",'WM']


def mass_club_conv(chain_code):
    if chain_code in CLUBS_CODES:
        return "Clubs"
    if chain_code in MASS_CODES:
        return "Mass"


initial_df = pd.DataFrame(pd.read_excel(FILEPATH,skip_footer=3, index_col=6,
                                        converters={'\n\nChain Code': mass_club_conv}))
initial_df.index.names = ['EAN']
initial_df.index = initial_df.index.map(str)

middle_df = initial_df[DESIRED_COLUMNS]

clubs_df = middle_df[middle_df['\n\nChain Code'] == 'Clubs'].drop('\n\nChain Code',axis=1).groupby('EAN').sum()
clubs_df.columns = ['ClubsSold', 'ClubsOH']

mass_df = middle_df[middle_df['\n\nChain Code'] == 'Mass'].drop('\n\nChain Code',axis=1).groupby('EAN').sum()
mass_df.columns = ['MassSold', 'MassOH']

output_df = pd.DataFrame()
output_df['EAN'] = initial_df.index.values
output_df = output_df.set_index('EAN')
output_df = output_df[~output_df.index.duplicated(keep='first')]

output_df = output_df.join(clubs_df,how='outer').join(mass_df,how='outer')
output_df['ClubsYTD'] = np.NaN
output_df['MassYTD'] = np.NaN

writer = pd.ExcelWriter(SAVEPATH)
output_df.to_excel(writer)
writer.save()
