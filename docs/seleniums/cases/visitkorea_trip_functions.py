from bs4 import BeautifulSoup

def set_content_items(content_items):
    match_list = ['시작일', '종료일', '전화번호', '홈페이지', '주소', '행사장보'
            ,'주최', '주관', '이용요금', '행사시간']
    row = [''] * len(match_list)
    for content in content_items:
        match_item = content.select_one('li > strong').text
        if match_item in match_list:
            add_item = content.select_one('li > span').text
            match_index = match_list.index(match_item)
            row[match_index] = add_item
    return row

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    row = list()
    # 행사명
    row.append(soup.select_one('#topTitle').text)
    # 행사 부제목명
    subtitle = soup.select_one('.titTypeWrap')
    if subtitle:    # 없을 때를 위한 안전 코드
        row.append(subtitle.text)


    contents = soup.select('.inr_wrap > .inr')
    
    # 세부 정보(일정, 연락처 등)
    row.extend(set_content_items(contents[1].select('.inr_wrap > .inr > ul > li')))
    # 참조 내용
    row.append(contents[0].text)    

    return row

import pandas as pd

def store_datas(datas, columns):
    korea_trip = pd.DataFrame(data=datas, columns=columns)
    pass
    return 

