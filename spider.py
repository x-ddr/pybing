import requests
import parsel
import re



for page in range (84,135):
    print('-------------------正在爬取第{}页数据------------------'.format(page))
    # proxies = {'http': '60.190.23.50:8080'
    #            }
    base_url = 'https://bing.ioliu.cn/?p={}'.format(str(page))
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}


    response=requests.get(url=base_url, headers=headers)
    print(response)

    html_data=response.text
    # print(html_data)
    selector = parsel.Selector(html_data)
    result_list=selector.xpath('//div[@class="card progressive"]')
    # print(result_list)
    for result in result_list:
        img_url= result.xpath('./a[@class="mark"]/@href').get()
        title= result.xpath('./div[@class="description"]/h3').get()
        no_title_data = title.replace('<h3>', '').replace('</h3>', '')
        # img_url_a =img_url.replace('=[******]','download')
        # img_url_a = img_url.replace('home_'+'[1-9][0-9]*', 'download')
        img_url_a =re.sub('home_'+'[1-9][0-9]*','download',img_url)
        # print(no_title_data,":-----",img_url_a)
        title_all_no = no_title_data.replace('/', '')
        # print(title_all_no)



        title_all=title_all_no+".jpg"
        # print(img_url_a)
        # print(title_all, 'https://bing.ioliu.cn'+img_url_a)
        imgurl='https://bing.ioliu.cn'+img_url_a
    #
        img_data=requests.get(url=imgurl,headers=headers).content
        no_title_data = title.replace('/', '').replace('\\', '').replace('>', '')
        print(no_title_data)

        with open('pic/'+title_all,mode='wb')as f:
                f.write(img_data)
                print(title_all,":保存完成")
            # (3)操作
