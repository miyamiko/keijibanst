import streamlit as st
import pandas as pd
# from datetime import date
from datetime import datetime
# from dateutil.relativedelta import relativedelta
# import yfinance as yf #追加
# yf.pdr_override() #追加

st.title('掲示板　-　イチゲブログ')
st.caption('最下部の入力欄に書いてEnterしてください。削除も可能です。')
st.markdown('###### Streamelitやこのサイトの関連情報は')
link = '[イチゲブログ](https://kikuichige.com/17180/)'

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
    # sen='<hr size="60">'
    # st.write(sen, unsafe_allow_html=True)
#**********************************************
# print('for前'+str(kosuu))
#削除を押したあとに実行される下のfor文でkosuuが削除された分少なく更新されない
#理由はわからないがpassでエラーを無視した
# try:
#     for i in range(kosuu):
#         # print('for後'+str(kosuu))
#         if st.button("削除", key=i):
#             st.write(str(df.index[i]),'番削除')
#             df1=df.drop(i, axis=0)
#             df=df1
#             df.to_csv("toukou.csv")
#             kosuu-=1
#         st.write(str(df.index[i]),'番')
#         st.write('    日付:',df.iat[i,0])
#         st.write('    内容:',df.iat[i,1])
#         sen='<hr size="6">'
#         st.write(sen, unsafe_allow_html=True)
# except:
#     pass
#**********************************************

if prompt:
# 水平線を表示
    st.markdown("<hr>", unsafe_allow_html=True)
    message1 = st.chat_message("user")
    message1.write(f"内容：{prompt}")
    dt_now = datetime.now()
    toukoubi=dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
    columns = [ '投稿日','内容']
    list = [[toukoubi,prompt]]
    df_append = pd.DataFrame(data=list, columns=columns)
    df1 = pd.concat([df, df_append], ignore_index=True, axis=0)
    df=df1
    # df=df_append
    df.to_csv("toukou.csv")
    # text='<span style="color:blue">表示更新を押してください！</span>'
    # st.write(text, unsafe_allow_html=True)
#**********************************************
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
# st.dataframe(df)


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



    # x=df['内容'].count()
    # kosuu=int(x)
    # for i in range(kosuu):
    #     if st.button("削除", key=i):
    #         st.write('削除',str(i))
    #     st.write(str(i),'番')
    #     st.write('    日付:',df.iat[i,0])
    #     st.write('    内容:',df.iat[i,1])
#**********************************************
        # text='<span style="color:blue">df.iat[i,1]</span>'
        # st.write(text, unsafe_allow_html=True)
# else:
#     df1=df
# del_list=df.index.values

# st.title('簡易掲示板イチゲブログ')
# st.caption('csvファイルを使って掲示板作ってみました。')
# with st.form(key='keijiban_form'):
#     name=st.text_input('名前')
#     message=st.text_input('メッセージ')
#     st.text('投稿を押したあと表示更新を押してください。')
#     toukou_btn=st.form_submit_button('投稿')
#     hyouji_btn=st.form_submit_button('表示更新')
#     st.markdown('###### 簡易掲示板')
#     # del_no=st.text_input('削除する番号を選んでください')
#     #セレクトボックス
#     df=pd.read_csv("toukou.csv",index_col=0)
#     st.dataframe(df)
#     del_list=df.index.values
#     del_no=st.selectbox(
#             '削除する番号を選んでください',
#             (del_list))
#     # hyouji_btn=st.form_submit_button('削除直後や、セレクトボックスの値がおかしいときは、このボタンを押してください。セレクトボックスの番号がリフレッシュされます。')
#     del_btn=st.form_submit_button('削除')
#     if toukou_btn or hyouji_btn:
#         # df=pd.read_csv("toukou.csv",index_col=0)
#         if toukou_btn: 
#             dt_now = datetime.now()
#             toukoubi=dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
#             columns = [ '投稿日','名前','内容']
#             list = [[toukoubi,name,message
#             ]]
#             df_append = pd.DataFrame(data=list, columns=columns)
#             df1 = pd.concat([df, df_append], ignore_index=True, axis=0)
#             df=df1
#             df.to_csv("toukou.csv")
#             text='<span style="color:blue">表示更新を押してください！</span>'
#             st.write(text, unsafe_allow_html=True)
#         else:
#             df1=df
#         # df1
#         del_list=df.index.values
#         # del_no=st.selectbox(
#         #         '削除する番号を選んでください',
#         #         (del_list))
#     if del_btn:
#         # st.text('del_no'+del_no)
#         # df=pd.read_csv("toukou.csv",index_col=0)
#         df1=df.drop(del_no, axis=0)
#         # df1
#         df=df1
#         del_list=df.index.values
#         df.to_csv("toukou.csv")
#         text='<span style="color:red">表示更新を押してください！</span>'
#         st.write(text, unsafe_allow_html=True)