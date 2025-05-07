import pandas as pd

df = pd.read_csv('es_01-06-05-25.xlsx - Orders.csv')

def fix_address(row):
    if pd.isnull(row['receiverAddress']) or row['receiverAddress'].strip() == '' or \
    'Receiver\'s address is empty' in row['statusAdditionalInfo'] or \
    'Address exceeds 60 symbols' in row['statusAdditionalInfo']:
        
        new_address = f"{row['receiverCity']}, {row['receiverZip']}, {row['receiverCountry']}"
        return new_address[:40]
    else:
        return row['receiverAddress']
        
def fix_full_name(row):
    if 'Full name exceeds 40 symbols' in row[statusAdditionalInfo]:
        new_name = row['receiverFullName'][:40].title()
        return new_name
    else:
        return row['receiverFullName']
        
df['receiverAddress'] = df.apply(fix_address, axis=1)
df['receiverFullName'] = df.apply(fix_full_name, axis=1)

df.to_csv('es_01-06-05-25.csv', index=False)
df.to_excel('es_01-06-05-25.xslx', index=False)

print(df.shape)

