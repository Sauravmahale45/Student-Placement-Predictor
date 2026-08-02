import streamlit as st


def contact_page():

    # ====================================
    # HERO SECTION
    # ====================================

    st.markdown("""

    <div class="hero">

    <h1>📞 Contact Developer</h1>

    <h3>

    Get in touch with the developer

    </h3>

    </div>

    """, unsafe_allow_html=True)

    st.write("")

    # ====================================
    # PROFILE CARD
    # ====================================

    col1, col2 = st.columns([1,2])

    with col1:

        st.image(
            "assets/images/logo.png",
            width=180
        )

    with col2:

        st.markdown("""

### 👨‍💻 Developer

**Name :** Saurav

**Role :** Data Scientist | Python Developer

**Project :** Student Placement Prediction

""")

    st.divider()

    # ====================================
    # CONTACT DETAILS
    # ====================================

    st.subheader("📬 Contact Information")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
📧 Email

sauravmahale45@gmail.com
""")

        st.info("""
📱 Phone

+91 8624942956
""")

        st.info("""
📍 Mumbai

India
""")

    with col2:

        st.info("""
🌐 GitHub

https://github.com/Sauavmahale45
""")

        st.info("""
💼 LinkedIn

https://linkedin.com/
""")

        st.info("""
🌍 Portfolio

Coming Soon
""")

    st.divider()

    # ====================================
    # CONTACT FORM
    # ====================================

    st.subheader("✉ Send a Message")

    name = st.text_input("Name")

    email = st.text_input("Email")

    subject = st.text_input("Subject")

    message = st.text_area("Message")

    if st.button(
        "Send Message",
        use_container_width=True
    ):

        if name and email and message:

            st.success(
                "✅ Thank you! Your message has been recorded."
            )

        else:

            st.warning(
                "Please fill all required fields."
            )

    st.divider()

    # ====================================
    # SOCIAL BUTTONS
    # ====================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.link_button(

            "💻 GitHub",

            "https://github.com/Sauravmahale45"

        )

    with col2:

        st.link_button(

            "💼 LinkedIn",

            "https://linkedin.com/"

        )

    with col3:

        st.link_button(

            "🌍 Portfolio",

            "https://google.com"

        )