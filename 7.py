import pandas as pd

df = pd.read_csv("school_projects.csv")

df["final_score"] = df["jury_score"] * 0.7 + df["audience_votes"] * 0.3

max_votes = df["audience_votes"].max()
df["audience_score"] = (df["audience_votes"] / max_votes) * 100

avg_final = df["final_score"].mean()
finalists = df[df["final_score"] > avg_final]


mask_jury = finalists["jury_score"] >= 85
mask_audience = finalists["audience_score"] >= 75

strong_finalists = finalists[mask_jury & mask_audience]

mean_score = strong_finalists["final_score"].mean()
mean_hours = strong_finalists["prep_hours"].mean()

main_prize_candidates = strong_finalists[
    (strong_finalists["final_score"] > mean_score)
    & (strong_finalists["prep_hours"] < mean_hours)
]

print("Средний рейтинг сильных финалистов:", mean_score)
print("Среднее время подготовки:", mean_hours)
print()
print("Кандидатов на главный приз:", len(main_prize_candidates))
print()
print("Кандидаты:")
print(main_prize_candidates[["project_name", "prep_hours", "final_score"]])
