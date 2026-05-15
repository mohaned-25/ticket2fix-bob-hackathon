def generate_test_plan(ticket_text, repo_analysis):
    text = ticket_text.lower()

    if "password" in text or "login" in text or "log in" in text:
        tests = [
            "User can log in after resetting password.",
            "User cannot log in with the old password after reset.",
            "Invalid reset token shows a clear error message.",
            "Expired reset token shows a clear error message.",
            "Empty password field displays validation feedback.",
            "Backend returns correct status code for failed login.",
            "Frontend displays error message when login fails.",
            "Password reset updates the stored password hash.",
            "Successful login creates a valid session or token."
        ]

    elif "payment" in text or "checkout" in text:
        tests = [
            "User can complete checkout with valid payment details.",
            "Invalid card details show a clear error message.",
            "Failed payment does not create a completed order.",
            "Successful payment creates an order record.",
            "Payment gateway timeout is handled correctly.",
            "Duplicate payment attempts are prevented."
        ]

    else:
        tests = [
            "Main reported workflow works successfully.",
            "Invalid input is handled correctly.",
            "Error message is displayed when the operation fails.",
            "Backend returns meaningful status codes.",
            "Frontend does not crash or reload silently.",
            "Relevant edge cases are covered."
        ]

    tests_markdown = "\n".join(
        [f"{index + 1}. {test}" for index, test in enumerate(tests)]
    )

    return f"""
# Suggested Test Plan

{tests_markdown}

## Recommended Test Types

- Unit tests for business logic
- Integration tests for API flow
- Frontend tests for user interaction
- Regression tests to prevent the issue from returning

## IBM Bob Usage

IBM Bob can help generate test scenarios, identify edge cases, and suggest where tests should be added in the repository.
"""