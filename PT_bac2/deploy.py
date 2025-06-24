import streamlit as st
from ham_giai_pt import giai_pt_bac_2

# Tiêu đề ứng dụng
st.title("Giải phương trình bậc 2")

st.write("Phương trình có dạng: **ax² + bx + c = 0**")

# Nhập hệ số
a = st.number_input("Nhập hệ số a:", value=1)
b = st.number_input("Nhập hệ số b:", value=0)
c = st.number_input("Nhập hệ số c:", value=0)

# Nút giải
if st.button("Giải phương trình"):
    ket_qua = giai_pt_bac_2(a, b, c)
    st.write(ket_qua)
