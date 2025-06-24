import streamlit as st

st.title("Kiểm tra tuổi người dùng")

ten = st.text_input("Nhập tên của bạn:")
tuoi = st.text_input("Nhập tuổi của bạn:")

if st.button("Kiểm tra"):
    if ten == "" or tuoi == "":
        st.error("Vui lòng nhập đầy đủ tên và tuổi!")
    else:
        try:
            tuoi_int = int(tuoi)
            if tuoi_int >= 20:
                ket_qua = "Già"
            else:
                ket_qua = "Trẻ"
            st.success(f"Xin chào {ten}, bạn {tuoi_int} tuổi và bạn là: {ket_qua}")

        except ValueError:
            st.error("Vui lòng nhập tuổi là một số nguyên hợp lệ!")

