import pandas as pd

df = pd.read_csv("school_projects.csv")


df["final_score"] = df["jury_score"] * 0.7 + df["audience_votes"] * 0.3

avg_final = df["final_score"].mean()
min_final = df["final_score"].min()
max_final = df["final_score"].max()

diff_final = max_final - avg_final

print("Средний итоговый рейтинг: ", round(avg_final, 2))
print("Минимальный итоговый рейтинг: ", round(min_final, 2))
print("Максимальный итоговый рейтинг: ", round(max_final, 2))
print("Лучший результат выше среднего на: ", round(diff_final, 2))
