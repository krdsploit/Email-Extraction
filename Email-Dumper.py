from http.client import responses
from rich.console import Console
from rich.table import Table
import requests
import json
from rich.tree import Tree
from rich import print


table = Table(title="Web-Extractor-Actions")


table.add_column("Attacks", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("OS", justify="right", style="green")

table.add_row("Email Extractions", "Extraction The Email Address", "Web Pages")

target = input("Enter The Target Website $ ")


url = "https://email-search16.p.rapidapi.com/search-emails"

querystring = {"query":target,"email_domain":"gmail.com","limit":"100"}

headers = {
	"X-RapidAPI-Key": "10fe8349fdmshe65e961fab46a92p17d5bfjsnda13ecd4b9b3",
	"X-RapidAPI-Host": "email-search16.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

responses = response.text
dumper = json.loads(responses)

print(dumper["data"])

msg = input("Do you want to save this email from txt file : ")

if msg=="yes":
	f = open("Emails", "a")
	f.write(dumper)
	f.close()
else:
	quit()