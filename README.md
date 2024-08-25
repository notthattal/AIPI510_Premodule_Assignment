# AIPI510_Premodule_Assignment
## Overview
This project uses a CSV of NBA player statistics from the 2022-2023 regular season (labeled "2023_nba_player_stats.csv"), sorts the players from highest to lowest based on field goal percentage, and prints out the top 5 players.
## Pre-requisites
 - Python 3
 - Git
## How to install and run the project
### 1. Clone the repository
Open a terminal on your local machine and run the following command:
```
git clone https://github.com/notthattal/AIPI_510_Premodule_Assignment.git
```
 ### 2. Change your current directory to the project's directory
 In the same terminal type:
 ```
 cd AIPI_510_Premodule_Assignment
```
### 3. Create and activate the Python virtual environment
For Windows Users:
```
python -m venv venv
venv\Scripts\activate
```
For macOS/Linux Users:
```
python3 -m venv venv
source venv/bin/activate
```
### 4. Install the required dependencies
Run the following command:
```
pip install -r requirements.txt
```
### 5. Run the package
To run the package enter the following command:
```
python csvParser/main.py
```
### 6. Run unit tests
To run the unit tests for this package use the following command:
```
pytest -v
```
### 7. Deactivate the virtual environment
To deactivate the virtual environment run:
```
deactivate
```
## Sources
1. The CSV used to process the data: Mirzaei, Amirhossein. "https://www.kaggle.com/datasets/amirhosseinmirzaie/nba-players-stats2023-season" 2023
2. ChatGPT/Pandas Documentation: ChatGPT was used to lookup documentation for pandas and was further verified using the official pandas documentation website "https://pandas.pydata.org/docs/"