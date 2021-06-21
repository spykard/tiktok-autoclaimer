from json import dumps
from colorama import init, Fore, Style
init(convert=True) # For Windows
import requests

headers = {
    'authority': 'www.tiktok.com',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.tiktok.com/signup/create-username?lang=en',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'tt_webid_v2=6960869513848309253; tt_webid=6960869513848309253; tt_csrf_token=jA-J-kAi-UlBBRj3kaG3ztM8; '
              'MONITOR_WEB_ID=6960869513848309253; '
              'R6kq3TV7=ADZkeFl5AQAAPbz98qbB2AoNyFMIBuBooD7ZgoYn8Uhd8AKWRCV-ls5u8GYq|1|0'
              '|0760a53a1e0c14271ab8282fcb04de1100ba0616; csrf_session_id=f02e269c246d40fa868f6fcaf8dfe229; '
              's_v_web_id=verify_kojh5on8_PD5dBNSL_veZ6_4GHM_8lRD_VaDcFKJiOZmV; '
              'ak_bmsc=D472ADBF5C85E7617CC51DA1D2E1535718E2213C483F0000F5F9996027C86E26~pljnPwRudIoNGDS53v+SVlBw7'
              '/LgD4q6q8K8ldRbIzhpbCX2d+oEm2qPuu1oW/7ukAJ56seKZ7HFqJAIeBS'
              '+kmwMd8Q0cVbJFXx3vZSSq6ImtOOLfDv2Ym3B99APbaNBZSNaMRLr1A2VnOC+zBmsbkjeF8dn1gNT+CYhle'
              '/23YyK8yCmsKSDluSpukv1Qaip4Wfs3YZOYVUi3VOoH4aOauuDzLHSxB7cf104DzVOP06Wo=; '
              'bm_sz=CDF5E425194D59886F2F8C6B86BF1287~YAAQPCHiGFTVzDF5AQAA3GZ4WQuCtmg7p7sskEoq7wylH/jddeqtq1I6bXWSy'
              '+hqmXotV4ZLpJs6QOMYjoR4VfjQuxhg275pTVmTc21zJU06pz0khs9ivQxPYTnnPc'
              '+E0lWECPu36YshAFWZ9KRROYZG6Ouha5zYjUntFTJqYhFhg52OkquYno9vJAv53sum; '
              '_abck=A43D65FA1AF21932B052077EC12F2DF8~-1~YAAQPCHiGFXVzDF5AQAA3GZ4WQUyqKPRUYwaQByhlD8k84'
              '+zwAY8QYwXcct022Zr/pO2Xdp6ZzntpM5YBtEF6hCicFwF/KvR3/HvAitajkUc4/ePnFkk1e3kKNsPKam5QuFCieO/pK9T+XhFRp'
              '/lQWo1DqUF2l9PdLXV/GmTAMAEEyaEkm7WVKDv8u'
              '/7PBDLZJqyP9U0TRstv5mmOCRwMPGmWssNNoX75ykwcbvrWpZJF7aGpwPoQWhMvgUjfDaEIQU4N8fHnObkoo6ik++9kVHBH9g'
              '+qOPt1uzKqzpyRHJlAw2+M4xtc4cvVxwoyOfvX1BX2co0owShz0p6mYNm1GuLxHXcGRc4C8Frzcw487Vkjg2jv7NeyrtYr4c=~-1'
              '~-1~-1; passport_csrf_token=bbab7ea4bf2809dd94ddf26e0a5b5054; '
              'passport_csrf_token_default=bbab7ea4bf2809dd94ddf26e0a5b5054; '
              'passport_auth_status=284325a5aad5ef47f81facd8c83179ec%2C; '
              'passport_auth_status_ss=284325a5aad5ef47f81facd8c83179ec%2C; store-idc=maliva; store-country-code=ca; '
              'bm_sv=656946701D72C82317CB201D2EBC8FFB~6w1j9MvsTwvW/smGX4eme0NCqGBdxTo3o2zM/RWgdXpm0Gpdm7YZ7ulGrRaRFJe'
              '+7VuStyymenLZUpYgJBiUIAjx3WfPzZWxW67e5k6C9KaKFG6bT9hMI/JWhWA0PE6/8LO/+5weHCxVCb6MEGKncTWbMyPs'
              '/+vIZA2YjKTAYbw=; ttwid=1%7CjTA7nQRnaq81uP_IGppuXsgb4hhLG6aCgIT468RaOqc%7C1620704211'
              '%7C5a0eca061f11045c43e4499440cd2500c482484fb82afd7f7a0bf276f65c1700; '
              'cmpl_token=AgQQAPNoF-RO0rCnM6n2Yl08-vhgwuNZf4fjYP-ybw; '
              'sid_guard=05d851c33cb206eb06b5776744da7c1b%7C1620704363%7C5184000%7CSat%2C+10-Jul-2021+03%3A39%3A23'
              '+GMT; uid_tt=9fbc46c05d1f842ec00d6ea93e67ecbf4f020242d9672854f426df3f7e3b60c2; '
              'uid_tt_ss=9fbc46c05d1f842ec00d6ea93e67ecbf4f020242d9672854f426df3f7e3b60c2; '
              'sid_tt=05d851c33cb206eb06b5776744da7c1b; sessionid=05d851c33cb206eb06b5776744da7c1b; '
              'sessionid_ss=05d851c33cb206eb06b5776744da7c1b; '
              'odin_tt=f2feefe13f299f208e6d1ac5782a0696efc852ea123b4b4b21a8cc2a1a0a18d278b530610c8b454e6b0a2db513fff51371b5faa74d0d03d0e1b479768cfcbf700c0a3b77a94a1688e35a3c5337d6bcaf '
}

params = (
    ('aid', '1233'),
    ('unique_id', 'ppp'),
    ('app_language', 'en'),
    ('fromWeb', '1'),
    ('cookie_enabled', 'true'),
    ('screen_width', '472'),
    ('screen_height', '700'),
    ('browser_language', 'en-US'),
    ('browser_platform', 'Win32'),
    ('browser_name', 'Mozilla'),
    ('browser_version', '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'),
    ('browser_online', 'true'),
    ('timezone_name', 'America/Toronto'),
    ('device_platform', 'web_pc'),
    ('region', 'CA'),
)

response = requests.get('https://www.tiktok.com/api/uniqueid/check/', headers=headers, params=params)

print(response.json())
input('''                             [\x1b[33m✓\x1b[39m] The username \x1b[33m\x1bs@ninter\x1b[39m is available on \x1b[33m\x1bsTikTok!\x1b[39m
    ''')

quit()

if response.json()['status_code'] == 0:
    input('''                             [\x1b[33m✓\x1b[39m] The username \x1b[33m\x1bs@ninter\x1b[39m is available on \x1b[33m\x1bsTikTok!\x1b[39m
    ''')
elif response.json()['status_code'] == 3249:
    input('''                             [\x1b[33m✓\x1b[39m] The username \x1b[33m\x1bs@ninter\x1b[39m is not available on \x1b[33m\x1bsTikTok!\x1b[39m
    ''')