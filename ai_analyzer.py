import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY was not found. Check the .env file."
    )

client = genai.Client(api_key=API_KEY)

WORKING_MODEL = "models/gemini-3.5-flash"


def analyze_with_gemini(log_text: str) -> str:
    if not log_text.strip():
        raise ValueError("The uploaded log file is empty.")

    prompt = f"""
You are a senior Site Reliability Engineer.

Analyze only the software logs provided below.

Return these clearly labelled sections:

1. Incident Summary
2. Most Likely Root Cause
3. Severity
4. Supporting Evidence
5. Recommended Fixes
6. Prevention Steps
7. Important Limitations

Rules:
- Use only the information present in the logs.
- Do not invent facts.
- Clearly state uncertainty.
- Treat the root cause as a hypothesis, not proven fact.

LOGS:

{log_text}
"""

    maximum_attempts = 3
    last_error = None

    for attempt in range(1, maximum_attempts + 1):
        try:
            response = client.models.generate_content(
                model=WORKING_MODEL,
                contents=prompt,
            )

            if not response.text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            return response.text

        except Exception as error:
            last_error = error
            error_message = str(error)

            is_temporary_error = (
                "503" in error_message
                or "UNAVAILABLE" in error_message
                or "high demand" in error_message.lower()
            )

            if is_temporary_error and attempt < maximum_attempts:
                wait_seconds = attempt * 5
                time.sleep(wait_seconds)
                continue

            raise RuntimeError(
                f"Gemini analysis failed after {attempt} attempt(s): "
                f"{error}"
            ) from error

    raise RuntimeError(
        f"Gemini analysis failed: {last_error}"
    )