# -*- coding: utf-8 -*-
# @Time     : 2018/10/08 
# @Author   : liguibin
#
#usage: xmlyMp3Dl.py [-h] [-v] [-o OUTPUT] fileName
#
#manual to this script
#
#optional arguments:
#  -h, --help            show this help message and exit
#  -v, --verbosity       increase output verbosity
#  -o OUTPUT, --output OUTPUT
#                        output file name


import os
import re
import sys
import json
import requests
import argparse
import subprocess
from bs4 import BeautifulSoup


headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    }

defaultOutputFile = 'dl_ymq.sh'

defaultAlbumUrl = '2018.9.8中科大60周年校庆五羽轮比团体赛.htm'

postUrl = 'http://user.ymq.me/public/live/getDemandInfo'

reUrl = r'http://apply.ymq.me/Index/video/demand/id/\d+/macthid/\d+.html'

payloadJson = {
    "body":
    {"live_type":2,
        "data":{
            "raceId":"rid",
            "matchId":"mid"
        }
    },
    "header":
    {
        "token":"",
        "from":"wx"
    }
}

payloadStr = json.dumps(payloadJson)

def getM3u8(payloadData):
    res = requests.post(postUrl, data=json.dumps(payloadData), headers=headers)
    js = json.loads(res.text)
    
    if res.status_code == 200 and js["message"] == '成功':
        return js["data"]["hlsLive_url"]
    else:
        print("Error while geting m3u8 of "+postUrl)
        print(js)
    

def main(webUrl, outputFile):
    f = open(outputFile, 'w+')

    htmlfile=open(webUrl, 'r')
    htmlpage = htmlfile.read()
    soup = BeautifulSoup(htmlpage, "html.parser")

    matchTagList = soup.findAll('div', attrs={'class': 'cont'})
    matchNum = len(matchTagList)
    videoNum = 0

    print('###---', soup.title.string, matchNum, 'matches ---###')

    for i in range(matchNum):
        matchUrl = matchTagList[i].a['href']

        if re.match(reUrl, matchTagList[i].a['href']):
            videoNum += 1

            raceId = re.findall(r'\d+',matchTagList[i].a['href'])[0]
            matchId = re.findall(r'\d+',matchTagList[i].a['href'])[1]

            #remove extra space
            matchName = re.sub(r'\s+', '_', matchTagList[i].a.text.strip())
            matchName = re.sub(r'_弃_', '', matchName)
            matchName = re.sub(r'比赛结束_', '', matchName)
            matchName = matchName+'.mp4'

            payloadString = payloadStr.replace('rid', raceId).replace('mid', matchId)
            payloadData = json.loads(payloadString)
            m3u8Url = getM3u8(payloadData)

            if m3u8Url == None:
                print("Failed to get m3u8 of", matchName)
            else:
                print('youtube-dl -o', matchName, m3u8Url)
                print('youtube-dl -o', matchName, m3u8Url, file=f)

    print('###---Total', videoNum ,'match Videos ---###')

    f.close()
    p = subprocess.Popen(["chmod", "+x", outputFile], stdout=subprocess.PIPE)
    print('save result to excutable file : ' + outputFile)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='download all audioes in ximalay album like :' + defaultAlbumUrl)
    parser.add_argument('url', type=str, help="web url need to download")
    parser.add_argument("-o", "--output", help="output file name")
    parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")

    args = parser.parse_args()
    webUrl = args.url
    outputFile = args.output

    # input url format checker
    if os.path.isfile(webUrl):
        pass
    else:
        sys.exit('\n ## Error : unrecognize url, please input correct url format like : ' + defaultAlbumUrl)

    if args.output:
        outputFile = args.output
    else:
        outputFile = defaultOutputFile

    print('## Info : save result to : ',outputFile)

    main(webUrl, outputFile)