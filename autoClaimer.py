from json import dumps
from colorama import init, Fore, Style
init(convert=True) # For Windows
import requests

headers = {
    'authority': 'www.tiktok.com',
    'method': 'GET',
    # 'path':
    'scheme': 'https',
    'accept': '*/*',
    # 'accept-encoding':
    'accept-language': 'en-US,en;q=0.9', 
    # 'cache-control':    
    'content-type': 'application/x-www-form-urlencoded',    
    'referer': 'https://www.tiktok.com/signup/create-username?lang=en',      
    # 'sec-ch-ua':
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',    
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    # 'x-kl-ajax-request':
    # 'x-mssdk-info':
    # 'x-secsdk-csrf-token':  
    # 'cookie': 'tt_webid_v2=6960869513848309253; tt_webid=6960869513848309253; tt_csrf_token=jA-J-kAi-UlBBRj3kaG3ztM8; '
    #           'MONITOR_WEB_ID=6960869513848309253; '
    #           'R6kq3TV7=ADZkeFl5AQAAPbz98qbB2AoNyFMIBuBooD7ZgoYn8Uhd8AKWRCV-ls5u8GYq|1|0'
    #           '|0760a53a1e0c14271ab8282fcb04de1100ba0616; csrf_session_id=f02e269c246d40fa868f6fcaf8dfe229; '
    #           's_v_web_id=verify_kojh5on8_PD5dBNSL_veZ6_4GHM_8lRD_VaDcFKJiOZmV; '
    #           'ak_bmsc=D472ADBF5C85E7617CC51DA1D2E1535718E2213C483F0000F5F9996027C86E26~pljnPwRudIoNGDS53v+SVlBw7'
    #           '/LgD4q6q8K8ldRbIzhpbCX2d+oEm2qPuu1oW/7ukAJ56seKZ7HFqJAIeBS'
    #           '+kmwMd8Q0cVbJFXx3vZSSq6ImtOOLfDv2Ym3B99APbaNBZSNaMRLr1A2VnOC+zBmsbkjeF8dn1gNT+CYhle'
    #           '/23YyK8yCmsKSDluSpukv1Qaip4Wfs3YZOYVUi3VOoH4aOauuDzLHSxB7cf104DzVOP06Wo=; '
    #           'bm_sz=CDF5E425194D59886F2F8C6B86BF1287~YAAQPCHiGFTVzDF5AQAA3GZ4WQuCtmg7p7sskEoq7wylH/jddeqtq1I6bXWSy'
    #           '+hqmXotV4ZLpJs6QOMYjoR4VfjQuxhg275pTVmTc21zJU06pz0khs9ivQxPYTnnPc'
    #           '+E0lWECPu36YshAFWZ9KRROYZG6Ouha5zYjUntFTJqYhFhg52OkquYno9vJAv53sum; '
    #           '_abck=A43D65FA1AF21932B052077EC12F2DF8~-1~YAAQPCHiGFXVzDF5AQAA3GZ4WQUyqKPRUYwaQByhlD8k84'
    #           '+zwAY8QYwXcct022Zr/pO2Xdp6ZzntpM5YBtEF6hCicFwF/KvR3/HvAitajkUc4/ePnFkk1e3kKNsPKam5QuFCieO/pK9T+XhFRp'
    #           '/lQWo1DqUF2l9PdLXV/GmTAMAEEyaEkm7WVKDv8u'
    #           '/7PBDLZJqyP9U0TRstv5mmOCRwMPGmWssNNoX75ykwcbvrWpZJF7aGpwPoQWhMvgUjfDaEIQU4N8fHnObkoo6ik++9kVHBH9g'
    #           '+qOPt1uzKqzpyRHJlAw2+M4xtc4cvVxwoyOfvX1BX2co0owShz0p6mYNm1GuLxHXcGRc4C8Frzcw487Vkjg2jv7NeyrtYr4c=~-1'
    #           '~-1~-1; passport_csrf_token=bbab7ea4bf2809dd94ddf26e0a5b5054; '
    #           'passport_csrf_token_default=bbab7ea4bf2809dd94ddf26e0a5b5054; '
    #           'passport_auth_status=284325a5aad5ef47f81facd8c83179ec%2C; '
    #           'passport_auth_status_ss=284325a5aad5ef47f81facd8c83179ec%2C; store-idc=maliva; store-country-code=ca; '
    #           'bm_sv=656946701D72C82317CB201D2EBC8FFB~6w1j9MvsTwvW/smGX4eme0NCqGBdxTo3o2zM/RWgdXpm0Gpdm7YZ7ulGrRaRFJe'
    #           '+7VuStyymenLZUpYgJBiUIAjx3WfPzZWxW67e5k6C9KaKFG6bT9hMI/JWhWA0PE6/8LO/+5weHCxVCb6MEGKncTWbMyPs'
    #           '/+vIZA2YjKTAYbw=; ttwid=1%7CjTA7nQRnaq81uP_IGppuXsgb4hhLG6aCgIT468RaOqc%7C1620704211'
    #           '%7C5a0eca061f11045c43e4499440cd2500c482484fb82afd7f7a0bf276f65c1700; '
    #           'cmpl_token=AgQQAPNoF-RO0rCnM6n2Yl08-vhgwuNZf4fjYP-ybw; '
    #           'sid_guard=05d851c33cb206eb06b5776744da7c1b%7C1620704363%7C5184000%7CSat%2C+10-Jul-2021+03%3A39%3A23'
    #           '+GMT; uid_tt=9fbc46c05d1f842ec00d6ea93e67ecbf4f020242d9672854f426df3f7e3b60c2; '
    #           'uid_tt_ss=9fbc46c05d1f842ec00d6ea93e67ecbf4f020242d9672854f426df3f7e3b60c2; '
    #           'sid_tt=05d851c33cb206eb06b5776744da7c1b; sessionid=05d851c33cb206eb06b5776744da7c1b; '
    #           'sessionid_ss=05d851c33cb206eb06b5776744da7c1b; '
    #           'odin_tt=f2feefe13f299f208e6d1ac5782a0696efc852ea123b4b4b21a8cc2a1a0a18d278b530610c8b454e6b0a2db513fff51371b5faa74d0d03d0e1b479768cfcbf700c0a3b77a94a1688e35a3c5337d6bcaf '
    'cookie': 'passport_csrf_token_default=093ed211e214777fd670239baa280ecb; passport_csrf_token=093ed211e214777fd670239baa280ecb; tt_webid_v2=6971999491461809670; tt_webid=6971999491461809670; store-idc=maliva; store-country-code=gr; user_oec_info=0a53d5e654d67b19d8a98d879424bd25484521a97949fb5c9bd31d370b087081f39733e81ebe67f5a59bd4dea94774ea462c62e04575083e920ded2d3074520a85a73d5ca2a6889f285608641c543942afd071d90d1a490a3cc75dc9c6e7e9d56383eeffc70d3fe31a3fbcc5f0b47bc96cb5446186e9014d38d182745dde985d590a747ec4dd65fb72f75be0db7450efc82f65a99e1095a5f30c1886d2f6f20d2201047449565b; passport_auth_status=663b8e0b3bfbed8a98d01fff58405ef6%2C9dbd57fff74843dbd2d7beebbc55acf4; passport_auth_status_ss=663b8e0b3bfbed8a98d01fff58405ef6%2C9dbd57fff74843dbd2d7beebbc55acf4; sid_guard=0c740c639d30da8cbb64dc5cd896ef99%7C1623400939%7C5184000%7CTue%2C+10-Aug-2021+08%3A42%3A19+GMT; uid_tt=e69c74a107772d1be9d09418d6d2eeaa832ba036e3c2beca51346dafe829d6e2; uid_tt_ss=e69c74a107772d1be9d09418d6d2eeaa832ba036e3c2beca51346dafe829d6e2; sid_tt=0c740c639d30da8cbb64dc5cd896ef99; sessionid=0c740c639d30da8cbb64dc5cd896ef99; sessionid_ss=0c740c639d30da8cbb64dc5cd896ef99; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22version%22:%22v2%22}; s_v_web_id=verify_kq6momrt_C5HrhVSk_3FkL_4Xkz_9ADX_t4lofsJ89brD; tt_csrf_token=qUhaNvntPIzKrLtz0NvRslyM; R6kq3TV7=AFClqy56AQAAvzrGW26wIoq6LkyD-Vgf0qCskPKNAN9-xhzyPzP5RF_2ms1D|1|0|b7ccf4b09995b0e0234ad5e8cc2a5160d81493ed; csrf_session_id=9c41006cad9b4f519c7cdf47dba0c6eb; bm_sz=C97DEEAEE97DC3351A676D387E27B423~YAAQjtzNF/8DXSB6AQAAJqmrLgyqjpLV4evGoSlU5psTKaYChXmNVthAU9Zz3Umbg9LZzDBPsUxs5nArwu1qaUGaUFrqeRn2SPgaELkjYoTzSeKvTsBuB10jN6JGL0uXWLkGEG7t5x2xXgjdbphdTFfwbXw3YnnzRsKcAqCfV3P4mK0GImV26JX+eTwQ/iIa; _abck=510AEEF3282E5F8502C75DDE07A109C3~-1~YAAQjtzNFwAEXSB6AQAAJqmrLgbknHduwxUQfzFphu+WlIctNpdus/mE8HY9QkX+/E1nbR5nXWjz0qSo+DD5Ep4Y0APmwcTfNxat4LUFDXOqcWuwGid+Q7T2ZRqGPvrxY+dt+0fpTzuCWg3LPpwjBsoVZVf5mnVtaJOv043lQERqNymbPrsIA5cClkAfRlUJpcNKk6OtBuoUK8046pzfzD7zKQK0RrVLXc3xHtd7yJwq8ygHvrktCBssXUGsRlqbGmaGykXK1AA+NwpUnlhhSv+EN4PFxXmvRB+ZLUtAx9H0lHEkjGd1Tpo9EUWm7i/DpJHByZjlUHMojy+d28UVIMNESXv+zVMef318aZy8fZm6LaybxR8nObsdYRN+qWpvjtmsNZuOOhWEBw==~-1~-1~-1; ak_bmsc=1BAA3CB9DB778384F74B8224EF53D06B~000000000000000000000000000000~YAAQjtzNFwEEXSB6AQAAJqmrLgyDRBQeYt47HlP5lESZm/fl2Rhrk+ZuOy+TLBdOkzecU7XGaSE1IuGSnNou8hilaXlO6alL4LF2PeEg24cA0OpbmfcvZZWpZXXDiMQUjVVkTNd48eui4ul22/JC4VV2ifVESlqH6i6cqiE4lDIKZPqr4eDbt1AMjpdW5r87+nEDvC9aw6eD6wOo97KWzNrUwUzPmX8Hj+mEVKTCxQwC8oQ0jmxdAFocB4EDC/A/rBBKAKLO4uuvXepDSpjLveh0w2Z2sDX0FLEr4NUL3xaNqvV3sh9h4OIrAtUc+3Vj8FFUfDm9EzOkM8m2V6RbuZfZaYXJqVuHjoM40O3ZPgk5+sRL7JaB8nHRocwq63CxW8PEsur6WUPx4w==; csrf_session_id=9c41006cad9b4f519c7cdf47dba0c6eb; cmpl_token=AgQQAPOfF-RMpbD_ex__e108-qAdqolWP4QUYP6Law; bm_sv=9A7E65334A0CFB43042ECE63DDE1A539~ZDvcR8xEyNPVNpym797Wa/3+qIxVyUHNwSU1VJN7CcSVXuac/NqsgCJ9M3vFhYRKk5Lc+aG96ZP+KsUg/26egVRqQbNOp9QcSO96paSUd0DJGYpP8Jz/ut53q56c1WrWp3eAUm7Z9+H4wK14UUO1LNex1MxeOZ9uoTRXpNA/pLk=; passport_fe_beating_status=false; odin_tt=dce1c2c7916f83e8a9fe91b90fd171d3056799bbf0c29c9923b5507f2cd998069f86c6c113c7ba8f1a5523bb85813f73633a38d5ebfb92fc92231c310dff5c8643a6961638d0569060acd92475bdf713; ttwid=1%7C6hGVZU3Q391vcBYc4SoLdaaGuxQw3WulUsySdzEe6lU%7C1624283563%7C5d4209e59bf63dde4aacc427bee85d286965520e1319a9716f0a5a0c17aaa5bc'
}

