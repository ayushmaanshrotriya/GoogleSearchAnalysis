from re import search
from turtle import color
import pandas as pd
import pytrends
import matplotlib.pyplot as plt
import io
import urllib,base64
from urllib.parse import quote
from pytrends.request import TrendReq

def graph(qu):
    trends = TrendReq()
    trends.build_payload(kw_list=[qu],timeframe='2020-01-01 2021-01-01',geo='IN')
    data = trends.interest_by_region()
    data = data.sort_values(by=qu, ascending=False)
    data = data.head(10)
    data.reset_index().plot(x="geoName", y=qu, figsize=(10,5), kind="barh")

    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='jpeg')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = quote(string)

    return uri