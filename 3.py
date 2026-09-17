import pandas as pd

df = pd.read_csv("school_projects.csv")

max_votes = df["audience_votes"].max()

df["audience_score"] = (df["audience_votes"] / max_votes) * 100

avg_audience = round(df["audience_votes"].mean(), 2)
min_audience = round(df["audience_votes"].min(), 2)
max_audience = round(df["audience_votes"].max(), 2)

print("Средняя оценка зрителей: ", avg_audience)
print("Минимальная оценка зрителей: ", min_audience)
print("Максимальная оценка зрителей: ", max_audience)
