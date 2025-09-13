import streamlit as st
import google.generativeai as genai

# --- Configure Gemini API ---
genai.configure(api_key="AIzaSyCM4vIdZylsML_EvYub0ky-ynPuJtYXvUE")  # apni API key yahan lagao

# --- E-commerce Knowledge Base ---
faq_knowledge = """
You are an E-commerce customer support assistant.

Company Name: FashionHub
Industry: Fashion & Lifestyle E-commerce
Tagline: Style that defines you
Website: www.fashionhub.com

Contact Email: support@fashionhub.com
Contact Number: +1 (800) 555-FASH
Live Chat: Available on website & mobile app
Instagram: @fashionhub_official
Facebook: FashionHub
Twitter/X: @fashionhub

Return Policy: 7 days free return (no questions asked)
Refund Policy: Refunds processed within 3-5 business days after item inspection
Exchange Policy: Free exchange within 7 days (size/color issues)
Delivery Time: 3-5 business days (standard) / 1-2 business days (express)
Shipping Charges: Free shipping on orders above $50
International Shipping: Available to 50+ countries (charges vary)
Warranty: 6-month stitching guarantee on all FashionHub branded items

Order Tracking: Real-time tracking via email & SMS
Payment Options: Credit/Debit Card, PayPal, Cash on Delivery (selected regions)
Support Areas: Order Placement, Size Guide, Returns, Refunds, Product Availability, Discounts, Account Issues, Delivery Queries, Gift Cards

Personal Stylist: AI-powered outfit suggestions
Size Assistant: Helps choose the perfect fit
Loyalty Program: Earn Style Points with every purchase
Birthday Discounts: Exclusive coupons on birthdays
FashionHub Care: Free stitching repair within 6 months

Example orders:
- Order #12345: Shipped, will be delivered on 10th September.
- Order #67890: Processing, expected delivery: 12th September.
"""

# --- Function to handle chatbot queries ---
def ecommerce_chatbot(user_query):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(
        f"{faq_knowledge}\n\nUser: {user_query}\nAssistant:"
    )
    return response.text

# --- Streamlit UI ---
st.set_page_config(page_title="FashionHub Support Assistant", page_icon="🛍️")

st.title("🛍️ FashionHub Customer Support Assistant")
st.write("Welcome to FashionHub! Ask me anything about your orders, returns, delivery, or products.")

# Input box
user_query = st.text_input("Your Question:")

if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Assistant is typing..."):
            answer = ecommerce_chatbot(user_query)
        st.success(f"**Assistant:** {answer}")
    else:
        st.warning("Please enter a question before submitting.")
