import pandas as pd


if __name__ == '__main__':
    df_persons = pd.read_json('persons.json')
    df_anonyms = pd.read_csv('anonyms.csv')
    df_new = df_persons.copy()

    for index, row in df_persons.iterrows():
        new_name = df_anonyms.iloc[index][0] + ' ' + df_anonyms.iloc[index][1]
        new_login = df_anonyms.iloc[index][0] + df_anonyms.iloc[index][1][0]
        df_new.iloc[index][2]['name'] = new_name
        df_new.iloc[index][2]['login'] = new_login

    df_new.to_json('1_anonymized_persons.json', orient='records', lines=True)
