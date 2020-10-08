import os
import re

methodCFGFile = 'cfg\\methodList.cfg'
urlCFGFile = 'cfg\\urltype.cfg'

def filterDataByMethod(fileData):
    file = os.path.curdir + "\\" + methodCFGFile
    with open(file,'r') as cfgFile:
        methods = list(cfgFile.read().splitlines())

    filteredData = dict()
    for method in methods:
        filteredData[method] = list()

    for entry in fileData:
        method = entry['method']
        entryCopy = entry.copy()
        entryCopy.pop('method', "Key not found")
        filteredData[method].append(entryCopy)

    for method in methods:
        if len(filteredData[method]) == 0:
            filteredData.pop(method, "Key not found")


    return filteredData


def filterDataByURL(fileData):
    file = os.path.curdir + "\\" + urlCFGFile
    urldict = dict()
    with open(file,'r') as cfgFile:
        urls = cfgFile.read().splitlines()
        for entry in urls:
            key, url = entry.split(":")
            if "{id}" in url:
                url = url.replace("{id}", "[0-9]+")
            urldict[int(key)] = url

    filteredData = dict()
    for url in urldict:
        filteredData[url] = list()

    for entry in fileData:
        url = entry['url']
        entryCopy = entry.copy()
        entryCopy.pop('url', "Key not found")
        for urlkey, urltype in urldict.items():
            if re.search(urltype, url):
                filteredData[urlkey].append(entryCopy)
                break

    for url in urldict:
        if len(filteredData[url]) == 0:
            filteredData.pop(url, "Key not found")

    return filteredData
