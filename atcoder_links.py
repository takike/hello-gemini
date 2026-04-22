from bs4 import BeautifulSoup

def parse_tasks(html):
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find_all("tr")
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
