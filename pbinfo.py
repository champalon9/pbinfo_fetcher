#!/usr/bin/python

from lxml import html
import requests
import sys
import os

if len(sys.argv) == 1:
    sys.exit("Usage: pbinfo NUMBER...")

for p in sys.argv[1:]:
    if not p.isdecimal():
        raise SystemExit("Please use an integer bigger than 0!")
    link = "https://www.pbinfo.ro/probleme/" + p
    print(link)

    try:
        page = requests.get(link)
    except requests.exceptions.RequestException as e:
        # raise SystemExit(e)
        raise SystemExit(
            "There has been a problem connecting to pbinfo.ro. Please check your internet connection.")

    tree = html.fromstring(page.content)

    try:
        enunt = tree.get_element_by_id("enunt").text_content()
    except:
        # raise SystemExit("The problem " + p + " does not exist!")
        print("The problem " + p + " does not exist!")
        continue

    enunt = enunt.replace(
        "(adsbygoogle = window.adsbygoogle || []).push({});", "")
    enunt = enunt.replace("\t", "")
    enunt = enunt.strip("\n")
    enunt = enunt.replace("\n\n\n", "")

    enunt = enunt.splitlines(True)

    enunt = ["//" + word for word in enunt]

    try:
        os.makedirs(p)
    except FileExistsError:
        pass

    path = p + "/main.cpp"
    with open(path, 'w') as source:
        source.writelines(enunt)
