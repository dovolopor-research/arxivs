import re
import time
import urllib
import datetime

import pytz
import feedparser


def get_paper(tags, days):
    cats = "+OR+".join(tags)
    # submittedDate or lastUpdatedDate
    sort = "lastUpdatedDate"
    total_results = 1000
    results_per_iteration = 100
    today = datetime.datetime.today()
    print(f">> arxivs: # start {today}")

    paper_list = []
    break_key = 0
    for i in range(0, total_results, results_per_iteration):
        print(f"\n>> arxivs: ## {i} - {i + results_per_iteration} ##")

        query = f"http://export.arxiv.org/api/query?search_query=cat:{cats}&sortBy={sort}&start={i}&max_results={results_per_iteration}"
        response = urllib.request.urlopen(query).read()
        feed = feedparser.parse(response)

        for index, entry in enumerate(feed.entries):
            published_time = datetime.datetime.fromtimestamp(time.mktime(entry["updated_parsed"])).replace(tzinfo=pytz.UTC)
            # to current time zone
            published_time = published_time.astimezone(pytz.timezone("Asia/Shanghai")).replace(tzinfo=None)
            delta_time = today - published_time
            entry["updated_time"] = published_time

            if delta_time.days <= days:
                e_id = entry["id"].split("abs/")[1]
                title = entry["title"]
                summary = entry["summary"]

                print(f"\n>> arxivs: {index+1} {title}")

                if "github" in summary:
                    ptn = re.compile("github.com/[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]")
                    result = ptn.findall(summary)
                    if result:
                        entry["github"] = f"https://{result[0]}"
                        print(">> arxivs: [GITHUB] " + entry["github"])

                paper_list.append(entry)
            else:
                break_key = 1
                break

            time.sleep(3)

        if break_key:
            break

        time.sleep(3)

    print(">> arxivs: # end\n")
    return paper_list
