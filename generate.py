import requests
from bs4 import BeautifulSoup

from Job import Job

# Font for scrap data
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# Get all cards with job info
job_elements = results.find_all("div", class_="card-content")

jobs = []

# Get info from each card
print("Getting jobs info...")
for job_element in job_elements:
    title = job_element.find("h2", class_="title is-5").text
    company = job_element.find("h3", class_="subtitle").text
    location = job_element.find("p", class_="location").text
    date = job_element.find("time").text
    img = job_element.find("img")["src"]
    link = job_element.findAll("a", class_="card-footer-item")[1]["href"]

    job = Job(title, company, img, date, link, location)
    jobs.append(job)


# Create html file with jobs info
print("Creating HTML file...")
strHtml = '<html>'

with open("style.css", "r") as archivo:
    styleContent = archivo.read()

strStyle = '<style>' + styleContent + '</style>'

strHeader = '<header><h1>Jobs List</h1></header>'

strTable = '<table><tr><th>Title</th><th>Company</th><th>Img</th><th>Location</th><th>Date</th><th>Link</th></tr>'

# For each job create a row
for job in jobs:
    strRW = "<tr><td>" + job.title + "</td><td>" + job.company + "</td><td>" + '<img src="'+job.img+'"/>' + \
        "</td><td>" + job.location + "</td><td>" + job.date + \
            "</td><td>" + '<a href="'+job.link+'">link</a>'

    strTable = strTable+strRW

strTable = strTable+"</table></html>"

# Concat all html elements (style, header and table)
strHtml = strHtml + strStyle + strHeader + strTable

hs = open("jobsList.html", 'w')
hs.write(strHtml)

print("HTML file created successfully! jobsList.html")