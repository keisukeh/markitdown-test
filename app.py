import streamlit as st
from markitdown import MarkItDown
import os
import pandas as pd

markitdown = MarkItDown()

st.title('MarkItDown Test APP')
file = st.file_uploader("Upload file")
if file:
    # 一時ファイルとして保存
    with open(file.name, "wb") as f:
        f.write(file.getbuffer())
    
    # ファイルパスを取得
    file_path = os.path.abspath(file.name)
    
    # CSVファイルを読み込み、Markdown形式に変換
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
        result = df.to_markdown(index=False)
    else:
        # 他の形式の場合はmarkitdown.convertを使用
        result = markitdown.convert(file_path)

    print(result.text_content)

    if result:
        st.code(result.text_content)
