import streamlit as st

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    header {visibility: hidden;}
    
    /* Hide the GitHub icon */
    .viewerBadge_container__1QSob {display: none !important;}

    /* Hide streamlit branding */
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
    
    /* Remove extra padding */
    .block-container {padding-top: 1rem;}
    
    /* Hide any other Streamlit elements */
    .stAppViewerBadge {display: none;}
    [data-testid="stAppViewContainer"] > .main {background-color: transparent;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Royal Sai Homes Data
APARTMENT_DATA = {
    "name": "Royal Sai Homes",
    "address": "Doddathogur Panchayath Office, Doddathoguru, Electronic City Phase I, Electronic City, Bengaluru, Karnataka 560100",
    "email": "royalsaihomes@gmail.com",
    "owner": "Sathisha Kumar",
    "description": "Premium rental apartments in the heart of Electronic City, Bengaluru. Experience comfortable living with modern amenities and excellent connectivity to IT hubs, schools, and shopping centers.",
    "features": [
        "Semi / Fully Furnished Apartments",
        "24/7 CCTV Surveillance",
        "UPS Power Backup",
        "Common Area Cleaning",
        "Solar / Geyser Hot Water Supply",
        "Parking Space"
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

    st.markdown("""
    <div style="margin-top: 15px;">
        <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d124475.28213937675!2d77.51207470893863!3d12.852797488383718!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae6c9e5e214983%3A0xf8a48b8d4d32ceb8!2sRoyal%20Sai%20Homes!5e0!3m2!1sen!2sin!4v1763478730572!5m2!1sen!2sin" 
            width="100%" 
            height="200" 
            style="border:0; border-radius: 8px;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
        </iframe>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="margin-top: 10px;">
        <a href="https://www.google.com/maps/dir/?api=1&destination=Royal+Sai+Homes,+Doddathogur+Panchayath+Office,+Doddathoguru,+Electronic+City+Phase+I,+Electronic+City,+Bengaluru,+Karnataka+560100" 
           target="_blank" 
           style="background-color: #FF6B00; color: white; padding: 8px 16px; text-decoration: none; border-radius: 5px; display: inline-block;">
           🗺️ Get Directions
        </a>
    </div>
    """, unsafe_allow_html=True)

with contact_cols[2]:
    st.subheader("📧 Email")
    st.write(APARTMENT_DATA["email"])

st.write(f"**Managed by:** {APARTMENT_DATA['owner']}")

# Footer
st.markdown("---")
st.markdown("© 2024 Royal Sai Homes. All rights reserved.")
