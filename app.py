import streamlit as st
import base64

# -----------------------------
# ✅ MUST BE FIRST Streamlit call
# -----------------------------
st.set_page_config(page_title="91 Care IPD Helpdesk", page_icon="🏥")

# -----------------------------
# Background & Button Styles
# -----------------------------
def get_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return None

img = get_base64("bg.jpeg")

if img:
    st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)),
                    url("data:image/jpeg;base64,{img}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """, unsafe_allow_html=True)



st.markdown("""
<style>
div.stButton > button {
    background-color: #f0f2f6;
    color: black;
    border-radius: 8px;
    height: 45px;
}
div.stButton > button:hover {
    background-color: #007bFF;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# Session State
# -----------------------------
if "step" not in st.session_state:
    st.session_state.step = "greeting"

if "role" not in st.session_state:
    st.session_state.role = None


# -----------------------------
# Reusable Back Button
# -----------------------------
def back_to_main():
    if st.button("⬅ Back"):
        st.session_state.step = "main"


# -----------------------------
# Greeting Section
# -----------------------------
def greeting():
    st.subheader("Welcome to 91 Care IPD Helpdesk")
    st.write("**Your Role please:**")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("👨‍⚕️ Doctor"):
            st.session_state.role = "Doctor"
            st.session_state.step = "main"

    with col2:
        if st.button("👩‍⚕️ Nurse"):
            st.session_state.role = "Nurse"
            st.session_state.step = "main"

    with col3:
        if st.button("🧑‍💼 Receptionist"):
            st.session_state.role = "Receptionist"
            st.session_state.step = "main"

    with col4:
        if st.button("🧑‍💼 Admin"):
            st.session_state.role = "Admin"
            st.session_state.step = "main"


# -----------------------------
# Role-Based Main Menu
# -----------------------------
def main_menu():
    role = st.session_state.role

    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("🔙"):
            st.session_state.role = None
            st.session_state.step = "greeting"

    st.subheader(f"Hello {role}, How can I help you?")

    buttons = []

    if role == "Doctor":
        buttons = [
            ("🎟️ Book OT", "OT"),
            ("🧾 Prescription", "Prescription"),
            ("📝 Assign Doctor", "assign_doctor"),
            ("🔄 Transfer Patient", "Transfer"),
            
        ]

    elif role == "Admin":
        buttons = [
            ("🎟️ Book OT", "OT"),
            ("🛏️ Admit Patient", "Admit"),
            ("🔄 Reschedule OT", "Reschedule"),
            ("📋 Registration Form", "Registration_form"),
            ("📁 Upload Files", "Upload"),
            ("📝 Assign Doctor", "assign_doctor"),
            ("🔄 Transfer Patient", "Transfer"),
            ("❌ Cancel Appointment", "cancel_appointment"),
            ("🏠 Discharge Patient", "Discharge"),
            ("📁 Consent Form", "consent_form"),
            ("📅 Schedule Consultation", "schedule_consultation"),
            ("🪪 Visitor ID", "visitor_id"),
            ("➕ Add Service", "Add_service"),
            ("🧾 Billing History", "billing_history"),
            ("📜 Download Invoice", "Download_invoice"),
            ("💳 Pay Final Bill", "Pay_Bill"),
            ("👁️ View Certificate", "View_certificate"),
            ("♻️ Old Patient Linking", "old_patient_linking"),
            ("⬆️ Update Admission", "Update_Admission"),
            ("👩 Nurse Notes", "Nurse_notes"),
            ("💊 Prescription", "Prescription"),
        ]

    elif role == "Nurse":
        buttons = [
        
            ("🛏️ Admit Patient", "Admit"),
            ("🔄 Reschedule OT", "Reschedule"),
            ("📋 Registration Form", "Registration_form"),
            ("📁 Upload Files", "Upload"),
            ("📝 Assign Doctor", "assign_doctor"),
            ("🔄 Transfer Patient", "Transfer"),
            ("❌ Cancel Appointment", "cancel_appointment"),
            ("📁 Consent Form", "consent_form"),
            ("📅 Schedule Consultation", "schedule_consultation"),
            ("🪪 Visitor ID", "visitor_id"),
            ("🧾 Billing History", "billing_history"),
            ("📜 Download Invoice", "Download_invoice"),
            ("👁️ View Certificate", "View_certificate"),
            ("♻️ Old Patient Linking", "old_patient_linking"),
            ("⬆️ Update Admission", "Update_Admission"),
            ("👩 Nurse Notes", "Nurse_notes"),
            
        ]
    elif role == "Receptionist":
        buttons = [
            
            ("🛏️ Admit Patient", "Admit"),
            ("🔄 Reschedule OT", "Reschedule"),
            ("📋 Registration Form", "Registration_form"),
            ("📁 Upload Files", "Upload"),           
            ("🔄 Transfer Patient", "Transfer"),
            ("❌ Cancel Appointment", "cancel_appointment"),
            ("🏠 Discharge Patient", "Discharge"),
            ("📁 Consent Form", "consent_form"),
            ("📅 Schedule Consultation", "schedule_consultation"),
            ("🪪 Visitor ID", "visitor_id"),
            ("➕ Add Service", "Add_service"),
            ("🧾 Billing History", "billing_history"),
            ("📜 Download Invoice", "Download_invoice"),
            ("💳 Pay Final Bill", "Pay_Bill"),
            ("👁️ View Certificate", "View_certificate"),
            ("♻️ Old Patient Linking", "old_patient_linking"),
            ("⬆️ Update Admission", "Update_Admission"),
        ]

    cols_per_row = 4
    if buttons:
        for i in range(0, len(buttons), cols_per_row):
            cols = st.columns(cols_per_row)
            for j in range(cols_per_row):
                if i + j < len(buttons):
                    label, step = buttons[i + j]
                    with cols[j]:
                        if st.button(label, key=f"{role}_{i}_{j}", use_container_width=True):
                            st.session_state.step = step


# -----------------------------
# Logo Header (safe — after set_page_config)
# -----------------------------
col1, col2, col3 = st.columns([2, 3, 2])
with col2:
    colA, colB = st.columns([1, 3])
    with colA:
        try:
            st.image("loginlogo.jpg", width=70)
        except Exception:
            st.markdown("🏥")
    with colB:
        st.markdown("<h2 style='margin-top:15px;'>91 Care</h2>", unsafe_allow_html=True)


# -----------------------------
# Feature Pages
# -----------------------------

def OT():
    st.markdown("""
### 🎟️ OT Booking Instructions
🔹 Go to the **OT Page**  
🔹 Click on **Book OT** (top right corner)  
🔹 Fill in the required details  
🔹 Submit the form to book the OT  
""")
    back_to_main()


def Admit():
    st.markdown("""
### 🛏️ Admit Patient Instructions
🔹 Go to the **Home Page**  
🔹 Click on **Admit Patient** (top right corner)  
🔹 Fill in the required details  
🔹 Submit the form to admit the patient  
""")
    back_to_main()


def Reschedule():
    st.markdown("""
### 🧾 OT Reschedule Instructions
🔹 Go to the **OT Page**  
🔹 View the list of all OT bookings  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Reschedule**  
🔹 Choose the new **date and time**  
🔹 Submit the form to reschedule the OT booking  
""")
    back_to_main()


def Registration_form():
    st.markdown("""
### 🏠 Patient Registration Form Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 At the end of each patient row, click on the **📄 File icon**  
🔹 The registration form will open  
🔹 View or verify the patient details  
""")
    back_to_main()


def  Prescription():
    st.markdown("""
### 💊 Prescription View Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Prescription**  
🔹 The prescription details will open in a new page  
""")
    back_to_main()


def Upload():
    st.markdown("""
### 📁 File Upload Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Files**  
🔹 Choose the file to upload  
🔹 Submit the form to upload the file  
""")
    back_to_main()


def Assign_Doctor():
    st.markdown("""
### 📝 Assign Doctor Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Assign Doctor**  
🔹 Choose the doctor to assign  
🔹 Submit the form to assign the doctor  
""")
    back_to_main()


def Transfer():
    st.markdown("""
### 🔄 Transfer Patient Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Transfer**  
🔹 Choose the new department or ward  
🔹 Submit the form to transfer the patient  
""")
    back_to_main()


def cancel_appointment():
    st.markdown("""
### ❌ Cancel Appointment Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Cancel Appointment**  
🔹 Confirm the cancellation  
""")
    back_to_main()


def Discharge():
    st.markdown("""
### 🏠 Discharge Patient Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Discharge**  
🔹 Submit the form to discharge the patient  
""")
    back_to_main()


def consent_form():
    st.markdown("""
### 📁 Consent Form Upload Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Upload Consent Form**  
🔹 Choose the consent form to upload  
🔹 Submit the form to upload the consent form  
""")
    back_to_main()




def schedule_consultation():
    st.markdown("""
### 📅 Schedule Consultation Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Schedule Consultation**  
🔹 Choose the date and time for the consultation  
🔹 Submit the form to schedule the consultation  
""")
    back_to_main()


def visitor_id():
    st.markdown("""
### 🪪 Visitor ID Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Visitor ID**  
🔹 View, download, or print the Visitor ID  
""")
    back_to_main()


def Add_service():
    st.markdown("""
### ➕ Add Service Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Billing History** → then **Add Service**  
🔹 Choose the service to add  
🔹 Submit the form to add the service  
""")
    back_to_main()


def billing_history():
    st.markdown("""
### 🧾 Billing History Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Billing History**  
🔹 View the billing history of the patient  
""")
    back_to_main()


def Download_invoice():
    st.markdown("""
### 📜 Download Invoice Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Final Billing**  
🔹 Click on the **Invoice** button to download   
""")
    back_to_main()


def Pay_Bill(): 
    st.markdown("""
### 💳 Pay Bill Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Final Billing**  
🔹 Click on the **Pay Bill** button to proceed with payment  
""")
    back_to_main()


def View_certificate():
    st.markdown("""
### 👁️ View Certificate Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **View Certificate**  
🔹 The certificate will open in a new page  
""")
    back_to_main()




def old_patient_linking():
    st.markdown("""
### ♻️ Old Patient Linking Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Old Patient Linking**  
🔹 Verify the **ABHA ID**  
🔹 Submit the form to link the old patient record  
""")
    back_to_main()



def Update_Admission():
    st.markdown("""
### ⬆️ Update Admission Instructions
🔹 Go to the **Home Page**  
🔹 View the list of all patients  
🔹 Click on **⋮** at the end of the row  
🔹 Select **Update Admission**  
🔹 Update the required details and submit  
""")
    back_to_main()



def Nurse_notes():
    st.markdown("""
### 👩‍⚕️ Nurse Notes Instructions
🔹 Go to the **Home Page**  
🔹 View the list of patients  
🔹 Identify patients in **Admitted Status**  
🔹 Click on **⋮ (three vertical dots)** at the end of the row  
🔹 Select **Nurse Notes**  
🔹 Fill in the required details  
🔹 Click **Submit** to save the nurse notes  
""")
    back_to_main()


# -----------------------------
# Navigation Controller
# -----------------------------
step = st.session_state.step

if step == "greeting":
    greeting()
elif step == "main":
    main_menu()
elif step == "OT":
    OT()
elif step == "Admit":
    Admit()
elif step == "Reschedule":
    Reschedule()

elif step == "Registration_form":
    Registration_form()
elif step == "Prescription":
    Prescription()
elif step == "Upload":
    Upload()
elif step == "assign_doctor":
    Assign_Doctor()
elif step == "Transfer":
    Transfer()
elif step == "cancel_appointment":
    cancel_appointment()
elif step == "Discharge":
    Discharge()
elif step == "consent_form":
    consent_form()
elif step == "schedule_consultation":
    schedule_consultation()
elif step == "visitor_id":
    visitor_id()
elif step == "Add_service":
    Add_service()
elif step == "billing_history":
    billing_history()
elif step == "Download_invoice":
    Download_invoice()
elif step == "Pay_Bill":
    Pay_Bill()
elif step == "View_certificate":
    View_certificate()
elif step == "old_patient_linking":
    old_patient_linking()
elif step == "Update_Admission":
    Update_Admission()
elif step == "Nurse_notes":
    Nurse_notes()