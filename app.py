import streamlit as st

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'menu_open' not in st.session_state:
    st.session_state.menu_open = False

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
    
    /* Floating Navigation Bar */
    .floating-nav {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        z-index: 1000;
        padding: 15px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .nav-brand {
        font-size: 24px;
        font-weight: bold;
        color: #2c5aa0;
    }
    .hamburger-container {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .main-content {
        margin-top: 80px;
    }
    
    /* Menu styles */
    .menu-container {
        position: fixed;
        top: 70px;
        right: 20px;
        background: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        border-radius: 8px;
        padding: 10px;
        z-index: 1001;
        min-width: 150px;
    }
    .menu-item {
        display: block;
        width: 100%;
        padding: 12px 15px;
        background: none;
        border: none;
        text-align: left;
        cursor: pointer;
        font-size: 16px;
        color: #333;
        border-radius: 5px;
        margin-bottom: 5px;
        transition: background 0.3s;
    }
    .menu-item:hover {
        background: #f0f0f0;
    }
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Floating Navigation Bar
st.markdown("""
<div class="floating-nav">
    <div class="nav-brand">🏠 Royal Sai Homes</div>
    <div class="hamburger-container">
""", unsafe_allow_html=True)

# Hamburger button using Streamlit
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("☰", key="hamburger"):
        st.session_state.menu_open = not st.session_state.menu_open

st.markdown("""
    </div>
</div>
<div class="main-content">
""", unsafe_allow_html=True)

# Show menu if open
if st.session_state.menu_open:
    st.markdown("""
    <div class="menu-container">
        <button class="menu-item" onclick="window.location.href='/?page=home'">🏠 Home</button>
        <button class="menu-item" onclick="window.location.href='/?page=gallery'">📸 Gallery</button>
        <button class="menu-item" onclick="window.location.href='/?page=enquiry'">📝 Enquiry</button>
    </div>
    """, unsafe_allow_html=True)

# Handle page navigation from URL parameters
try:
    query_params = st.experimental_get_query_params()
    if 'page' in query_params:
        st.session_state.current_page = query_params['page'][0]
        st.session_state.menu_open = False  # Close menu on navigation
except:
    pass

# Page Content based on navigation
if st.session_state.current_page == 'home':
    # Your existing homepage content
    APARTMENT_DATA = {
        "name": "Royal Sai Homes",
        "address": "Doddathogur Panchayath Office, Doddathoguru, Electronic City Phase I, Electronic City, Bengaluru, Karnataka 560100",
        "email": "royalsaihomes@gmail.com",
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

    st.set_page_config(
        page_title="Royal Sai Homes",
        page_icon="🏠",
        layout="wide"
    )

    # Hero Section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("🏠 Royal Sai Homes")
        st.subheader("Premium Apartments in Electronic City Phase 1, Bengaluru")
        st.write(APARTMENT_DATA["description"])

    with col2:
        st.image("https://i.ibb.co/dJWT4r7m/IMG-20241119-095319.jpg", use_column_width=True)

    st.markdown("---")

    # Features Section
    st.header("🏘️ Apartment Facilities")
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

elif st.session_state.current_page == 'gallery':
    st.title("📸 Gallery")
    st.write("Gallery page coming soon...")
    
elif st.session_state.current_page == 'enquiry':
    st.title("📝 Enquiry Form")
    st.write("Enquiry form coming soon...")

# Close the main-content div
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("© 2024 Royal Sai Homes. All rights reserved.")
