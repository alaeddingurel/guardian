#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:13:57 2019

@author: user
"""
import requests

d = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11",
 "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22",
 "23", "24", "25", "26", "27", "28", "29", "30", "31"
 ]

m = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

y = ["1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]



            
            






for year in y:
    for idx, month in enumerate(m[0:11]):
        request = requests.get("https://content.guardianapis.com/search?from-date="+year+"-"+month+"-01&to-date="+year+"-"+m[idx+1]+"-01&page-size=200&page=1&api-key=test")
        print(request.url)
        pagenumber = request.json()['response']['pages']
        with open(year+"-"+month, "a") as file:
            for i in range(1, pagenumber+1):
                request = requests.get("https://content.guardianapis.com/search?from-date="+year+"-"+month+"-01&to-date="+year+"-"+m[idx+1]+"-01&page-size=200&page="+str(i)+"&api-key=test")
                print(request.url)
                all_links = request.json()['response']['results']
                for link in all_links:
                        print(link['webUrl'])
                        file.write(link['webUrl']+"\n")