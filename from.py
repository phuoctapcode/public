from time import sleep
from threading import Thread
import threading, time, requests, random, re, os, sys, html , json, urllib3, hashlib, platform, uuid, socket, getpass ,datetime, urllib.parse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup
from retrying import retry
from colorama import init, Fore, Back, Style
sys.stdout.reconfigure(encoding='utf-8')
def Run(mail_cc,stt,tongmail,proxy1):

    check_mail = re.search(':', mail_cc)
    if check_mail == None:
        mail = mail_cc
        mail = mail.lower()
        
        
    else:
        mail = mail_cc.split(':')[0]
        mail = mail.lower()
    session2 = requests.session()
    proxy = {
                
                'http': f'http://{proxy1}',
                'https': f'http://{proxy1}'
                # 27.76.243.186:62503:phuoc_gJK7b:40GR7XwZ
            }


    with open('resuts/Danh Sách Số Lượng Mail Đã Check.txt','a', encoding= "utf-8") as somail:
            somail.write('\n'+f'')
    cookies = {
                'datr': 'DFMRZAevF9WqfLvVzHFvzhUm',
                'sb': 'DlMRZIA-YX9q5lW9q1ztkj-Z',
                'fr': '0SxrXsleBbVv3S7N8.AWWf06Q9R6hBaZxB7i34Y27p4j0.BkInYC.At.AAA.0.0.BkKu6L.AWXlz2V-58s',
                'wd': '738x963',
                'sfiu': 'AYhIwawCFYVSDMkSq4Dz_BUEVfZbb4D-TZ9ZIqD44RevW7KoqqWVEqDd-uGcERgQmiVvzBEZRqv7amLTk6ULYpT00jhJIAfvzF5HAFNuiR7WWn0ul1mmYWqzel30l7qnw27y5oA6EmzhfRJyxu_irC-BJxDuc3yY0bdBT7qw9gHvcWFd1-8vI_bUa_k05kejD10r1a3t3CVL_bC697g2Uscv',
        }
    headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'datr=DFMRZAevF9WqfLvVzHFvzhUm; sb=DlMRZIA-YX9q5lW9q1ztkj-Z; fr=0SxrXsleBbVv3S7N8.AWWf06Q9R6hBaZxB7i34Y27p4j0.BkInYC.At.AAA.0.0.BkKu6L.AWXlz2V-58s; wd=738x963; sfiu=AYhIwawCFYVSDMkSq4Dz_BUEVfZbb4D-TZ9ZIqD44RevW7KoqqWVEqDd-uGcERgQmiVvzBEZRqv7amLTk6ULYpT00jhJIAfvzF5HAFNuiR7WWn0ul1mmYWqzel30l7qnw27y5oA6EmzhfRJyxu_irC-BJxDuc3yY0bdBT7qw9gHvcWFd1-8vI_bUa_k05kejD10r1a3t3CVL_bC697g2Uscv',
        'origin': 'https://www.facebook.com',
        'pragma': 'no-cache',
        'referer': 'https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-asbd-id': '198387',
        'x-fb-lsd': 'AVo85eGdX-s',
        'Connection': 'keep-alive',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache'
        
    }
    params = {
        'ctx': 'recover',
    }
    data = {
        'jazoest': '2891',
        'lsd': 'AVo85eGdX-s',
        'email': mail,
        'did_submit': '1',
        '__user': '0',
        '__a': '1',
        '__dyn': '7xe6E5aQ1PyUbFuC1swgE98nwgU29zEdEc8uwdK0lW4o3Bw5VCwjE3awbG782Cw8G1Qw5Mx61vw5zwwwi81nE1u83mwaS0zE1bE1AE17U2ZwrU19E36w',
        '__csr': '',
        '__req': '3',
        '__hs': '19450.BP:DEFAULT.2.0..0.0',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': '1007231265',
        '__s': 'sv0m61:jrp2rg:e8j18j',
        '__hsi': '7217843798143222548',
        '__comet_req': '0',
        '__spin_r': '1007231265',
        '__spin_b': 'trunk',
        '__spin_t': '1680535217',
    }
    checklk = session2.post(
        'https://www.facebook.com/ajax/login/help/identify.php',
        params=params,
        # cookies=cookies,
        headers=headers,
        data=data,
        proxies=proxy,
    )
    checklk.close()
    if checklk.status_code != 200:
        print(f'\033 \033[1;93m>> \033[1;91m[{mail}]  \033[1;96m=>  \033[1;97mStatus=Cần Check lại ở status]')
        with open('resuts/Danh Sách Mail Cần Check Lại.txt','a', encoding= "utf-8") as mail_an:
                            mail_an.write('\n'+f'{mail_cc}')
    else:
        
        checklk = checklk.text
        # print(checklk)
        # exit()
        kq_checklk = re.search('#account_search",false,', checklk)
        if kq_checklk != None:
            print(f'\033 \033[1;93m>> \033[1;91m[{mail}]  \033[1;96m=>  \033[1;91mStatus=[Không Liên Kết]')

        else:
            if 'name="cuid" value="' in checklk:
                ldata = checklk.split('name="cuid" value="')[1].split('"')[0]
                
                print(f'\033 \033[1;93m>> \033[1;91m[{mail}]  \033[1;96m=>  \033[1;97mStatus=Cần Check lại ở thiết ldata mới là {ldata}]')
            elif 'ldata' in checklk:
                ldata = checklk.split('ldata=')[1].split('"')[0]

                print(f'\033 \033[1;93m>> \033[1;91m[{mail}]  \033[1;96m=>  \033[1;95mStatus= {ldata}]')
            else:
                print(f'\033 \033[1;93m>> \033[1;91m[{mail}]  \033[1;96m=>  \033[1;94mStatus= {}')
                
                
