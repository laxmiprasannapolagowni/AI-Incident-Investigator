def generate_incident_report(
    file_name,
    severity,
    results,
    ai_analysis,
):
    report = f"""
AI INCIDENT INVESTIGATION REPORT
================================

File Name:
{file_name}

Incident Severity:
{severity}

Log Statistics:
- Total Logs: {results["Total Logs"]}
- INFO: {results["INFO"]}
- WARNING: {results["WARNING"]}
- ERROR: {results["ERROR"]}
- CRITICAL: {results["CRITICAL"]}

AI Incident Analysis:
---------------------
{ai_analysis if ai_analysis else "AI analysis was not available."}

Disclaimer:
This report is AI-assisted. The suggested root cause is a hypothesis
and should be validated using system metrics, traces, deployment history,
and engineering judgment.
"""

    return report