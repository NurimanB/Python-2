import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "C:/Users/Admin/Downloads/netflix_titles.csv"  # Replace with the actual file path
netflix_data = pd.read_csv("C:/Users/Admin/Downloads/netflix_titles.csv")

#Total number of movies and TV shows
type_counts = netflix_data['type'].value_counts()

#Most common genres
genre_counts = netflix_data['listed_in'].str.split(', ').explode().value_counts()

#Handle missing values
netflix_data['director'] = netflix_data['director'].fillna('Unknown')
netflix_data['cast'] = netflix_data['cast'].fillna('Unknown')
netflix_data['country'] = netflix_data['country'].fillna('Unknown')

netflix_data['date_added'] = netflix_data['date_added'].str.strip()  # Remove leading/trailing spaces
netflix_data['date_added'] = pd.to_datetime(netflix_data['date_added'], errors='coerce')  # Convert to datetime


netflix_data.dropna(subset=['date_added', 'rating', 'duration'], inplace=True)

netflix_data['date_added'] = pd.to_datetime(netflix_data['date_added'])
netflix_data['year_added'] = netflix_data['date_added'].dt.year

#The number of movies and TV shows added each year
year_counts = netflix_data.groupby(['year_added', 'type']).size().reset_index(name='count')

plt.figure(figsize=(12, 6))
sns.barplot(data=year_counts, x='year_added', y='count', hue='type', palette='viridis')
plt.title('Number of Movies and TV Shows Added Each Year', fontsize=16)
plt.xlabel('Year Added', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Type', loc='upper left')
plt.tight_layout()
plt.show()

#The most common genre
most_common_genre = genre_counts.idxmax()

print("Total Counts:")
print(type_counts)
print("\nMost Common Genres:")
print(genre_counts.head())
print(f"\nThe most common genre in the dataset is '{most_common_genre}'.")

print("\nThe bar chart shows how the addition of movies and TV shows has changed over the years. This can reflect the growing content catalog of Netflix.")
