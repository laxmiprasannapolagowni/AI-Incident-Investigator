import pandas as pd
import streamlit as st

from ai_analyzer import analyze_with_gemini
from log_parser import analyze_logs
from report_generator import generate_incident_report


st.set_page_config(
    page_title="AI Incident Investigator",
    page_icon="🚨",
    layout="wide",
)

st.title("🚨 AI Incident Investigator")

st.write(
    """
    Upload a software log file to detect errors, warnings,
    incidents, possible root causes, and recommended fixes.
    """
)

uploaded_file = st.file_uploader(
    "Upload a log file",
    type=["log", "txt"],
)

if uploaded_file is not None:
    log_content = uploaded_file.read().decode(
        "utf-8",
        errors="ignore",
    )

    results = analyze_logs(log_content)

    if results["CRITICAL"] > 0:
        severity = "🔴 Critical"
    elif results["ERROR"] >= 3:
        severity = "🟠 High"
    elif results["WARNING"] >= 3:
        severity = "🟡 Medium"
    else:
        severity = "🟢 Low"

    st.success("Log file uploaded successfully!")

    st.subheader("Uploaded File Details")

    st.write("**File name:**", uploaded_file.name)

    st.write(
        "**File size:**",
        f"{uploaded_file.size} bytes",
    )

    st.subheader("Log Preview")

    st.code(
        log_content[:5000],
        language="text",
    )

    st.subheader("🚨 Incident Severity")

    if severity == "🔴 Critical":
        st.error(severity)
    elif severity in ["🟠 High", "🟡 Medium"]:
        st.warning(severity)
    else:
        st.success(severity)

    st.subheader("📊 Log Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📄 Total Logs",
            results["Total Logs"],
        )

    with col2:
        st.metric(
            "ℹ️ INFO",
            results["INFO"],
        )

    with col3:
        st.metric(
            "⚠️ WARNING",
            results["WARNING"],
        )

    col4, col5 = st.columns(2)

    with col4:
        st.metric(
            "❌ ERROR",
            results["ERROR"],
        )

    with col5:
        st.metric(
            "🚨 CRITICAL",
            results["CRITICAL"],
        )

    st.subheader("📈 Incident Distribution")

    chart_data = pd.DataFrame(
        {
            "Log Level": [
                "INFO",
                "WARNING",
                "ERROR",
                "CRITICAL",
            ],
            "Count": [
                results["INFO"],
                results["WARNING"],
                results["ERROR"],
                results["CRITICAL"],
            ],
        }
    )

    st.bar_chart(
        chart_data,
        x="Log Level",
        y="Count",
    )

    st.subheader("🔎 Search and Filter Logs")

    timeline_data = pd.DataFrame(
        results["Entries"]
    )

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:
        selected_level = st.selectbox(
            "Filter by log level",
            [
                "ALL",
                "INFO",
                "WARNING",
                "ERROR",
                "CRITICAL",
            ],
        )

    with filter_col2:
        search_text = st.text_input(
            "Search log messages",
            placeholder="Example: database, timeout, HTTP",
        )

    filtered_data = timeline_data.copy()

    if selected_level != "ALL":
        filtered_data = filtered_data[
            filtered_data["Level"] == selected_level
        ]

    if search_text.strip():
        filtered_data = filtered_data[
            filtered_data["Message"].str.contains(
                search_text,
                case=False,
                na=False,
            )
        ]

    st.write(
        f"**Matching log entries:** {len(filtered_data)}"
    )

    if not filtered_data.empty:
        st.dataframe(
            filtered_data,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.warning(
            "No log entries match the selected filters."
        )

    st.subheader("🕒 Complete Incident Timeline")

    if not timeline_data.empty:
        st.dataframe(
            timeline_data,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.warning(
            "No valid timeline entries were found."
        )

    st.subheader("🔍 Possible Root Cause")

    root_cause_data = pd.DataFrame(
        results["Root Cause"]
    )

    if not root_cause_data.empty:
        st.dataframe(
            root_cause_data,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.success(
            "No ERROR or CRITICAL logs were found."
        )

    st.subheader("🤖 AI Incident Analysis")

    if "ai_result" not in st.session_state:
        st.session_state["ai_result"] = ""

    if st.button(
        "Analyze with Gemini",
        type="primary",
    ):
        with st.spinner(
            "Gemini is analyzing the logs..."
        ):
            try:
                st.session_state["ai_result"] = (
                    analyze_with_gemini(log_content)
                )

                st.success(
                    "AI analysis completed successfully!"
                )

            except Exception as error:
                error_message = str(error)

                if (
                    "503" in error_message
                    or "UNAVAILABLE" in error_message
                    or "high demand" in error_message.lower()
                ):
                    st.warning(
                        "Gemini is temporarily busy. "
                        "Please try again later."
                    )
                else:
                    st.error(error_message)

    if st.session_state["ai_result"]:
        st.markdown(
            st.session_state["ai_result"]
        )

    st.subheader("📄 Download Incident Report")

    report_text = generate_incident_report(
        file_name=uploaded_file.name,
        severity=severity,
        results=results,
        ai_analysis=st.session_state["ai_result"],
    )

    st.download_button(
        label="Download Incident Report",
        data=report_text,
        file_name="incident_report.txt",
        mime="text/plain",
        use_container_width=True,
    )

else:
    st.info(
        "Please upload a `.log` or `.txt` file."
    )