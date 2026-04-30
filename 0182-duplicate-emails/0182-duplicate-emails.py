import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person = person.dropna()
    duplicates = person[person[["email"]].duplicated()]
    return duplicates[["email"]].drop_duplicates()