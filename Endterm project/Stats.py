import pandas as pd
import matplotlib.pyplot as plt

path = r'D:\VsCode\python-2\Endterm project\2023-2024 NBA Player Stats - Playoffs.csv'
data = pd.read_csv(path, delimiter=';')

# Task 1:
most_points_player = data.loc[data['PTS'].idxmax(), ['Player', 'PTS']]

# Task 2
avg_pts_per_team = data.groupby('Tm')['PTS'].mean().sort_values(ascending=False)

# Plotting
plt.figure(figsize=(12, 6))
avg_pts_per_team.plot(kind='bar', color='skyblue')
plt.title('Average Points Per Game Across Teams')
plt.xlabel('Team')
plt.ylabel('Average Points')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Task 3
top_5_players = data.nlargest(5, 'PTS')[['Player', 'PTS', 'G']]
top_5_data = data[data['Player'].isin(top_5_players['Player'])]

# Plotting
plt.figure(figsize=(10, 6))
for player in top_5_players['Player']:
    player_data = data[data['Player'] == player]
    plt.plot(player_data['G'], player_data['PTS'], label=player, marker='o')

plt.title('Performance Trends of Top 5 Players')
plt.xlabel('Games Played')
plt.ylabel('Points Scored')
plt.legend()
plt.grid(True)
plt.show()

# Task 4
avg_fouls_per_team = data.groupby('Tm')['PF'].mean().sort_values(ascending=False)

# Plotting
plt.figure(figsize=(12, 6))
avg_fouls_per_team.plot(kind='bar', color='salmon')
plt.title('Average Fouls Committed Per Team')
plt.xlabel('Team')
plt.ylabel('Average Fouls')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Task 5
data['Total_Contribution'] = data['PTS'] + data['AST']
goat_contributor = data.loc[data['Total_Contribution'].idxmax(), ['Player', 'Total_Contribution']]

# Results
print("Player with the most points scored in the playoffs:")
print(most_points_player)

print("\nAverage points per game across teams:")
print(avg_pts_per_team)

print("\nAverage fouls committed by each team:")
print(avg_fouls_per_team)

print("\nPlayer with the greatest overall contribution (points + assists):")
print(goat_contributor)
