# broken_link_scanner
This a small python script that checks for broken links

## What it does
This script takes a web page and renderes its HTML. It then finds all the a elements and compiles a list of links /urls. 

Then, the script sends a request to each URL to see that it responds with either 200, 201, or 301.
If the URL responds with anything else, it's considered a broken link and is logged into a csv.

## Requirements
This server stress script makes use of the requests and requests_html python packages. Install them before you run the script.
https://pypi.org/project/requests-html/
https://2.python-requests.org/en/master/

requests_html makes use of pypteer. On first run, requests_html downloads and sets up on your machine. 

Code was written in python3

## How to run
Simply run the main file run.py

