import pandas as pd
import time

# Load the data from both CSV files
submission_df = pd.read_csv("submission_labels.csv")
msli_df = pd.read_csv("msli.csv")

if "URL" not in submission_df.columns or "Code URL" not in msli_df.columns:
    print("Required columns not found in CSV files.")
    exit()

msli_urls = set(msli_df["Code URL"].dropna())

for url in submission_df["URL"].dropna():
    if url in msli_urls:
        print(f"{url} yes")
    else:
        print(f"{url} no")
    time.sleep(0.5)
