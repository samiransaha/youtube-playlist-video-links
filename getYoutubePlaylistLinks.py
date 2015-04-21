#!/usr/bin/python

import urllib2
import re
import json

url = raw_input('Enter the Youtube Playlist url : ')

print 'Your given Youtube Playlist url is :' + url
temp = url.find('www.youtube.com/playlist')

if temp == -1:
    print "Given url is not a valid one.. check the url"
    exit()

pl = re.search('(?<=list=)(.*)', url).group(0)
j = urllib2.urlopen('http://gdata.youtube.com/feeds/api/playlists/' + pl + '?v=2&alt=json&feature=plcp')
j_obj = json.load(j)

              
filename = raw_input('Enter the file name(without extension) :')
obj = open(filename + '.txt', 'w')
for link in j_obj["feed"]["entry"]:
    obj.write(re.match( '(.*)&feature=youtube_gdata', link["link"][0][u'href'], 0).group(1) + '\n')

obj.close()


