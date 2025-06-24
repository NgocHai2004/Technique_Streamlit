import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model Qwen
model_name = "Qwen/Qwen3-0.6B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

st.title("Giải bài tập Vật Lý với Qwen3-0.6B")

# Nhập bài toán
user_prompt = st.text_area("1+1 =?")

if st.button("Giải bài"):
    if user_prompt.strip() == "":
        st.warning("Vui lòng nhập bài toán!")
    else:
        messages = [
            {"role": "system", "content": "Bạn là một chuyên gia giải bài tập vật lý. Giải bài tập vật lý sau đây từng bước. Thế số và kết luận."},
            {"role": "user", "content": user_prompt}
        ]

        # Apply chat template
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        # Encode text
        input_ids = tokenizer(text, return_tensors="pt").to(model.device)

        # Generate response
        output_ids = model.generate(
            **input_ids,
            max_new_tokens=512,
            temperature=0.7
        )

        # Decode output
        response = tokenizer.decode(output_ids[0][input_ids['input_ids'].shape[-1]:], skip_special_tokens=True)

        st.markdown("### 📖 Lời giải:")
        st.write(response)
