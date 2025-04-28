import streamlit as st
import pandas as pd
from pathlib import Path

def load_data():
    """Load password reset logs from CSV with error handling"""
    try:
        file_path = Path(__file__).parent / "password_reset_logs.csv"
        return pd.read_csv(file_path, 
                         names=["timestamp", "email", "temp_password"])
    except FileNotFoundError:
        return pd.DataFrame(columns=["timestamp", "email", "temp_password"])

def main():
    st.title("🔐 IT Helpdesk Analytics Dashboard")
    data = load_data()
    
    if not data.empty:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Resets", len(data))
        with col2:
            st.metric("Last Reset", data.iloc[-1]["timestamp"][:10])
        
        st.subheader("Recent Activity")
        st.dataframe(data.tail(5))  # Fixed line
    else:
        st.warning("No password reset data yet", icon="⚠️")

if __name__ == "__main__":
    main()