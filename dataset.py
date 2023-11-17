import pandas as pd


def get_country_data(dataset_path: str = "facts_countries.csv") -> pd.DataFrame:
    """Učitava CSV datoteku na dataset_path putanji. Čisti podatke, uklanja NaN ćelije,
    transponira podatke u DataFrame-u i vraća takav DataFrame.

    Args:
        dataset_path (str, optional): Putanja do CSV datoteke. Defaultno "facts_countries.csv".

    Returns:
        pd.DataFrame: DataFrame sa pročišćenim podacima.
    """
    df = pd.read_csv(dataset_path, sep=";", skiprows=[1])

    for column in df.columns:
        df[column].fillna(0, inplace=True)

    df_transposed = df.transpose()
    df_transposed.columns = df_transposed.iloc[0]
    df_transposed.columns = map(str.lower, df_transposed.columns)
    df_transposed = df_transposed[1:]

    return df_transposed


if __name__ == "__main__":
    df = get_country_data()
    print(df)