params = (
    ('aid', '1233'),
    # 'app_name':
    ('app_language', 'en'),
    # 'device_id':
    ('device_platform', 'web_pc'),
    ('region', 'GR'),
    # 'os':
    # 'referer':
    # 'root_referer':
    ('cookie_enabled', 'true'),
    ('screen_width', '472'),
    ('screen_height', '700'),
    ('browser_language', 'en-US'),
    ('browser_platform', 'Win32'),
    ('browser_name', 'Mozilla'),
    ('browser_version', '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'),
    ('browser_online', 'true'),
    ('timezone_name', 'Europe/Athens'),
    # 'is_page_visible':
    # 'focus_state':
    # 'is_fullscreen':
    # 'history_len':
    # 'battery_info':     
    ('unique_id', 'fbi'),
    ('fromWeb', '1'),
    # '_signature':    
)

headers = {
    'authority': 'www.tiktok.com',
    'method': 'GET',
    'path': '/api/uniqueid/check/?aid=1233&app_name=tiktok_web&app_language=en&device_id=6971999491461809670&device_platform=web_pc&region=GR&os=windows&referer=&root_referer=&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=el-GR&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F91.0.4472.106%20Safari%2F537.36&browser_online=true&timezone_name=Europe%2FAthens&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=4&battery_info=1&unique_id=ppp&fromWeb=1&_signature=_02B4Z6wo00101H3UZmQAAIDCoZAbFyIF66R91GLAAH-te5',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'el-GR,el;q=0.9,en;q=0.8', 
    # 'cache-control':    
    'content-type': 'application/x-www-form-urlencoded',    
    'referer': 'https://www.tiktok.com/signup/create-username?lang=en',      
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',    
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'x-kl-ajax-request': 'Ajax_Request',
    'x-mssdk-info': 'Vi2upjEzLUs4muQo6h-mjHpDpN48-uJOrntDViWur5O1y-uCZ97KQEqxFHs2E58n77mN791legNL6cnvJtGcZrfj7Ury3PO5gZ-T.oNfzuYBcmb4oD-RoI2m08PhmBeSkg5RbJKiL89v5LiKXqzHXPDo0.BKEFCMNX8Uc11xVFiHLMqaLiWW6UNo.hqfwAaZLFW51EJ0xVQPb9zq8lQP9YlzUBHMm4oxtdKndjLgvAiY2W5D9NjwU.Qufrp6UR8I8ZD39q50qxp6DQAZoVYroPW9pAqfVusVfZb8AYoURdwORKx5kzHub9yaG3NoCmF4V8-Z4WqT.47C9M59wR2OLCEWX3-yoKaiEyQBu2wrpC-vsh3RUeoklyCm.KCRepQbYFQipBDbVvTKfKYR5xxhskgCsiPd.aAoSKoE.vQi1PM5BRDdw6rIEUYYeGGMcuJjsj43h62CRFwWTY.tcTqgbLtvMARgs6DzpjOcDOQanJUrE9FS8ZXtHqEi9z-Wjus6YsluHWwgU3CIWMPVoYv2BpS55uq56MAfJ7.rhgIZatbTmpgqbyI3ONf7nmd1rJK-9Fqdkud8-pQu4hp0Su5Low4oTH7BG74fZcTprOLfR3n.4HQw7XQcVhWgCHJn68kIHVDHTECNprdCITcR8L.d4GK-UXPvfB7ZloFaY29cEjfc4sS8aIGHpqBvbFOuy8fRIqUU7oj0NWeWLT1aIYVRSDo3eb1FcfNABY5ymJiiqWIR2Reaj74FP0xuM5JY0zzDlnrBKqDgOjGuuIRUn74DLElM.s5A7vIayIN5lbiStiA5Vzz9HSn1Yc7w3kGzMnKZCkRSLxqIaV0RBE3zr0U9BmjmLQKSCxSerVyt9uyjF8RuVOe.5PmSYxS8kEj8Up5d04JdHqB-bznEq3HcYCIlZyydlsdP4YRTkurwst7q-VxqlDFsiTWK9EyjVRX8QEq4EU6IjSN.PekyDwoBeh16ddDnSQenzY9OsSiQWwkUwMNLwNHFsNaZI6yMIWxbVVlQE4VINz-csTUr2BmnJ5TNWtvfLAz7cVSgNe5XeLreJXhBuOuH.2ga6fPjedP4qi-VrWjuAYQjQZZXj5dmvOEI.G4GTgyXGdyDx23mw9zKuPAV2jkiGM5dNtAeman9mvaI3B69IMIC0a5JG1g.WJb-9S20FB5uQPjKiET2MV8E5nm-kaKA7CEkX9te1ZSpTa19INoi29pXWU.Nm5VK6wxtfCwTJO6OCEbx5FzgN4zDtA4pStcERDlFyYNRA9c2SJL8HaQEb.KrRFwMJQ-56DsagAEv93X4CLpRu6212zL-0zviZZVPdaJd3bKdfX1WC5WfvzsZ4iiBCy1griRtwpjC0HY4tZ55cDgf2E6E4rzJ5FIs9rg9K4S3LlzzLeZXeyVeosMsSErW1uIlKJIAXBawE6DnJ11SbytjRmqiBOgDT5SWx5JBWcA5vDHAuxxZ8my1dbMLiZVWDAFv0mvieWilBYLID9BbElcBFdAkmUt6zIKyhBLJFbIu4mzwpXUohmXiSeOgRRZnNBS7R3h9axfo5qsWEEFV7ACyHD529emPknlh.G6hsdNgT-lVxI1ADRQn5dNY8m62ZJqVCEWloj.0TnK5FBnC-uOlRi8m31kH6jwjrxAhr8JBhvE2Qdx4a5DS71gF2iqO96KmXReH65dm8FBOlx3Tg1yZ8Bo9kja7d3EZpquiI0L26ZQwXy78N9RO56CWXGLPk9HUq7Or0ydXwYnYWKqQqjPL4UE7ULVwAsK74OUOUL1ve0YIqM2OoWBBPvD6eLEvX80E9YFUzMa4DG65AlJyEG54NOSWDwp2FJvMeb8Wc79C6Z2bmYgcUXQbj.bS-3p5RC697VhVe6u.4CvNS7uvqYoBBEwW.DYnejYYl9ePaZdX3wW89PkKosN7S3SViUMwhN2PV7KK895N3MtqTKhU7I5c0QoQ-yBrrqohKAMI3ulkPNkU5xHJqXKiqQWDP0ov5LVk4siuKEGpbf0MlknKYbdrqE8lqgLYTZr5I3Vhs89DF4cJwyBId3USMLWSl8OWPCPsctA8kk7iKtImWdmkUFruu8TXAqcpcD8c0kelaurAtju47pqUQ6es.XxKKlrZwJwrIxDlf2HE8mUlAT.ibSOK5CV4zkJRWvZxz.nJf-ga-5atNF8u3FxN4XSl3CkVwcT.5rIZEOCZ1uD8liwP11TXFNIX13NHqSkc5O0.Yii2vPWlKgFHHJPt7natp7WCnkxlMGZRo-VZBVyJ01dcOBWfEijm36Cha0scy.ktxzVBWKMMeYi6CJgzwJWBB6AoK1SHezqeBMitFBAGtxmLQ2Hm5v8fgiIuIBGGAcbBaQt64uZpmx13.lcKsUQUab4EPXfr3JbAh9QbFStOgEzXJXInoonzEtTqL.PjWbbLBvx4INjETMzgHzExihG18S6s8nqWsN8cyyHzR7L1MK7B2Oi3xXmtlErCyZcwOrcE3slI6b4WKkds8uOtD174TUnGo1p9Lj10zfjRJMG5oE3iAUrcuVWvffr6AkVLRPRYkCriB4n2PdHt5YKzRk2NdLwchpGPt4Clr.Fd4BoC9rMb-gEsNpSEtwQo0USidiqi1HuwXfuYazqp4.NazwTzMT4C3TwkPTV9rz.58aC.ghqGNY8v5.sA7paHk9-z.eG8bmogGTwhhqZ5q2y6CI.kkJWC2M.XHE078AxR5yPZ1zYaIMOJrZ799W4CXLH2YYHJeTWH4XM4s.pnhayRCNSJw7ibitNQDeOWLq61NiX8.NaZQWbPARv8-ZBrDip3o9Mbc4q-hQmqD0b1oCx2WCha7V5ujmre8xSLJVFEGMh78Lxsp6efOvLkCIeZ.8R6.r6eLCAtEo0vqsyr3x.TFON6twnLDkHkV-qh6rwm-eBygYrDJYws4H0SeQFyIVE1WTUGNUPjZfKUVkxMiR71y5V6C58J.gzZdelM.U1fjZaK78W1hMilkB9y1r2o7FxP.ohrCJmSJgUnN5UIpbqXPI2ljO2.McAr1MN8sLc9l4wq414H4hEe-vub5LV7IWWabWe3XGoCOhI24P-ygycUBRuqnWyJyExEQ0cyv.m4VXLvjlYgilI5Srem4wJDsnUikDzN911wCdWJ640fh-nGy2EWE0votoLErhynF-m1y2nKpdllm6cW4fci5aUzzU8BYgHuvTut-bSeel5qBHR76npkB7wvAX7JqIYlO20r1xaRnrNiDwfKOSAwjxpI6P6akOqYfaz8pYBCY1NfkbdvqsgpLR92c5mbEjuCewoG-N-tehkV0fcJGRlIjCE30W40VwH8gh0KgiK-PbZTrhB-qCZzf7x0aArASF7uXo3bf2VtCyDjjH56yCHzvoPcHAv-.cpCui6TgtGNWXzOg0r3yJHkWLWCAtS9XwcA1L831D5hag==',
    'x-secsdk-csrf-token': '000100000001e157fca6480c52c5160fb6a2472c635314c2b1d0d6657636397174eaf2def204168a9e212c4e956b',  
    'cookie': 'passport_csrf_token_default=093ed211e214777fd670239baa280ecb; passport_csrf_token=093ed211e214777fd670239baa280ecb; tt_webid_v2=6971999491461809670; tt_webid=6971999491461809670; store-idc=maliva; store-country-code=gr; user_oec_info=0a53d5e654d67b19d8a98d879424bd25484521a97949fb5c9bd31d370b087081f39733e81ebe67f5a59bd4dea94774ea462c62e04575083e920ded2d3074520a85a73d5ca2a6889f285608641c543942afd071d90d1a490a3cc75dc9c6e7e9d56383eeffc70d3fe31a3fbcc5f0b47bc96cb5446186e9014d38d182745dde985d590a747ec4dd65fb72f75be0db7450efc82f65a99e1095a5f30c1886d2f6f20d2201047449565b; passport_auth_status=663b8e0b3bfbed8a98d01fff58405ef6%2C9dbd57fff74843dbd2d7beebbc55acf4; passport_auth_status_ss=663b8e0b3bfbed8a98d01fff58405ef6%2C9dbd57fff74843dbd2d7beebbc55acf4; sid_guard=0c740c639d30da8cbb64dc5cd896ef99%7C1623400939%7C5184000%7CTue%2C+10-Aug-2021+08%3A42%3A19+GMT; uid_tt=e69c74a107772d1be9d09418d6d2eeaa832ba036e3c2beca51346dafe829d6e2; uid_tt_ss=e69c74a107772d1be9d09418d6d2eeaa832ba036e3c2beca51346dafe829d6e2; sid_tt=0c740c639d30da8cbb64dc5cd896ef99; sessionid=0c740c639d30da8cbb64dc5cd896ef99; sessionid_ss=0c740c639d30da8cbb64dc5cd896ef99; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22version%22:%22v2%22}; s_v_web_id=verify_kq6momrt_C5HrhVSk_3FkL_4Xkz_9ADX_t4lofsJ89brD; tt_csrf_token=qUhaNvntPIzKrLtz0NvRslyM; R6kq3TV7=AFClqy56AQAAvzrGW26wIoq6LkyD-Vgf0qCskPKNAN9-xhzyPzP5RF_2ms1D|1|0|b7ccf4b09995b0e0234ad5e8cc2a5160d81493ed; csrf_session_id=9c41006cad9b4f519c7cdf47dba0c6eb; bm_sz=C97DEEAEE97DC3351A676D387E27B423~YAAQjtzNF/8DXSB6AQAAJqmrLgyqjpLV4evGoSlU5psTKaYChXmNVthAU9Zz3Umbg9LZzDBPsUxs5nArwu1qaUGaUFrqeRn2SPgaELkjYoTzSeKvTsBuB10jN6JGL0uXWLkGEG7t5x2xXgjdbphdTFfwbXw3YnnzRsKcAqCfV3P4mK0GImV26JX+eTwQ/iIa; _abck=510AEEF3282E5F8502C75DDE07A109C3~-1~YAAQjtzNFwAEXSB6AQAAJqmrLgbknHduwxUQfzFphu+WlIctNpdus/mE8HY9QkX+/E1nbR5nXWjz0qSo+DD5Ep4Y0APmwcTfNxat4LUFDXOqcWuwGid+Q7T2ZRqGPvrxY+dt+0fpTzuCWg3LPpwjBsoVZVf5mnVtaJOv043lQERqNymbPrsIA5cClkAfRlUJpcNKk6OtBuoUK8046pzfzD7zKQK0RrVLXc3xHtd7yJwq8ygHvrktCBssXUGsRlqbGmaGykXK1AA+NwpUnlhhSv+EN4PFxXmvRB+ZLUtAx9H0lHEkjGd1Tpo9EUWm7i/DpJHByZjlUHMojy+d28UVIMNESXv+zVMef318aZy8fZm6LaybxR8nObsdYRN+qWpvjtmsNZuOOhWEBw==~-1~-1~-1; ak_bmsc=1BAA3CB9DB778384F74B8224EF53D06B~000000000000000000000000000000~YAAQjtzNFwEEXSB6AQAAJqmrLgyDRBQeYt47HlP5lESZm/fl2Rhrk+ZuOy+TLBdOkzecU7XGaSE1IuGSnNou8hilaXlO6alL4LF2PeEg24cA0OpbmfcvZZWpZXXDiMQUjVVkTNd48eui4ul22/JC4VV2ifVESlqH6i6cqiE4lDIKZPqr4eDbt1AMjpdW5r87+nEDvC9aw6eD6wOo97KWzNrUwUzPmX8Hj+mEVKTCxQwC8oQ0jmxdAFocB4EDC/A/rBBKAKLO4uuvXepDSpjLveh0w2Z2sDX0FLEr4NUL3xaNqvV3sh9h4OIrAtUc+3Vj8FFUfDm9EzOkM8m2V6RbuZfZaYXJqVuHjoM40O3ZPgk5+sRL7JaB8nHRocwq63CxW8PEsur6WUPx4w==; csrf_session_id=9c41006cad9b4f519c7cdf47dba0c6eb; cmpl_token=AgQQAPOfF-RMpbD_ex__e108-qAdqolWP4QUYP6Law; bm_sv=9A7E65334A0CFB43042ECE63DDE1A539~ZDvcR8xEyNPVNpym797Wa/3+qIxVyUHNwSU1VJN7CcSVXuac/NqsgCJ9M3vFhYRKk5Lc+aG96ZP+KsUg/26egVRqQbNOp9QcSO96paSUd0DJGYpP8Jz/ut53q56c1WrWp3eAUm7Z9+H4wK14UUO1LNex1MxeOZ9uoTRXpNA/pLk=; passport_fe_beating_status=false; odin_tt=dce1c2c7916f83e8a9fe91b90fd171d3056799bbf0c29c9923b5507f2cd998069f86c6c113c7ba8f1a5523bb85813f73633a38d5ebfb92fc92231c310dff5c8643a6961638d0569060acd92475bdf713; ttwid=1%7C6hGVZU3Q391vcBYc4SoLdaaGuxQw3WulUsySdzEe6lU%7C1624283563%7C5d4209e59bf63dde4aacc427bee85d286965520e1319a9716f0a5a0c17aaa5bc'
}


