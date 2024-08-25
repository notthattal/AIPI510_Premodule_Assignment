import main
import pandas as pd

'''
test_sortDF_actually_sorts - A test function used to verify that the SortDFByCol function found in the main module correctly sorts the
                             FG% column of the dataframe in descending order
'''
def test_sortDF_actually_sorts():
    #use pandas to read the csv
    df = pd.read_csv('csvParser/2023_nba_player_stats.csv')
    
    # Sort the 'PTS' column in descending order
    sorted_pts = sorted(df['FG%'], reverse=True)

    #retrieve the sorted dataframe from the function we are testing
    result_df = main.SortDFByCol(df, 'FG%')
    
    #Get the points column as a list to be compared to sorted_pts
    result_list = result_df['FG%'].to_list()

    #ensure the 2 columns are equivalent
    assert sorted_pts == result_list