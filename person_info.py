# -*- coding: utf-8 -*-
import os
import re
import sys
import json
import xlwt
import requests
import argparse
import subprocess
from bs4 import BeautifulSoup


headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
    }


jsonFileName = 'match_info.json'
xlsFileName = 'info.xls'
defaultAllMatchUrl = 'http://apply.ymq.me/Index/Index/match_all/id/947.html'

matchRange = range(50, 1118)
minMatchIndex = 1
maxMatchIndex = 50

def matchName():
    print('get all match name from %d-%d'%(minMatchIndex, maxMatchIndex))

    for i in range(minMatchIndex, maxMatchIndex):
        res = requests.get(defaultAllMatchUrl.replace('947', str(i)), headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        if soup.title:
            print(i, ':' , soup.title.text)
        else:
            print(i, ':', 'match not found')



def readInfoToXls(inputFileName, outputFileName):
    print('extract person info from match info')

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')

	# 设置表头
    worksheet.write(0, 0, label='name')
    worksheet.write(0, 1, label='sex')	
    worksheet.write(0, 2, label='age')
    worksheet.write(0, 3, label='birthday')
    worksheet.write(0, 4, label='phone')
    worksheet.write(0, 5, label='club')
    worksheet.write(0, 6, label='idCard')	

	# 读取json文件
    with open(inputFileName, 'r') as f:
        jsonMatch = json.load(f)

    i = j = k = 0
    val1 = val2 = val3 = val4 = val5 = val6 = val7 = val8 = 1

    nameList = []
    for i in range(0, len(jsonMatch['detail']['matches'])):

        for j in range(0, len(jsonMatch['detail']['matches'][i])):

            if jsonMatch['detail']['matches'][i][j] == None:
                pass
            else:
                for onetwo in ['playerOnes', 'playerTwos']:
                    p = 0

                    for p in range(0, len(jsonMatch['detail']['matches'][i][j][onetwo])):
                        playerInfo = jsonMatch['detail']['matches'][i][j][onetwo][p]

                        #print(playerInfo)

                        if playerInfo['name'] in nameList:
                            pass
                        else:
                            nameList.append(playerInfo['name'])

                            print(i, playerInfo['name'], playerInfo['sex'], playerInfo['age'],
                                playerInfo['birthday'], playerInfo['phone'], playerInfo['club'], playerInfo['idcard'])

                            for key in playerInfo:
                                if key == 'name':
                                    worksheet.write(val1, 0, playerInfo[key])
                                    val1 += 1
                                elif key == 'sex':
                                    worksheet.write(val2, 1, playerInfo[key])
                                    val2 += 1
                                elif key == 'age':
                                    worksheet.write(val3, 2, playerInfo[key])
                                    val3 += 1
                                elif key == 'birthday':
                                    worksheet.write(val4, 3, playerInfo[key])
                                    val4 += 1
                                elif key == 'phone':
                                    worksheet.write(val5, 4, playerInfo[key])
                                    val5 += 1
                                elif key == 'club':
                                    worksheet.write(val6, 5, playerInfo[key])
                                    val6 += 1
                                elif key == 'idcard':
                                    worksheet.write(val7, 6, playerInfo[key])
                                    val7 += 1
                                else:
                                    pass

    workbook.save(outputFileName)



if __name__ == '__main__':
    readInfoToXls(jsonFileName, xlsFileName)
    #matchName()
