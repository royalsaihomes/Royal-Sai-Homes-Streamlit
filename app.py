import streamlit as st

# Royal Sai Homes Data
APARTMENT_DATA = {
    "name": "Royal Sai Homes",
    "address": "Doddathogur Panchayath Office, Doddathoguru, Electronic City Phase I, Electronic City, Bengaluru, Karnataka 560100",
    "phone": "7204000530",
    "email": "royalsaihomes@gmail.com",
    "owner": "Sathisha Kumar",
    "description": "Premium rental apartments in the heart of Electronic City, Bengaluru. Experience comfortable living with modern amenities and excellent connectivity to IT hubs, schools, and shopping centers.",
    "features": [
        "Fully Furnished Apartments",
        "24/7 Security & CCTV Surveillance",
        "High-Speed Internet",
        "Power Backup",
        "Regular Housekeeping",
        "Modern Modular Kitchen",
        "Laundry Facilities",
        "Dedicated Parking Space"
    ]
}

# Streamlit App
st.set_page_config(
    page_title="Royal Sai Homes",
    page_icon="🏠",
    layout="wide"
)

# Hero Section
col1, col2 = st.columns([2, 1])
with col1:
    st.title("🏠 Royal Sai Homes")
    st.subheader("Premium Apartments in Electronic City, Bengaluru")
    st.write(APARTMENT_DATA["description"])

with col2:
    st.image("https://i.ibb.co/dJWT4r7m/IMG-20241119-095319.jpg", use_column_width=True)

st.markdown("---")

# Features Section
st.header("🏘️ Apartment Features")
features_cols = st.columns(2)
for i, feature in enumerate(APARTMENT_DATA["features"]):
    with features_cols[i % 2]:
        st.markdown(f"✅ {feature}")

st.markdown("---")

# Contact Section
st.header("📞 Contact Information")
contact_cols = st.columns(3)

with contact_cols[0]:
    st.subheader("📍 Address")
    st.write(APARTMENT_DATA["address"])

with contact_cols[1]:
    st.subheader("📞 Phone")
    st.write(APARTMENT_DATA["phone"])

with contact_cols[2]:
    st.subheader("📧 Email")
    st.write(APARTMENT_DATA["email"])

st.write(f"**Managed by:** {APARTMENT_DATA['owner']}")

# Footer
st.markdown("---")
st.markdown("© 2024 Royal Sai Homes. All rights reserved.")