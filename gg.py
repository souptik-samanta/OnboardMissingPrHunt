import pandas as pd

not_df = pd.read_csv("not.csv")
msli_df = pd.read_csv("msli.csv")

msli_links = set(msli_df["Code URL"].dropna())

results = []

for index, row in not_df.iterrows():
    pr_link = row["PR Link"]
    if pr_link not in msli_links:
        results.append({"PR Link": pr_link, "Status": "not in msli"})

# Write the results to a new CSV file if there are any entries
if results:
    results_df = pd.DataFrame(results)
    results_df.to_csv("not_found_in_msli.csv", index=False)
