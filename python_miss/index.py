import httpx
import re
import sys


def save_to_file(filename,contents):
    fh = open(filename, 'w', encoding='utf-8')
    fh.write(contents)
    fh.close()


headers_dict = {
"authority":"missav.com",

"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
"method":"GET", 
"path":"/dm264/chinese-subtitle",
"scheme": "https", 
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding":"gzip, deflate, br, zstd", 
"Accept-Language" : "zh-CN,zh;q=0.9" ,
"Cache-Control" : "max-age=0",
"If-Modified-Since":"Mon, 22 Apr 2024 01:07:50 GMT",
"Referer" : "https://missav.com/",
"Sec-Ch-Ua" : "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",

"Sec-Ch-Ua-Mobile" : "?0",
"Sec-Ch-Ua-Platform" : "\"Windows\"" ,
"Sec-Fetch-Dest" : "document",
"Sec-Fetch-Mode" : "navigate",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-User":"?1",
"Upgrade-Insecure-Requests" : "1",

}

cookie_dict = {"user_uuid":"c1451100-3673-4356-bb17-7dd48e681f4d",
"_ga":"GA1.1.1932232403.1713748071",
"cf_clearance":"yZyyEm716cjx1QnVhtILiZFOWDWij7cE.IslUW46Rk4-1713748070-1.0.1.1-qC0AZGHfj3IXmNjGHShg0oIzwC49m7G0wzEDJM.fndaUqcupgxQAAbzSFLBj4g8.hxVUoSrNiLlLmAMxoyBaxw",
"_ga_Z3V6T9VBM6":"GS1.1.1713748071.1.1.1713748599.0.0.0"
}


def request_missav_main_page(str):
    url_str_page = "https://missav.com"+str
    res = httpx.get(url=url_str_page, headers = headers_dict, cookies=cookie_dict ,timeout=10)
    print(res.status_code)
    print(res.text)
    return res.text

def request_missav_search_page(search_text):
    url_str_search = "https://missav.com/search/"+str(search_text)
    res = httpx.get(url=url_str_search, headers = headers_dict, cookies=cookie_dict ,timeout=10)
    return res.text

def pattern_data(text):
    pattern_href_name_dict = r"<a class=\"text-secondary group-hover:text-primary\" href=\"(.*?)\".*?>(.*?)</a>"
    result_href_name = re.findall(pattern_href_name_dict,text ,re.S)

    pattern_num = r"<span class=\"text-gray-500 sm:text-sm\" id=\"price-currency\">(.*?)</span>"
    result_num = re.findall(pattern_num,text ,re.S)
    print("页数数量：")
    print(result_num)


    for item in result_href_name:
        if(len(item)) == 2:
            print(item[0] +": "+item[1])


if __name__ == "__main__":
    text = ""
    if len(sys.argv) == 2:
        type = sys.argv[1]
        if type == 1:
            text = request_missav_main_page("/dm73/actresses/美咲佳奈")
        elif type == 2:
            text = request_missav_search_page("中文字幕")
        else:
            text == request_missav_main_page("")
    else:
        text == request_missav_main_page("")
    
    pattern_data(text)