import streamlit as st
import pyrebase
from datetime import datetime

# === YOUR FIREBASE CONFIG ===
firebase_config = {
    "apiKey": "AIzaSyAPcETVnAOWJBzlnmwkgT_Mve98gWyYQwg",
    "authDomain": "royal-sai-homes.firebaseapp.com",
    "databaseURL": "https://royal-sai-homes-default-rtdb.firebaseio.com",
    "projectId": "royal-sai-homes",
    "storageBucket": "royal-sai-homes.firebasestorage.app",
    "messagingSenderId": "713626045208",
    "appId": "1:713626045208:web:635a0025a31b410fc6ec6d"
}

# Initialize Firebase
try:
    firebase = pyrebase.initialize_app(firebase_config)
    db = firebase.database()
    # st.success("✅ Connected to Firebase")  # Optional: remove comment to see connection status
except Exception as e:
    st.error(f"❌ Firebase connection failed: {e}")

# Function to save enquiry to Firebase
def save_enquiry_to_firebase(name, mobile, apartment, people):
    try:
        enquiry_data = {
            'name': name,
            'mobile': mobile,
            'apartment': apartment,
            'people': people,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'status': 'new'
        }
        
        # Save to Firebase Realtime Database
        db.child("enquiries").push(enquiry_data)
        return True
    except Exception as e:
        st.error(f"Error saving enquiry: {str(e)}")
        return False

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

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
        padding: 15px 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-left: 20px;
        padding-right: 20px;
    }
    .nav-brand {
        font-size: 24px;
        font-weight: bold;
        color: #2c5aa0;
    }
    .nav-buttons {
        display: flex;
        gap: 20px;
    }
    .nav-button {
        background: none;
        border: 2px solid #2c5aa0;
        color: #2c5aa0;
        font-size: 16px;
        cursor: pointer;
        padding: 8px 20px;
        border-radius: 25px;
        transition: all 0.3s;
        font-weight: 500;
        text-decoration: none;
    }
    .nav-button:hover {
        background: #2c5aa0;
        color: white;
    }
    .main-content {
        margin-top: 80px;
    }
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Simple navigation using URL parameters
st.markdown("""
<div class="floating-nav">
    <div class="nav-brand">🏠 Royal Sai Homes</div>
    <div class="nav-buttons">
        <a href="/?page=home" class="nav-button">🏠 Home</a>
        <a href="/?page=gallery" class="nav-button">📸 Gallery</a>
        <a href="/?page=enquiry" class="nav-button">📝 Enquiry</a>
    </div>
</div>
<div class="main-content">
""", unsafe_allow_html=True)

# Get current page from URL
query_params = st.experimental_get_query_params()
current_page = query_params.get('page', ['home'])[0]

# Page Content based on navigation
if current_page == 'home':
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

    st.set_page_config(page_title="Royal Sai Homes", page_icon="🏠", layout="wide")

    # Hero Section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("🏠 Royal Sai Homes")
        st.subheader("Premium Apartments in Electronic City Phase 1, Bengaluru")
        st.write(APARTMENT_DATA["description"])

    with col2:
        st.image("https://i.ibb.co/dJWT4r7m/IMG-20241119-095319.jpg", use_column_width=True)

    st.markdown("---")
    st.header("🏘️ Apartment Facilities")
    features_cols = st.columns(2)
    for i, feature in enumerate(APARTMENT_DATA["features"]):
        with features_cols[i % 2]:
            st.markdown(f"✅ {feature}")

    st.markdown("---")
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

elif current_page == 'gallery':
    st.title("📸 Gallery")
    st.write("Gallery page coming soon...")
    
elif current_page == 'enquiry':
    st.title("📝 Enquiry Form")
    st.write("Interested in our apartments? Fill out the form below and we'll get back to you soon!")
    
    # Enquiry Form
    with st.form("enquiry_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Full Name *", placeholder="Enter your full name")
        
        with col2:
            mobile = st.text_input("Mobile Number *", placeholder="Enter your 10-digit mobile number")
        
        apartment_options = [
            "Select Apartment",
            "GF1 - Ground Floor 1", "GF2 - Ground Floor 2", 
            "FF1 - First Floor 1", "FF2 - First Floor 2", "FF3 - First Floor 3", "FF4 - First Floor 4",
            "SF1 - Second Floor 1", "SF2 - Second Floor 2", "SF3 - Second Floor 3", "SF4 - Second Floor 4"
        ]
        
        selected_apartment = st.selectbox("Preferred Apartment *", apartment_options)
        
        people_options = ["1", "2", "3", "4", "5", "6+"]
        num_people = st.selectbox("Number of People *", ["Select number"] + people_options)
        
        submitted = st.form_submit_button("Submit Enquiry", type="primary")
        
        if submitted:
            if not name or not mobile or selected_apartment == "Select Apartment" or num_people == "Select number":
                st.error("Please fill all required fields marked with *")
            elif len(mobile) != 10 or not mobile.isdigit():
                st.error("Please enter a valid 10-digit mobile number")
            else:
                if save_enquiry_to_firebase(name, mobile, selected_apartment, num_people):
                    st.success("✅ Thank you for your enquiry! We have received your details and the owner will contact you shortly.")
                    st.info(f"""
                    **Enquiry Summary:**
                    - **Name:** {name}
                    - **Mobile:** {mobile}
                    - **Preferred Apartment:** {selected_apartment}
                    - **Number of People:** {num_people}
                    - **Submitted at:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    """)
                else:
                    st.error("Failed to save enquiry. Please try again.")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("© 2024 Royal Sai Homes. All rights reserved.")
