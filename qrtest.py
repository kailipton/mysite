import qrcode
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# img = qrcode.make('https://www.google.co.jp/')
# img.save('/Applications/kai_work/python/python-test/qrtes.png')

st.title('mytestapp入門')
st.write('dataframe')

df1 = pd.DataFrame({
    '1ren': [1,2,3,4],
    '2ren': [10,20,30,40]
})

# write()では表の細かい設定はできない
# dataframe()では表の縦横の長さを指定できる
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=500, height=300)

# dataframe()は動的なテーブルを使いたい時
# table()は静的なテーブルを使いたい時
st.table(df1.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

# 図を描画
st.dataframe(df2)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

# 地図を表示
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.dataframe(df3)
st.map(df3)


if st.checkbox('show image'):
    # checkboxはtrueかfalseを返す
    # 画像を表示
    # 他にも音声や動画を簡単に表示できる
    img = Image.open('/Applications/kai_work/python/python-test/qrtes.png')
    st.image(img, caption='qrtest', use_column_width=True)

option = st.selectbox(
    '好きな数字は？',
    list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です。'

st.write('interactive widgets')
text = st.text_input('your like number')
'あなたは、', text, 'です'

# condition = st.slider('今日の調子は？', 0, 100, 50)
condition = st.sidebar.slider('今日の調子は？', 0, 100, 50)

'コンディション', condition, 'です'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.expander('aaa')
expander1.write('aaaa')
expander2 = st.expander('bbb')
expander2.write('bbbb')

st.write('barwrite!!!')
'start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'































