BANNED_PHRASES = [
    "guaranteed returns",
    "risk-free",
    "100% safe"
]

class ComplianceError(Exception):
    pass

def validate_response(response: str):
    response_lower = response.lower()
    for phrase in BANNED_PHRASES:
        if phrase in response_lower:
            raise ComplianceError(f"Response contains banned phrase: '{phrase}'")
    return response
