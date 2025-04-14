import csv

# Input files
onboard_file = "onboard_pr_data.csv"
msli_file = "msli.csv"
output_file = "unmatched_pr_links.csv"

def load_code_urls_from_msli(filename):
    code_urls = set()
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            code_urls.add(row.get("Code URL", "").strip())
    return code_urls

def find_unmatched_pr_links(onboard_filename, code_urls):
    unmatched = []
    with open(onboard_filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pr_link = row.get("PR Link", "").strip()
            if pr_link not in code_urls:
                unmatched.append({"PR Link": pr_link, "Matched": "No"})
    return unmatched

def save_unmatched(results, output_filename):
    with open(output_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["PR Link", "Matched"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

def main():
    code_urls = load_code_urls_from_msli(msli_file)
    unmatched_results = find_unmatched_pr_links(onboard_file, code_urls)
    save_unmatched(unmatched_results, output_file)
    print(f"Total unmatched PR links: {len(unmatched_results)}")
    print(f"Results saved in: {output_file}")

if __name__ == "__main__":
    main()
