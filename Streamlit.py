from shapely import wkt
import streamlit as st
import folium
import pandas as pd
from streamlit.components.v1 import iframe
import pandas as pd
import openpyxl
import pandas as pd
import geopandas as gpd
import json

st.title('지도 시각화')

#텍스트
st.header('행정구역별 출생률 지도 시각화')
df_br = pd.read_excel('assignment_3_df.xlsx')

st.write(df_br.head())

# GeoDataFrame 로딩
gdf_SGG = gpd.read_file('TL_SCCO_SIG.json')


# 'geometry' 컬럼을 WKT 형식으로 변환하여 'geometry_wkt'라는 새로운 컬럼에 저장
gdf_SGG['geometry_wkt'] = gdf_SGG['geometry'].apply(lambda x: wkt.dumps(x))


# 변환된 GeoDataFrame 출력
st.write(gdf_SGG[['SIG_KOR_NM', 'geometry_wkt']].head())

# 처리 함수 정의
def process_location(data):
    processed_data = []
    stored_prefixes = []
    
    for word in data:
        # 길이가 5보다 크고, 3번째 문자가 '시'인지 확인
        if len(word) > 5 and word[2] == '시':
            # 공백을 기준으로 나누거나, 3번째 이후를 추출
            if " " in word:
                parts = word.split(" ")
            else:
                parts = [word[:3], word[3:]]
            # 결과 저장
            stored_prefixes.append(parts[0])  # [0] 인덱스를 별도로 저장
            processed_data.append(parts[1])  # [1] 인덱스로 교체
        else:
            processed_data.append(word)  # 조건에 맞지 않으면 그대로 저장
    
    return processed_data, stored_prefixes


# 적용 함수
def apply_processing(row):
    processed, prefixes = process_location([row])
    return processed[0]  # 결과에서 첫 번째 값 반환

# 데이터프레임 컬럼 생성
gdf_SGG_filtered = gdf_SGG.copy()   
gdf_SGG_filtered['행정구역'] = gdf_SGG['SIG_KOR_NM'].apply(apply_processing)

# 결과 확인
st.write(gdf_SGG_filtered.head())
# 한국 시각화

title = '한국 시군구 별 출산율'
title_gtml = title_html = f'<h3 align="center" style="font-size:20px"><b>{title}</b></h3>'

korea = [35.907757, 127.766922] # 대한민국

korea_map = folium.Map(
    location = korea,
    zoom_start=7,
    tiles = 'cartodbpositron'
)
korea_map.get_root().html.add_child(folium.Element(title_html))

# korea_map.save('data/korea_map.html') # 지도 저장

# Choropleth map 그리기

folium.Choropleth( 
    geo_data = gdf_SGG_filtered,
    data = df_br,
    columns= ('행정구역별','합계출산율'),
    key_on='feature.properties.행정구역', # key
    fill_color = 'BuPu',
    fill_opacity = 0.7,
    line_opacity = 0.5,
    legend_name = '출산율'
).add_to(korea_map)
