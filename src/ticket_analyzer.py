def estimate_severity(ticket_text):
    text = ticket_text.lower()

    high_keywords = [
        "cannot log in", "can't log in", "login failed", "payment",
        "crash", "data loss", "security", "password", "account locked"
    ]

    medium_keywords = [
        "error", "not working", "failed", "slow", "reload",
        "blank page", "missing", "incorrect"
    ]

    for word in high_keywords:
        if word in text:
            return "High"

    for word in medium_keywords:
        if word in text:
            return "Medium"

    return "Low"


def analyze_ticket(ticket_text):
    severity = estimate_severity(ticket_text)

    return f"""
## Clean Bug Summary

A user reported the following issue:

> {ticket_text}

The issue appears to affect an important user workflow and should be investigated by the development team.

## Severity Estimation

**{severity}**

## Missing Information

- Browser and device used by the user
- User account type or role
- Time the issue occurred
- Backend error logs
- HTTP response status code
- Whether the issue affects one user or multiple users
- Screenshot or screen recording of the issue
- Whether the password reset was completed successfully

## Reproduction Steps

1. Open the application login page.
2. Click **Forgot Password**.
3. Complete the password reset process.
4. Return to the login page.
5. Enter the new password.
6. Submit the login form.
7. Observe whether the user is logged in or whether the page reloads.

## Expected Behavior

The user should be able to log in successfully after resetting the password.

## Actual Behavior

The page reloads, but the user is not logged in and no clear error message is displayed.
"""