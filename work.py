import pandas as pd
import time

onboard_df = pd.read_csv("onboard_pr_data.csv")
msli_df = pd.read_csv("msli.csv")

required_onboard_columns = {"PR Number", "Author", "PR Link"}
if not required_onboard_columns.issubset(onboard_df.columns):
    raise ValueError("One or more required columns are missing in onboard_pr_data.csv.")

required_msli_columns = {"GitHub Username", "Code URL"}
if not required_msli_columns.issubset(msli_df.columns):
    raise ValueError("One or more required columns are missing in msli.csv.")

# List to accmulate the PRs not found in msli.csv
not_found = []

# find through each record in onboard_pr_data.csv
for index, row in onboard_df.iterrows():
    pr_link = row["PR Link"]
    author = row["Author"]
    match = msli_df[(msli_df["GitHub Username"] == author) & (msli_df["Code URL"] == pr_link)]
    
    # If no matching record is found, add this PR record to the not_found list.
    if match.empty:
        not_found.append({
            "PR Number": row["PR Number"],
            "Author": author,
            "PR Link": pr_link
        })
        


# Write the records not found in msli.csv to a new CSV file
if not_found:
    not_found_df = pd.DataFrame(not_found)
    not_found_df.to_csv("pr_not_found.csv", index=False)
