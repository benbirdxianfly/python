#!/usr/local/bin/python
# -*- coding:utf-8 -*-

"""
 @author: valor
 @file: file.py
 @time: 2018/11/5 10:59
"""

import os
import json
import time


# 删除每行文字最后的换行符
def delete_line_breaks(line: str):
    if line.__contains__('\n'):
        line = line.rstrip('\n')
    return line.strip()

  #  return line.rstrip('\n') if line.__contains__('\n') else line


class File:
    def __init__(self):
        self._basePath = os.path.dirname(__file__)

    # 打开文件 替换换行符为 \n
    def open(self, path: str, mode='r'):
        return open(file=self._basePath + path, mode=mode, newline='\n',encoding='utf-8')

    def dump(self, _list, key):
        stamp = time.strftime("%Y%m%d", time.localtime())

        if not os.path.exists(self._basePath + '/result/' + stamp):
            os.makedirs(self._basePath + '/result/' + stamp)

        with self.open(path='/result/' + stamp + '/' + key + '.txt', mode='a') as f:
            for e in _list:
                f.write(str(e) + '\n')
            f.close()
        # 清空列表
        _list.clear()

    def json(self):
        with self.open('\\config\\config.json') as f:
            o = json.load(f)
            f.close()
        return o

    # def deleteline():
    #     with open("fileread.txt","r",encoding="utf-8") as f:
    #         lines = f.readlines()
    #         #print(lines)
    #     with open("fileread.txt","w",encoding="utf-8") as f_w:
    #         for line in lines:
    #             if "tasting123" in line:
    #                 continue
    #             f_w.write(line)
