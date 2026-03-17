import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def sanitize(data):
    """Mask sensitive fields"""
    if isinstance(data, list):
        return [sanitize(item) for item in data]

    if not isinstance(data, dict):
        return data

    SENSITIVE_KEYS = ["name", "email", "account", "phone", "id"]

    sanitized = {}
    for k, v in data.items():
        if any(s in k.lower() for s in SENSITIVE_KEYS):
            sanitized[k] = "XXX"
        else:
            sanitized[k] = sanitize(v)
    return sanitized


def ai_analyze_response(response_json):
    safe_data = sanitize(response_json)

    prompt = f"""
Check this API response:
- Missing fields
- Null or empty values
- Structure issues
- Anything suspicious

Response:
{safe_data}
"""

    try:
        result = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return result.choices[0].message.content

    except Exception as e:
        return f"AI error: {e}"