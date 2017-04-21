#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fetch complete list of companies registered with PrivacyShield.

License: GNU GPL v2 or later at your choice
"""

import httplib
import lxml.html
import urllib
import urllib2
import urlparse

def participant(url):
    response = urllib2.urlopen(url)
    root = lxml.html.fromstring(response.read())
    info = {}
    for section in root.cssselect("div.panel-default"):
        c = section.cssselect("div h2")[0].text_content()
        #print c
        if 'Industries' == c:
            pass
        elif 'Participation' == c:
            for p in section.cssselect("div.about"):
                (f,v) = p.text_content().split(":")
                info[f.strip()] = v.strip()
                (f,v) = section.cssselect("div.col-md-12 p")[1:]
                info[f.text_content().strip()] = v.text_content().strip()
            pass
        elif 'Privacy Policy' == c:
            pass
        elif 'Dispute Resolution' == c:
            pass
        elif 'Other Covered Entities' == c:
            pass
        else:
            raise Exception("unhandled class %s" % c)
        #print section.text_content()

    return info

def allCompanies():
    baseurl = "https://www.privacyshield.gov/list"
    posturl = "https://www.privacyshield.gov/participant_search"

    response = urllib2.urlopen(baseurl)
    root = lxml.html.fromstring(response.read())
    total = int(root.cssselect("div.containerInternal")[0].text_content().split(':')[1])
    offset = 0

    while offset < total:
        #print offset

        data = urllib.urlencode({'offsetChange' : str(offset)})
        req = urllib2.Request(posturl, data)
        response = urllib2.urlopen(req)
        top= response.read()

        root = lxml.html.fromstring(top)
        for e in root.cssselect("div.each_result h4"):
            link=e.cssselect("a")[0]
            org = e.text_content()
            url = urlparse.urljoin(posturl, link.attrib['href'])
            info = participant(url)
            d = {
                'org' : org,
                'url' : url,
                'info': info,
                }
            print d
        offset = offset + 10

def main():
    allCompanies()

if __name__ == '__main__':
    exit(main())
