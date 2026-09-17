import pandas as pd

df = pd.read_csv("school_projects.csv")

df["final_score"] = df["jury_score"] * 0.7 + df["audience_votes"] * 0.3

avg_final = df["final_score"].mean()

finalists = df[df["final_score"] > avg_final]

count_finalists = len(finalists)


print("Средний итоговый рейтинг: ", round(avg_final, 2))
print(f"Прошло в следующий этап: ", count_finalists)
print("\n", "Финалисты:")


for index, row in finalists.iterrows():
    print(f"{row["project_name"]}: {round(row["final_score"], 2)}")