params = (
    ('aid', '1233'),
    ('app_name', 'tiktok_web'),
    ('app_language', 'en'),
    ('device_id', '6971999491461809670'),
    ('device_platform', 'web_pc'),
    ('region', 'GR'),
    ('os', 'windows'),
    ('referer', ''),
    ('root_referer', ''),
    ('cookie_enabled', 'true'),
    ('screen_width', '472'),
    ('screen_height', '700'),
    ('browser_language', 'en-US'),
    ('browser_platform', 'Win32'),
    ('browser_name', 'Mozilla'),
    ('browser_version', '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'),
    ('browser_online', 'true'),
    ('timezone_name', 'Europe/Athens'),
    ('is_page_visible', 'true'),
    ('focus_state', 'true'),
    ('is_fullscreen', 'false'),
    ('history_len', '3'),
    ('battery_info', '1'),    
    ('unique_id', 'ppr'),
    ('fromWeb', '1'),
    ('_signature', '_02B4Z6wo00101H3UZmQAAIDCoZAbFyIF66R91GLAAH-te5'),   
)


response = requests.get('https://www.tiktok.com/api/uniqueid/check/', headers=headers, params=params)

print(response)
print(response.status_code)
print(response.content)
print(response.json())
print('''                             [\x1b[33m✓\x1b[39m] The username \x1b[33m\x1bs@ninter\x1b[39m is available on \x1b[33m\x1bsTikTok!\x1b[39m
    ''')

if response.json()['status_code'] == 0:
    input('''                             [\x1b[33m✓\x1b[39m] The username \x1b[33m\x1bs@ninter\x1b[39m is available on \x1b[33m\x1bsTikTok!\x1b[39m
    ''')
elif response.json()['status_code'] == 3249:
    input('''                             [\x1b[33m✓\x1b[39m] The username \x1b[33m\x1bs@ninter\x1b[39m is not available on \x1b[33m\x1bsTikTok!\x1b[39m
    ''')