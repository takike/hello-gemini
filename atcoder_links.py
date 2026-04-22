import sys
import requests
from bs4 import BeautifulSoup

def parse_tasks(html):
    soup = BeautifulSoup(html, "html.parser")
    # AtCoderの課題テーブルは通常 div.table-responsive 内の table
    table = soup.find("table")
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

def fetch_tasks(contest_id):
    url = f"https://atcoder.jp/contests/{contest_id}/tasks"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Could not fetch tasks for contest '{contest_id}' (Status: {response.status_code})", file=sys.stderr)
        sys.exit(1)
    return parse_tasks(response.text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python atcoder_links.py <contest_id>")
        sys.exit(1)
    
    contest_id = sys.argv[1]
    tasks = fetch_tasks(contest_id)
    
    if not tasks:
        print(f"No tasks found for contest '{contest_id}'.")
        return

    for task in tasks:
        print(f"- [{task['label']} - {task['title']}]({task['url']})")

if __name__ == "__main__":
    main()
