#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, os, threading
from lxml import etree

Url = "https://www.moestack.com/all"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}


def Mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        pass


def Get_Page(x):
    Page = requests.get(x, headers=headers)
    Page.encoding = "utf-8"
    Page = Page.text
    Page = etree.HTML(Page)
    return Page


def end():
    ImgUrl = GetImgUrl[i]
    save_img = requests.get(ImgUrl, headers=headers)
    with open(r"Moe/" + Title[0] + "/" + ImgUrl[-27:], "wb") as fh:
        fh.write(save_img.content)
        fh.flush()


def DownImg():
    global i
    global t
    path = "Moe/" + Title[0] + "/"
    Mkdir(path)
    threads = []
    for i in range(len(GetImgUrl)):
        t = threading.Thread(target=end, daemon=True)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("下载完成")


def OnePageDown(x):
    global Title, GetImgUrl
    GetImgUrl = Get_Page(x).xpath('//*/div[2]/div/div[1]/p/img/@src')
    Title = Get_Page(x).xpath('//*[@class="entry-title"]/text()')
    print("标题：" + Title[0])
    print("一共有%d张图片" % len(GetImgUrl))
    DownImg()


def PageDown(x):
    ImgPageUrl = Get_Page(x).xpath('//*[@class="entry-media"]/div/a/@href')
    for i in ImgPageUrl:
        OnePageDown(i)


def AllDown(x):
    # PageNum = Get_Page(x).xpath('/html/body/div/div[3]/div/div[2]/div/div/main/div[2]/ul/li[6]/a/text()')
    print("1")
    PageNum=Get_Page(x).xpath('//ul[@class="page-numbers"]/li[6]/a/text()')
    print("全站共有%d页" % int(PageNum[0]))
    for i in range(int(PageNum[0])):
        i = i + 1
        if i == '1':
            PageUrl = "https://www.moestack.com/all"
            PageDown(PageUrl)
        else:
            PageUrl = "https://www.moestack.com/all" + "/page/" + str(i)
            PageDown(PageUrl)


def main():
    # print("菜单：\n1.单页下载\n2.页面下载\n3.全站下载(Boom!!!)")
    # Choice = input("请选择：")
    # if Choice == '1':
    #     ImgPageUrl = input("请输入链接：")
    #     OnePageDown(ImgPageUrl)
    # elif Choice == '2':
    #     PageUrl = input("请输入页面链接：")
    #     PageDown(PageUrl)
    # elif Choice == '3':
        AllDown(Url)


if __name__ == "__main__":
    main()
