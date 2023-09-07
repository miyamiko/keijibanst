import streamlit as st
import pandas as pd
# from datetime import datetime
import datetime

st.title('掲示板　-　イチゲブログ')
st.caption('最下部の入力欄に書いてEnterしてください。削除も可能です。')
st.markdown('###### Streamelitやこのサイトの関連情報は')
link = '[イチゲブログ](https://kikuichige.com/21772/)'

prompt=st.chat_input("何か書いてEnterまたは右のボタンをクリック！")
st.markdown(link, unsafe_allow_html=True)
df=pd.read_csv("toukou.csv",index_col=0)
x=df['内容'].count()
kosuu=int(x)
for i in range(kosuu):
    # 水平線を表示
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write(str(df.index[i]),'番')
    st.write('    日付:',df.iat[i,0])
    st.write('    内容:',df.iat[i,1])

if prompt:
# 水平線を表示
    st.markdown("<hr>", unsafe_allow_html=True)
    message1 = st.chat_message("user")
    message1.write(f"内容：{prompt}")
    # dt_now = datetime.now()
    t_delta = datetime.timedelta(hours=9)  # 9時間
    JST = datetime.timezone(t_delta, 'JST')  # UTCから9時間差の「JST」タイムゾーン
    dt_now = datetime.datetime.now(JST)  # タイムゾーン付きでローカルな日付と時刻を取得

    toukoubi=dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
    columns = [ '投稿日','内容']
    list = [[toukoubi,prompt]]
    df_append = pd.DataFrame(data=list, columns=columns)
    df1 = pd.concat([df, df_append], ignore_index=True, axis=0)
    df=df1
    df.to_csv("toukou.csv")

# 水平線を表示
st.markdown("<hr>", unsafe_allow_html=True)
with st.form(key='keijiban_form'):
    del_list=df.index.values
    del_no=st.selectbox(
            '削除する番号を選んでください',
            (del_list))
    del_btn=st.form_submit_button('削除')
    if del_btn:
        df1=df.drop(del_no, axis=0)
        df=df1
        del_list=df.index.values
        df.to_csv("toukou.csv")
        text='<span style="color:red">表示更新を押してください！</span>'
        st.write(text, unsafe_allow_html=True)

# カスタムCSSスタイルを定義
custom_css = """
<style>
hr {
    border: none;
    border-top: 2px solid red;
    margin: 20px 0;
}
.red-bold {
    color: red;
    font-weight: bold;
}
</style>
"""

# カスタムCSSスタイルを適用
st.markdown(custom_css, unsafe_allow_html=True)

# 水平線を表示
st.markdown("<hr>", unsafe_allow_html=True)
# 赤い太字の文字を表示
st.markdown("<span class='red-bold'>ここは管理者用です。</span>", unsafe_allow_html=True)

# 水平線の下にコンテンツを追加
# st.write("ここは水平線の下に表示されるコンテンツです。")
# CSVファイルをダウンロードするボタンを追加
st.download_button(
    label="管理人用CSVファイルのダウンロード",
    data=df.to_csv().encode('utf-8'),  # データフレームをCSV形式に変換してエンコード
    file_name='toukou.csv',  # ダウンロードするファイル名を指定
    key='download-button'
)

# CSVファイルをアップロードするウィジェットを追加
uploaded_file = st.file_uploader("管理人用CSVファイルのアップロード", type=["csv"])

# アップロードされたファイルが存在する場合
if uploaded_file is not None:
    # アップロードされたファイルをデータフレームに読み込む
    df7 = pd.read_csv(uploaded_file,index_col=0)
    
    # データフレームを表示
    # st.write("アップロードされたデータフレーム:")
    # st.write(df7)
    df7.to_csv("toukou.csv")
# 水平線を表示
st.markdown("<hr>", unsafe_allow_html=True)
