import pandas as pd

'''
SortDFByCol - Function that returns a dataframe sorted by the values of a specific column
    Parameters:
        df - the dataframe to be sorted
        colName - the column for which the dataframe should be sorted by
'''
def SortDFByCol(df, colName):
    #sort the column specified in descending order (highest to lowest)
    return df.sort_values(by=colName, ascending=False)

'''
Main - Function for primary logic to be executed
'''
def main():
    #use pandas to read the csv
    df = pd.read_csv('csvParser/2023_nba_player_stats.csv')

    #Sort the dataframe based on the data of a specific column
    sorted_df = SortDFByCol(df, "FG%")

    # Show the top 5 players
    print(sorted_df.head(5))

#ensure main is only run when the script is executed directly
if __name__ == "__main__":
    main()

