import os
import pandas as pd

urlCFGFile = 'cfg\\urltype.cfg'

def converttypetoURL(data):
    urldict = geturldict()
    for i in range(0, len(data)):
        entry = data[i]
        urlkey = entry['url']
        data[i]['url'] = urldict[urlkey]

def geturldict():
    file = os.path.curdir + "\\" + urlCFGFile
    urldict = dict()
    with open(file,'r') as cfgFile:
        urls = cfgFile.read().splitlines()
        for entry in urls:
            key, url = entry.split(":")
            urldict[int(key)] = url
    return urldict

def converttoDF(log_data):
    converttypetoURL(log_data)
    #print(log_data)
    df = pd.DataFrame(log_data)
    return df

def get_freq(df):
    grouped_multiple = df.groupby(['method', 'url'])
    count = grouped_multiple.size()
    count_df = count.to_frame()
    sorted_count_df = count_df.sort_values(0,ascending=False)
    return sorted_count_df

def print_res_time_details(df):
    grouped_multiple = df.groupby(['method', 'url']).agg({'response_time': ['min', 'max', 'mean']})
    grouped_multiple.columns = ['Min Time', 'Max Time', 'Average Time']
    grouped_multiple = grouped_multiple.reset_index()
    print(grouped_multiple)
