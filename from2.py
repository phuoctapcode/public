import requests

cookies = {
    'fr': '05tvWfcQNYDHuMUP1..BkiWQQ.jV.AAA.0.0.BkiWQQ.AWVYAV1Bb9U',
    'sb': 'EGSJZA3dofisAv1rK_7hRYAG',
    'datr': 'EGSJZDHIk7MdFeMcyO_vcpbp',
    'wd': '1101x923',
}

headers = {
    'authority': 'd.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'fr=05tvWfcQNYDHuMUP1..BkiWQQ.jV.AAA.0.0.BkiWQQ.AWVYAV1Bb9U; sb=EGSJZA3dofisAv1rK_7hRYAG; datr=EGSJZDHIk7MdFeMcyO_vcpbp; wd=1101x923',
    'origin': 'https://d.facebook.com',
    'pragma': 'no-cache',
    'referer': 'https://d.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F&multiple_results=0&from_login_screen=0&_rdr',
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
    'viewport-width': '1101',
}

params = {
    'ctx': 'recover',
    'c': '/login/',
    'search_attempts': '1',
    'alternate_search': '0',
    'show_friend_search_filtered_list': '0',
    'birth_month_search': '0',
    'city_search': '0',
}

data = {
    'lsd': 'AVrx1aQs-BI',
    'jazoest': '2911',
    'email': 'lol@usa.com',
    'did_submit': 'Tìm kiếm',
}

response = requests.post('https://d.facebook.com/login/identify/', params=params, cookies=cookies, headers=headers, data=data).text
print(response)