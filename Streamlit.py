import streamlit as st

st.title('첫번째 웹 어플 만들기😄')

#텍스트
st.header('텍스트 출력')
st.write('') #빈 줄 삽입

st.write('# 마크다운 H1 : st.write()')
st.write('### 마크다운 H3 : st.write()')
st.write('- 목록')
st.write('')

st.title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.write('')

st.markdown('## 마크다운 : st.markdown()')
st.markdown('''
1. ordered item
- unordered item
- unordered item
2. ordered item     
3. ordered item
10. ordered item
''')
st.divider() # 👈 구분선

# 마크다운
'''# 👑 Magic에 마크다운을 조합
1. ordered item
- 강조: **unordered item**
- 기울임: *unordered item*
2. ordered item
3. ordered item
'''

# 데이터프레임
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 
                   'B': [4, 5, 6],
                   'name': ['asdd','ddg','dfghtg']})
df # 👈 데이터프레임 출력

# 차트
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
fig # 👈 차트 출력
