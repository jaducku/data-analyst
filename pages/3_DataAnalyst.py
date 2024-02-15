import streamlit as st

import pandas as pd
import streamlit_shadcn_ui as ui
from streamlit_extras.card import card
from streamlit_extras.chart_container import chart_container 

loaded_data = [
    {"invoice": "INV001", "paymentStatus": "Paid", "totalAmount": 500, "paymentMethod": "Credit Card"},
    {"invoice": "INV002", "paymentStatus": "Unpaid", "totalAmount": 200, "paymentMethod": "Cash"},
    {"invoice": "INV003", "paymentStatus": "Paid", "totalAmount": 150, "paymentMethod": "Debit Card"},
    {"invoice": "INV004", "paymentStatus": "Unpaid", "totalAmount": 350, "paymentMethod": "Credit Card"},
    {"invoice": "INV005", "paymentStatus": "Paid", "totalAmount": 400, "paymentMethod": "PayPal"},
]

# Creating a DataFrame
invoice_df = pd.DataFrame(loaded_data)

#Table
ui.table(data=invoice_df, maxHeight=300)

# 질문 Input 및 Button
textarea_value = ui.textarea(placeholder="Type your message here...", key="query")
clicked = ui.button("요청", key="clk_req_btn", variant="secondary", className="w-full")

if clicked:
    with chart_container(loaded_data):
        st.write("Here's a cool chart")
        st.area_chart(loaded_data)