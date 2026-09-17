import pandas as pd

df = pd.read_csv("school_projects.csv")

df["final_score"] = df["jury_score"] * 0.7 + df["audience_votes"] * 0.3

max_votes = df["audience_votes"].max()

df["audience_score"] = (df["audience_votes"] / max_votes) * 100

avg_final = df["final_score"].mean()

finalists = df[df["final_score"] > avg_final]

condition_jury = finalists["jury_score"] >= 85

condition_audience = finalists["audience_score"] >= 75

strong_finalists = finalists[condition_jury & condition_audience]

count_strong = len(strong_finalists)

avg_final_score = strong_finalists["final_score"].mean()

avg_hours = strong_finalists["prep_hours"].mean()

print("Сильных финалистов: ", count_strong)
print("Средний итоговый рейтинг: ", round(avg_final_score, 2))
print("Среднее время подготовки: ", round(avg_hours, 2))
print("\n", "Проекты:")

for index, row in strong_finalists.iterrows():
    name = row["project_name"]
    jury = row["jury_score"]
    audience = round(row["audience_score"], 2)
    final = round(row["final_score"], 2)
    
    print(f"{name} — Жюри: {jury}, Зрители: {audience}, Итог: {final}")