def main():
    open('resuts/Danh Sách Số Lượng Mail Đã Check.txt','a', encoding= "utf-8")
    open('resuts/Danh Sách Mail Cần Check Lại.txt','a', encoding= "utf-8")
    open('resuts/Danh Sách Mail Liên kết Code 6.txt','a', encoding= "utf-8")
    open('resuts/Danh Sách Mail Liên kết Code 8.txt','a', encoding= "utf-8")
    os.system('cls')
    
    def logo():
        log="""
    
    \033[1;37m███╗░░██╗░\033[1;33m████████╗\033[1;36m██████╗░
    \033[1;37m████╗░██║\033[1;33m╚══██╔══╝\033[1;36m██╔══██╗
    \033[1;37m██╔██╗██║\033[1;33m░░░██║░░░\033[1;36m██████╔╝
    \033[1;37m██║╚████║\033[1;33m░░░██║░░░\033[1;36m██╔═══╝░
    \033[1;37m██║░╚███║\033[1;33m░░░██║░░░\033[1;36m██║░░░░░
    \033[1;37m╚═╝░░╚══╝\033[1;33m░░░╚═╝░░░\033[1;36m╚═╝░░░░░\033[1;31m [Tools Copyright Nguyễn Tiến Phước]
    """
        print(log)
    logo()
    computer_name = platform.node()
    mac_address = uuid.getnode()
    computer_name = socket.gethostname()
    user_name = getpass.getuser()
    key = hashlib.sha256((computer_name + str(mac_address) + user_name).encode()).hexdigest()
    # print(key)
    # lấy thông tin proxy 
    print('\033[1;91m>> [Thông Báo]\033[1;96m Đang xử lý 1 số thông số trước khi chạy tools')
    # lấy user:pass trên hệ thống xuống
    get_proxy_server =  requests.get(f'http://xn--cungcptoolmmo-7g2g.vn/proxy.php?key_user={key}').text
    get_userpass_server = get_proxy_server.split('@')[0]
    get_userpass_server = get_userpass_server.split(':')
    # Đổi 1 proxy mới và sau đó thêm proxy về server userpass
    #? BEGIN:   XỬ LÝ 1 SỐ THÔNG SỐ KHI VÀO TOOLS 
    headers = {
        'authority': 'app.proxydt.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
    }
    params = {
        'license': 'e6c5f70e-908c-4cc2-b9b2-3449069d7a2b',
        'user': f'{get_userpass_server[0]}', 
        'pass': f'{get_userpass_server[1]}',
    }

    doiipgenip = requests.get('https://app.proxydt.com/api/public/proxy/get-new-proxy-auth', params=params, headers=headers, timeout=30, verify=False).text
    print(doiipgenip)
    doiipgenip = json.loads(doiipgenip)
    # LẤY IP:POST
    ippost = doiipgenip['data']['http_ipv4']
    ippost = ippost.split('//')[1]
    proxy_new = get_userpass_server[0]+':'+get_userpass_server[1]+'@'+ippost
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
    }

    params = {
        'key': f'{key}',
        'proxy': f'{proxy_new}',
    }

    response = requests.get('http://xn--cungcptoolmmo-7g2g.vn/updateproxy.php', params=params, headers=headers).text
    
    
    #? END:   XỬ LÝ 1 SỐ THÔNG SỐ KHI VÀO TOOLS 

    list_mail = open('mail.txt' ,encoding= "utf-8").read().split('\n')
    sau_bao_nhiêu_mail_thì_đổi_ip = 200
    threads = []
    get_proxy =  requests.get(f'http://xn--cungcptoolmmo-7g2g.vn/proxy.php?key_user={key}').text
    # print(get_proxy)
    for stt,list_mail_loc in enumerate(list_mail):
        thread = threading.Thread(target=Run, args=(list_mail_loc,stt,len(list_mail), get_proxy))
        threads.append(thread)
        thread.start()
            
        if (stt + 1) % sau_bao_nhiêu_mail_thì_đổi_ip == 0:
            for thread in threads:
                thread.join()
            threads = []
            print('\033[1;93m >> \033[1;97m> Xử Lý Thay Mới Thông Số Chrome < \n')
            get_proxy_server1 =  requests.get(f'http://xn--cungcptoolmmo-7g2g.vn/proxy.php?key_user={key}').text
            get_userpass_server1 = get_proxy_server1.split('@')[0]
            get_userpass_server1 = get_userpass_server1.split(':')

            cookies = {
                '_ga': 'GA1.1.108850409.1686789374',
                '__gads': 'ID=387a81b1e62bafc9-228a89e2a5b4009f:T=1686789374:RT=1686789374:S=ALNI_MYD7Pzq6Ct2_DODTLzhfQszYRVO2g',
                '__gpi': 'UID=00000c4f1f5bba23:T=1686789374:RT=1686789374:S=ALNI_MZyb2pvdJ0KrHjNJCehVqWu0BuaHg',
                '_ga_W46Z5GSYNB': 'GS1.1.1686789373.1.1.1686790922.0.0.0',
            }

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                # 'Cookie': '_ga=GA1.1.108850409.1686789374; __gads=ID=387a81b1e62bafc9-228a89e2a5b4009f:T=1686789374:RT=1686789374:S=ALNI_MYD7Pzq6Ct2_DODTLzhfQszYRVO2g; __gpi=UID=00000c4f1f5bba23:T=1686789374:RT=1686789374:S=ALNI_MZyb2pvdJ0KrHjNJCehVqWu0BuaHg; _ga_W46Z5GSYNB=GS1.1.1686789373.1.1.1686790922.0.0.0',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            params = {
                'key_user': 'afa781c44212312a0a0fedcf646cb6ead50513f9714d8f8cdf55aeb70cc1c5ab',
                'license': 'e6c5f70e-908c-4cc2-b9b2-3449069d7a2b',
                'user': 'uxzdw00z',
                'pass': 'p0839107',
            }

            response = requests.get('http://xn--cungcptoolmmo-7g2g.vn/doiip.php', params=params, cookies=cookies, headers=headers, timeout=30, verify=False).text
            doiipgenip1 = json.loads(response)
            print(doiipgenip)
            ippost1 = doiipgenip1['data']['http_ipv4']
            ippost1 = ippost1.split('//')[1]
            proxy_new1 = get_userpass_server1[0]+':'+get_userpass_server1[1]+'@'+ippost1

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
            }

            params = {
                'key': f'{key}',
                'proxy': f'{proxy_new1}',
            }

            response = requests.get('http://xn--cungcptoolmmo-7g2g.vn/updateproxy.php', params=params, headers=headers, timeout=10).text

            get_proxy = proxy_new1
            # print(proxy_new)
            # Đổi 1 proxy mới và sau đó thêm proxy về server userpass
            #? BEGIN:   XỬ LÝ 1 SỐ THÔNG SỐ KHI VÀO TOOLS 
            
            
            # headers = {
            #     'authority': 'app.proxydt.com',
            #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            #     'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            #     'cache-control': 'no-cache',
            #     'pragma': 'no-cache',
            #     'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            #     'sec-ch-ua-mobile': '?0',
            #     'sec-ch-ua-platform': '"Windows"',
            #     'sec-fetch-dest': 'document',
            #     'sec-fetch-mode': 'navigate',
            #     'sec-fetch-site': 'none',
            #     'sec-fetch-user': '?1',
            #     'upgrade-insecure-requests': '1',
            #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            #     'Cache-Control': 'no-cache',
            #     'Pragma': 'no-cache',
            # }
            # params = {
            #     'license': 'e6c5f70e-908c-4cc2-b9b2-3449069d7a2b',
            #     'user': f'{get_userpass_server1[0]}', 
            #     'pass': f'{get_userpass_server1[1]}',
            # }

            # doiipgenip1 = requests.get('https://app.proxydt.com/api/public/proxy/get-new-proxy-auth', params=params, headers=headers, timeout=10)
            # if doiipgenip1.status_code !=200:
            #     pass
            #     print('Lỗi')
            #     headers = {
            #         'authority': 'app.proxydt.com',
            #         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            #         'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            #         'cache-control': 'no-cache',
            #         'pragma': 'no-cache',
            #         'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            #         'sec-ch-ua-mobile': '?0',
            #         'sec-ch-ua-platform': '"Windows"',
            #         'sec-fetch-dest': 'document',
            #         'sec-fetch-mode': 'navigate',
            #         'sec-fetch-site': 'none',
            #         'sec-fetch-user': '?1',
            #         'upgrade-insecure-requests': '1',
            #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            #         'Cache-Control': 'no-cache',
            #         'Pragma': 'no-cache',
            #     }
            #     params = {
            #         'license': 'e6c5f70e-908c-4cc2-b9b2-3449069d7a2b',
            #         'user': f'{get_userpass_server1[0]}', 
            #         'pass': f'{get_userpass_server1[1]}',
            #     }

            #     doiipgenip1 = requests.get('https://app.proxydt.com/api/public/proxy/get-new-proxy-auth', params=params, headers=headers, timeout=10)
            # else:
            #     doiipgenip1 = doiipgenip1.text
            
            
            # doiipgenip1 = json.loads(doiipgenip1)
            # if doiipgenip1['data']['location'] == None:
            #     headers = {
            #         'authority': 'app.proxydt.com',
            #         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            #         'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            #         'cache-control': 'no-cache',
            #         'pragma': 'no-cache',
            #         'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            #         'sec-ch-ua-mobile': '?0',
            #         'sec-ch-ua-platform': '"Windows"',
            #         'sec-fetch-dest': 'document',
            #         'sec-fetch-mode': 'navigate',
            #         'sec-fetch-site': 'none',
            #         'sec-fetch-user': '?1',
            #         'upgrade-insecure-requests': '1',
            #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            #         'Cache-Control': 'no-cache',
            #         'Pragma': 'no-cache',
            #     }
            #     params = {
            #         'license': 'e6c5f70e-908c-4cc2-b9b2-3449069d7a2b',
            #         'user': f'{get_userpass_server1[0]}', 
            #         'pass': f'{get_userpass_server1[1]}',
            #     }

            #     doiipgenip1 = requests.get('https://app.proxydt.com/api/public/proxy/get-new-proxy-auth', params=params, headers=headers, timeout=10)
            #     doiipgenip1 = json.loads(doiipgenip1.text)
            #     if doiipgenip1['data']['location'] == None:
            #         headers = {
            #             'authority': 'app.proxydt.com',
            #             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            #             'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            #             'cache-control': 'no-cache',
            #             'pragma': 'no-cache',
            #             'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            #             'sec-ch-ua-mobile': '?0',
            #             'sec-ch-ua-platform': '"Windows"',
            #             'sec-fetch-dest': 'document',
            #             'sec-fetch-mode': 'navigate',
            #             'sec-fetch-site': 'none',
            #             'sec-fetch-user': '?1',
            #             'upgrade-insecure-requests': '1',
            #             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            #             'Cache-Control': 'no-cache',
            #             'Pragma': 'no-cache',
            #         }
            #         params = {
            #             'license': 'e6c5f70e-908c-4cc2-b9b2-3449069d7a2b',
            #             'user': f'{get_userpass_server1[0]}', 
            #             'pass': f'{get_userpass_server1[1]}',
            #         }

            #         doiipgenip1 = requests.get('https://app.proxydt.com/api/public/proxy/get-new-proxy-auth', params=params, headers=headers, timeout=10)
            #         doiipgenip1 = json.loads(doiipgenip1.text)
            # else:
            #     pass
            # # LẤY IP:POST
            # print(doiipgenip1)
            # ippost1 = doiipgenip1['data']['http_ipv4']
            # ippost1 = ippost1.split('//')[1]
            # proxy_new1 = get_userpass_server1[0]+':'+get_userpass_server1[1]+'@'+ippost1
            # # print(proxy_new)
            
            # headers = {
            #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            #     'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            #     'Cache-Control': 'no-cache',
            #     'Connection': 'keep-alive',
            #     'Pragma': 'no-cache',
            #     'Upgrade-Insecure-Requests': '1',
            #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            #     'Cache-Control': 'no-cache',
            #     'Pragma': 'no-cache',
            # }

            # params = {
            #     'key': f'{key}',
            #     'proxy': f'{proxy_new1}',
            # }

            # response = requests.get('http://xn--cungcptoolmmo-7g2g.vn/updateproxy.php', params=params, headers=headers, timeout=10).text

            # get_proxy = proxy_new1
            
    for thread in threads:
        
        thread.join()
        
if __name__ == '__main__':
    main()
    
    
