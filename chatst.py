import streamlit as st
import numpy as np

# with st.chat_message("user"):
#     st.write("Hello 👋")
    # st.line_chart(np.random.randn(30, 3))
message = st.chat_message("assistant")
message.write("Hello human")
# message.bar_chart(np.random.randn(30, 3))

prompt=st.chat_input("何か言ってよ")
if prompt:
    st.write(f"言ったよ{prompt}")
    message1 = st.chat_message("user")
    message1.write(prompt)
