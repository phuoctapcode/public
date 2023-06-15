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
    ssNTP = requests.session()
    proxy = {
                
                'http': f'http://{proxy1}',
                'https': f'http://{proxy1}'
                # 27.76.243.186:62503:phuoc_gJK7b:40GR7XwZ
            }


    with open('resuts/Danh Sách Số Lượng Mail Đã Check.txt','a', encoding= "utf-8") as somail:
            somail.write('\n'+f'')
    headers = {
        'authority': 'd.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'cache-control': 'max-age=0',
        # 'cookie': 'fr=05tvWfcQNYDHuMUP1..BkiWQQ.jV.AAA.0.0.BkiWQQ.AWVYAV1Bb9U; sb=EGSJZA3dofisAv1rK_7hRYAG; wd=1920x923; datr=EGSJZDHIk7MdFeMcyO_vcpbp',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.148", "Google Chrome";v="112.0.5615.148", "Not:A-Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"14.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'viewport-width': '1365',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
    }

    gendata = ssNTP.get('https://d.facebook.com/',  headers=headers, proxies=proxy, timeout=10)
    if gendata.status_code != 200:
        print(f'\033 \033[1;93m>> \033[1;91m[{mail}]  \033[1;96m=>  \033[1;97mStatus=Cần Check lại]')
        with open('resuts/Danh Sách Mail Cần Check Lại.txt','a', encoding= "utf-8") as mail_an:
            mail_an.write('\n'+f'{mail_cc}')
    lsd = gendata.text.split('name="lsd" value="')[1].split('"')[0]
    jazoest = gendata.text.split('name="jazoest" value="')[1].split('"')[0]




    headers = {
        'authority': 'd.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': gendata.headers['set-cookie'],
        'origin': 'https://d.facebook.com',
        'pragma': 'no-cache',
        'referer': 'https://d.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fd.facebook.com%2F&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&_rdr',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.148", "Google Chrome";v="112.0.5615.148", "Not:A-Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"14.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'viewport-width': '1365',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
    }

    params = {
        'ctx': 'recover',
        'c': '/login/',
        'search_attempts': '1',
        'ars': 'facebook_login',
        'alternate_search': '0',
        'show_friend_search_filtered_list': '0',
        'birth_month_search': '0',
        'city_search': '0',
    }

    data = {
        'lsd': f'{lsd}',
        'jazoest': f'{jazoest}',
        'email': f'{mail}',
        'did_submit': 'Tìm kiếm',
    }

    response = ssNTP.post('https://d.facebook.com/login/identify/', params=params,  headers=headers, data=data, proxies=proxy, timeout=10)
    if response.status_code != 200:
                    print(f'\033 \033[1;93m>> \033[1;91m[{mail}]  \033[1;96m=>  \033[1;97mStatus=Cần Check lại]')
                    with open('resuts/Danh Sách Mail Cần Check Lại.txt','a', encoding= "utf-8") as mail_an:
                        mail_an.write('\n'+f'{mail_cc}')
    response = response.text              
    a = re.search('Tìm kiếm không trả về kết quả nào. Vui lòng thử lại với thông tin khác.', response)
    b = re.search('Điền vào ít nhất một mục bên dưới để tìm kiếm tài khoản của bạn', response)
    c = re.search('Có vẻ như bạn đang dùng nhầm tính năng này do sử dụng quá nhanh. Bạn tạm thời đã bị chặn sử dụng nó.', response)
    if a != None:
            print(f'\033 \033[1;93m>> [{stt}] \033[1;91m[{mail}]  \033[1;96m=>  \033[1;91mStatus=[Không Liên Kết] {proxy1}')
            with open('err.txt','a', encoding= "utf-8") as mail_an:
                mail_an.write('\n'+f'{mail_cc}')
    elif b!= None:
        print(f'\033 \033[1;93m>> [{stt}] \033[1;91m[{mail}]  \033[1;96m=>  \033[1;91mStatus=[Sai Định Dạng] {proxy1}')
    elif c!=None:
        print(f'\033 \033[1;93m>> [{stt}] \033[1;91m[{mail}]  \033[1;96m=>  \033[1;91mStatus=[Bạn tạm thời bị chặn] {proxy1}')
        
    else:
        #=================================  CHECK MAIL ẨN  ===================================#
        genldata = urllib.parse.unquote(response)
        # print(genldata)
        if 'name="cuid" value="' in genldata:
                ldata = genldata.split('name="cuid" value="')[1].split('"')[0]
                
                print(f'\033 \033[1;93m>> \033[1;91m[{mail}]  \033[1;96m=>  \033[1;97mStatus=Cần Check lại ở thiết ldata mới là {ldata}]')
        elif 'ldata' in genldata:
                ldata = genldata.split('ldata=')[1].split('"')[0]

                print(f'\033 \033[1;93m>> \033[1;91m[{mail}]  \033[1;96m=>  \033[1;95mStatus= {ldata}]')
        else:
                print(f'\033 \033[1;93m>> \033[1;91m[{mail}]  \033[1;96m=>  \033[1;94mStatus= {genldata}')

            
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
            
    for thread in threads:
        
        thread.join()
        
if __name__ == '__main__':
    main()
    
    
