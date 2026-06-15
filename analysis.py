import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")
df = df.fillna("Unknown")

# Movies vs TV Shows
type_counts = df["type"].value_counts()
print(type_counts)

plt.figure(figsize=(6, 6))
plt.pie(type_counts.values, labels=type_counts.index, autopct="%1.1f%%", colors=["steelblue", "firebrick"])
plt.title("Netflix content by type")
plt.savefig("type_chart.png")
print("Type chart saved!")

# Top 10 countries
top10 = df["country"].str.split(", ").explode().value_counts().head(10)

plt.figure(figsize=(10, 6))
plt.barh(top10.index.tolist(), top10.values.tolist(), color="steelblue")
plt.xlabel("Number of titles")
plt.title("Top 10 countries producing Netflix content")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("countries_chart.png")
print("Countries chart saved!")

# Content growth over time
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
yearly = df["date_added"].dt.year.value_counts().sort_index()

x = yearly.index.tolist()
y = yearly.values.tolist()

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker="o", color="steelblue")
plt.xlabel("Year")
plt.ylabel("Titles added")
plt.title("Netflix content growth over time")
plt.tight_layout()
plt.savefig("growth_chart.png")
print("Growth chart saved!")

# Top 10 genres
genres = df["listed_in"].str.split(", ").explode().value_counts().head(10)

x = genres.index.tolist()
y = genres.values.tolist()

plt.figure(figsize=(10, 6))
plt.barh(x, y, color="red")
plt.xlabel("Number of titles")
plt.title("Top 10 genres on Netflix")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("genres_chart.png")
print("Genres chart saved!")


#average netflix film length time
movies = df[df["type"] == "Movie"]
durations = movies[movies["duration"] != "Unknown"]["duration"].str.replace(" min", "").astype(int)
print(round(durations.mean(), 1))

plt.figure(figsize=(10, 6))
plt.hist(durations, bins=30, color="steelblue", edgecolor="white")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of movies")
plt.title(f"Distribution of Netflix movie durations (avg: {round(durations.mean(), 1)} mins)")
plt.tight_layout()
plt.savefig("duration_chart.png")
print("Duration chart saved!")