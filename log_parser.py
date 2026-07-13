def analyze_logs(log_text):
    lines = log_text.splitlines()

    info = 0
    warning = 0
    error = 0
    critical = 0

    entries = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        parts = line.split(" ", 3)

        if len(parts) == 4:
            date = parts[0]
            time = parts[1]
            level = parts[2].upper()
            message = parts[3]

            entry = {
                "Timestamp": f"{date} {time}",
                "Level": level,
                "Message": message,
            }

            entries.append(entry)

            if level == "CRITICAL":
                critical += 1
            elif level == "ERROR":
                error += 1
            elif level == "WARNING":
                warning += 1
            elif level == "INFO":
                info += 1

    root_cause = []

    for entry in entries:
        if entry["Level"] in ["ERROR", "CRITICAL"]:
            root_cause.append(entry)

    return {
        "Total Logs": len(entries),
        "INFO": info,
        "WARNING": warning,
        "ERROR": error,
        "CRITICAL": critical,
        "Entries": entries,
        "Root Cause": root_cause,
    }