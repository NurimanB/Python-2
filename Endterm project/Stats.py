import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'D:\VsCode\python-2\Endterm project\2023-2024 NBA Player Stats - Playoffs.csv'
nba_data = pd.read_csv(file_path, delimiter=';')

# Task 1: Identify the player with the most points scored in the playoffs
most_points_player = nba_data.loc[nba_data['PTS'].idxmax(), ['Player', 'PTS']]

# Task 2: Compare average points per game across teams
average_points_per_team = nba_data.groupby('Tm')['PTS'].mean().sort_values(ascending=False)

# Task 3: Performance trends of the top 5 players across games
# Identify the top 5 players by total points
top_5_players = nba_data.nlargest(5, 'PTS')[['Player', 'PTS', 'G']]
# Filter data for top 5 players
top_5_data = nba_data[nba_data['Player'].isin(top_5_players['Player'])]

# Plot performance trends
plt.figure(figsize=(10, 6))
for player in top_5_players['Player']:
    player_data = nba_data[nba_data['Player'] == player]
    plt.plot(player_data['G'], player_data['PTS'], label=player, marker='o')

plt.title('Performance Trends of Top 5 Players')
plt.xlabel('Games Played')
plt.ylabel('Points Scored')
plt.legend()
plt.grid(True)
plt.show()

# Task 4: Analyze the average number of fouls committed by each team
average_fouls_per_team = nba_data.groupby('Tm')['PF'].mean().sort_values(ascending=False)

# Task 5: Identify the player with the greatest overall contribution
nba_data['Total_Contribution'] = nba_data['PTS'] + nba_data['AST']
greatest_contributor = nba_data.loc[nba_data['Total_Contribution'].idxmax(), ['Player', 'Total_Contribution']]

# Display results
print("Player with the most points scored in the playoffs:")
print(most_points_player)

print("\nAverage points per game across teams:")
print(average_points_per_team)

print("\nAverage fouls committed by each team:")
print(average_fouls_per_team)

print("\nPlayer with the greatest overall contribution (points + assists):")
print(greatest_contributor)
