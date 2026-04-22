import argparse
import sys
import requests
from bs4 import BeautifulSoup

def parse_tasks(html):
    soup = BeautifulSoup(html, "html.parser")
    # AtCoderの課題テーブルは通常 id="main-container" 内の table
    main_container = soup.find(id="main-container")
    if not main_container:
        return []
    
    table = main_container.find("table")
    if not table:
        return []
    
    rows = table.find("tbody").find_all("tr") if table.find("tbody") else table.find_all("tr")
    tasks = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            label_link = cols[0].find("a")
            title_link = cols[1].find("a")
            if label_link and title_link:
                label = label_link.text.strip()
                title = title_link.text.strip()
                url = "https://atcoder.jp" + title_link["href"]
                tasks.append({"label": label, "title": title, "url": url})
    return tasks

def fetch_tasks(contest_id, lang="ja"):
    url = f"https://atcoder.jp/contests/{contest_id}/tasks"
    params = {"lang": lang}
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code != 200:
            print(f"Error: Could not fetch tasks for contest '{contest_id}' (Status: {response.status_code})", file=sys.stderr)
            sys.exit(1)
        return parse_tasks(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: Network request failed: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Generate Markdown links for AtCoder contest problems.")
    parser.add_argument("contest_id", help="The ID of the AtCoder contest (e.g., abc300)")
    parser.add_argument("--lang", default="ja", help="Language of the problem titles (default: ja)")
    
    args = parser.parse_args()
    
    tasks = fetch_tasks(args.contest_id, args.lang)
    
    if not tasks:
        print(f"No tasks found for contest '{args.contest_id}'.")
        return

    for task in tasks:
        print(f"- [{task['label']} - {task['title']}]({task['url']})")

if __name__ == "__main__":
    main()
