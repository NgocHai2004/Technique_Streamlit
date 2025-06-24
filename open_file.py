import streamlit as st
from PIL import Image

st.title("Upload file — Hiện ảnh hoặc text")


uploaded_file = st.file_uploader("Chọn file ảnh hoặc text", type=None)

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_type = uploaded_file.type

    st.write(f"Tên file: {file_name}")
    st.write(f"Kiểu file: {file_type}")

    if "image" in file_type:
      
        image = Image.open(uploaded_file)
        st.image(image, caption="Ảnh upload", use_column_width=True)

    elif "text" in file_type:
    
        content = uploaded_file.read().decode("utf-8")
        st.text_area("Nội dung file text:", content, height=200)

    else:
        st.warning("Loại file này chưa hỗ trợ hiển thị.")
