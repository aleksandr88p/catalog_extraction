import requests

cookies = {
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.digikey.es/en/products/filter/ceramic-capacitors/60?s=N4IgrCBcAEoA5WgRgCwCYA00RwTJADAQL7FA',
    'authorization': 'Bearer',
    'lang': 'en',
    'request-context': 'appId=cid-v1:40371992-8794-4ad9-9011-4552f68fdb07',
    'request-id': '|929c088e24fd40b0b82cad8a213b2f7e.4150575a88724614',
    'site': 'es',
    'traceparent': '00-929c088e24fd40b0b82cad8a213b2f7e-4150575a88724614-01',
    'x-currency': 'EUR',
    'x-request-id': '1f30f381-dd80-4a73-8b51-614f5051d507',
    'Alt-Used': 'www.digikey.es',
    'Connection': 'keep-alive',
    # 'Cookie': 'search=%7B%22usage%22%3A%7B%22dailyCount%22%3A2%2C%22lastRequest%22%3A%222024-02-15T19%3A43%3A17.456Z%22%7D%2C%22version%22%3A1%7D; ai_user=nPmofiOQHynSNXmv2dKD5v|2024-02-15T01:03:08.185Z; _pxhd=9862e1044edd564f12a996d2fd9fd226fa1f4acfe583a4aee3e676d2feb5e26d:fb35fd4a-cb9d-11ee-be19-791effb23b8c; utag_main=v_id:018daa49fcec000256b1785e8cb40504e006301100bd0$_sn:2$_se:4$_ss:0$_st:1708028201561$ses_id:1708026200068%3Bexp-session$_pn:2%3Bexp-session; dk_tagxi=undefined.0.1708026381; _pxvid=fb35fd4a-cb9d-11ee-be19-791effb23b8c; ping-accept-language=en-ES; dk_item_data=item_list_id=60&item_list_name=PS-FAM; _ga_1TEG8CV4XM=GS1.1.1708026200.2.1.1708026409.32.0.0; _ga=GA1.2.546556993.1707958994; EG-U-ID=A969aa8c2f-70cf-4a59-97e0-bba89f761788; _gid=GA1.2.1194005933.1707959162; _gcl_au=1.1.97676242.1707959162; _fbp=fb.1.1707959162374.211955395; _evga_3cfa=0c9e8b0c6616c025.; ai_session=eUGpVmr+eJjOpGt8IlJOoK|1708026197457|1708026382084; TS01173021=01694a1a6e51f6c9bbd6631bba0987cbf0b9663d72337e8c7ca6adef4ec157158566fd3e8bd46641ba9f9facb4e1c28a35e092331f; TS112fb876027=080716a071ab20001912c622f6c53419dd29a750ba674fc752c673c3e5c0bfba9cf31524a1a7441508f9234b07113000caab07835425707f03ab4c856b6d5f0b9d38ee3c5af19a50e2f320985d2c54ff0431276b1384dac2a8514f01d39274bf; dkc_tracker=3639838598425; _dd_s=rum=0&expire=1708027309910; TS019f5e6c=01c72bed215de8d292c44d098ffdc11bd27b744d1d871a96a6270fc640bc7f425d47588d3da97d5ca7830914128365b1e22ca367ca; TSbafe380b027=08a1509f8aab2000c55b1afc06efacfeaa37a7f642bf5c8017854500940d24b409c51e9eea2bfcf908cecc1dff113000bcb2a50da6c6cf5f7d123b3889cfa1ca052dee032c172e3bf320f908f3bac60e55d7ca4ff19ae9735c052484b354d0ce; TS016ca11c=01c72bed21c94d1edcf244e7d6819ae28bd83ea698c1461589c6382ce5bb583c0bc610601d43d7a042581e0d4d442880ec6b610f61; TSc580adf4027=08a1509f8aab20001acc2f67019390d8db036b06519c7986986dc4d94e8f3fde490734ee8ca9d33f0828dcf65e113000c4e055e7ab8b4f3c7d123b3889cfa1ca390ce92325a28f44c05b9aa91d7df51a3787f71b1426efb8f5d0e1f97f97e721; search_prefs=%7B%22theme%22%3A%22light%22%7D; EG-S-ID=E4fb6b4ce4-01fb-4ed9-a474-d99c123348d0; _cs_mk=0.7101882505902128_1708026224900; pxcts=7869668c-cc3a-11ee-9b97-7965598a3186; _pxde=4ddaaa987f62b52891a03ec6494f52a0df8d3e4df53acf5594647ac1bb10af34:eyJ0aW1lc3RhbXAiOjE3MDgwMjY0MDQzNzIsImZfa2IiOjAsImlwY19pZCI6W119; _px2=eyJ1IjoiZTUxM2JlYjAtY2MzYS0xMWVlLWE1OTMtMDUwYzNkNzAyNDdmIiwidiI6ImZiMzVmZDRhLWNiOWQtMTFlZS1iZTE5LTc5MWVmZmIyM2I4YyIsInQiOjE3MDgwMjY2ODMyOTIsImgiOiI3YWVmYjMwZTBlZTcxM2ZjNDNkNTk3NzVmYjVjODcxMzU2MTYxNGI3YzI3ODZjYTVkODNlOTlkMGQzZWVmZDhiIn0=; TS0f82a39e027=08ddc8ffffab2000a2a603f0cb42ce4d620ce39effaaaa529969667010350805da31aefba0580e4d0815d08638113000b35d4057a154a2d59ff5d78cc8f07299a68bdc3f225e26538f8bc8ebc8c0760a2ab7b932bb7f2e6c0e690b73f8c61a42; _gat_Production=1; _uetsid=630ff420cb9e11eeacdb5f8159546f10; _uetvid=630ffaa0cb9e11ee924dc53d77b8cd6a; utm_data_x=available_parameters%3D-1%40%40-4%40%40-5%40%401989%40%402049%40%403%40%4014%40%4017%40%40252%40%405%40%40707%40%40405%40%401531%40%4069%40%4016%40%4046%40%401500%40%401501%40%40508%40%404%2Cselected_parameters%3D%22%22%2Cref_page_event%3DSelect%20Part%2Cref_page_type%3DPS%2Cref_page_sub_type%3DFAM%2Cref_page_id%3D60%2Cccookie%3D2024-02-15T01%3A06%3A01.989Z%2Cref_part_id%3D3726140%2Cref_pn_sku%3D399-9718-ND%2Cref_page_state%3DSort%20Order%20Test%20-%20Default%2Cref_pers_state%3D%7B%22%5C%22PLS%5C%22%22%3A%22Scrolling%22%7D%2Cref_part_search_term%3D%2Cref_part_search_term_ext%3D%2CExtRun%3D450.3%7C409.2%7C429.2%7C428.1%7C428.5%7C450.1%7C409.1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'returnSeparatePricing': 'true',
}

response = requests.get(
    'https://www.digikey.es/products/api/v5/detail-page/3726140',
    params=params,
    cookies=cookies,
    headers=headers,
)


with open('one_product.json', 'w') as outfile:
    outfile.write(response.text)