#Shivika Rajvanshi XF
import re
import streamlit as st

st.title("🔒 Password Strength Checker")

# Select analysis view mode
mode = st.radio("Select View", ["Standard Analysis", "Detailed Metrics"])

st.divider()

password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Type a test password here...",
)

if password:
    # Evaluate individual security criteria
    has_length = len(password) >= 8
    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_lowercase = bool(re.search(r"[a-z]", password))
    has_number = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Criteria map for checklist and scoring
    criteria = {
        "Minimum 8 characters": has_length,
        "At least one uppercase letter (A-Z)": has_uppercase,
        "At least one lowercase letter (a-z)": has_lowercase,
        "At least one digit (0-9)": has_number,
        "At least one special character (!@#$%...)": has_special,
    }

    # Calculate overall score out of 5
    score = sum(criteria.values())

    # Determine strength level and visual status
    if score <= 2:
        strength = "Weak"
        st.error(f"**Password Strength:** {strength} ({score}/5 criteria met)")
    elif score in (3, 4):
        strength = "Moderate"
        st.warning(f"**Password Strength:** {strength} ({score}/5 criteria met)")
    else:
        strength = "Strong"
        st.success(f"**Password Strength:** {strength} ({score}/5 criteria met)")

    # Visual strength progress bar
    st.progress(score / 5.0)

    st.divider()

    if mode == "Standard Analysis":
        # Criteria Checklist View
        st.subheader("📋 Criteria Checklist")
        for desc, passed in criteria.items():
            if passed:
                st.markdown(f"✅ **{desc}**")
            else:
                st.markdown(f"❌ {desc}")

        # Improvement suggestions
        missing = [desc for desc, passed in criteria.items() if not passed]
        if missing:
            st.divider()
            st.subheader("💡 Suggestions to Improve")
            for desc in missing:
                st.write(f"- Add: {desc.lower()}")

    else:  # Detailed Metrics Mode
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Total Character Count", value=len(password))
            st.metric(label="Criteria Passed", value=f"{score} / 5")
        with col2:
            st.metric(label="Strength Rating", value=strength)
            st.metric(
                label="Security Score", value=f"{int((score / 5.0) * 100)}%"
            )

        st.divider()
        st.subheader("Detailed Requirements Breakdown")
        for desc, passed in criteria.items():
            status_text = "PASS" if passed else "FAIL"
            st.text(f"[{status_text}] {desc}")

else:
    st.info("Please enter a password above to evaluate its strength.")
