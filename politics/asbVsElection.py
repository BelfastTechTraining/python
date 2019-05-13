import pandas as pd

police2electoral = {'Antrim & Newtownabbey': 'Antrim and Newtownabbey',
                    'Ards & North Down': 'North Down and Ards',
                    'Armagh City Banbridge & Craigavon': 'Armagh, Banbridge and Craigavon',
                    'Belfast City': 'Belfast',
                    'Causeway Coast & Glens': 'Causeway Coast and Glens',
                    'Derry City & Strabane': 'Derry and Strabane',
                    'Fermanagh & Omagh': 'Fermanagh and Omagh',
                    'Lisburn & Castlereagh City': 'Lisburn and Castlereagh',
                    'Mid & East Antrim': 'Mid and East Antrim',
                    'Mid Ulster': 'Mid Ulster',
                    'Newry Mourne & Down': 'Newry, Mourne and Down'}

asb_df = pd.read_csv('anti-social-behaviour-monthly-data.csv', parse_dates={'datetime': ['Calendar_Year', 'Month']})
asb_df.set_index('datetime', inplace=True)

for police, electoral in police2electoral.items():
    asb_df['Policing_District'] = asb_df['Policing_District'].replace(police, electoral)

asb_df = asb_df[asb_df.index > pd.to_datetime('2018')]
asb_df = asb_df[asb_df['Policing_District'] != 'No Policing District Assigned']
asb_df = asb_df[asb_df['Policing_District'] != 'Northern Ireland']

election_df = pd.read_csv('Northern Ireland Council Election Results - DataCSV.csv')
election_df = election_df[election_df['DataCategory'] != '2014 Votes']
election_df = election_df.drop(['DEA', 'Elected', 'Name', 'Party', 'DataCategory'], axis=1)

party_list = ['AP', 'Aontú', 'Conservatives', 'DUP', 'GP', 'Independent', 'Independent Nationalist',
              'Independent Unionist', 'Other', 'Other Socialist', 'PBP', 'PUP', 'SDLP',
              'SF', 'TUV', 'UKIP', 'UUP', 'Workers\' Party']

police = asb_df.groupby('Policing_District')['Incident_Count'].sum()

grouped = election_df.groupby(['Council', 'PartyGrouped'])['FirstPrefs'].sum()
parties = grouped.unstack().fillna(0)
parties['Most votes'] = parties.idxmax(axis=1)
parties['Total votes'] = parties.sum(axis=1)

party_asb = parties
party_asb['anti-social'] = police

party_asb['anti2vote'] = party_asb['anti-social'] / party_asb['Total votes'] * 100

print(party_asb.sort_values('anti2vote', ascending=False).drop(party_list, axis=1))
