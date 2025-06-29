import pandas as pd

df = pd.read_csv("project_scores.csv")
print(df)

python_series = df["python_score"]

mean_score = python_series.mean()
print("Mean Python Score:", mean_score)

print("\nFirst 3 rows of the DataFrame:")
print(df.head(3))

print("\nName and ML_Score columns:")
print(df[["Name", "ML_Score"]])

df.fillna(0, inplace=True)

df["Total_Score"] = df["Python_Score"] + df["ML_Score"] + df["AI_Score"]
df["result"] = df["Total_Score"].apply(lambda x: "Pass" if x >= 240 else "Fail")

cs_passed = df[(df["Department"] == "CS" )& (df["result"] == "Pass")]
sorted_df = cs_passed.sort_values(by="Total_Score", ascending=False)
sorted_df.to_csv("final_results.csv", index=False)

print("\nFinal cleaned data saved to 'final_results.csv'")
