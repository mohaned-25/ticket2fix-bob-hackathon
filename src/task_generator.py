def generate_developer_task(ticket_text, ticket_analysis, repo_analysis):
    return f"""
# Developer Task

## Problem

Users are experiencing the following issue:

> {ticket_text}

The issue needs to be converted from a support report into a clear engineering task.

## Likely Cause

The problem may be caused by one or more of the following:

- The backend updates the password but does not return the correct response.
- The login endpoint does not correctly validate the new password.
- The frontend reloads the page before displaying an error message.
- The authentication session or token is not created correctly.
- Error responses are not handled properly in the login form.

## Files to Inspect

- `backend/auth.service.js`
- `backend/passwordReset.controller.js`
- `backend/routes/auth.routes.js`
- `frontend/LoginForm.tsx`
- `frontend/ResetPassword.tsx`
- `frontend/api/authClient.ts`

## Debugging Checklist

- Confirm that the password reset endpoint returns a successful response.
- Verify that the new password is saved correctly in the database.
- Check whether the password is hashed before saving.
- Confirm that the login endpoint accepts the new password.
- Inspect browser network requests after login submission.
- Check whether the frontend receives an error response.
- Verify that error messages are displayed correctly.
- Check token or session generation after successful login.

## Acceptance Criteria

- User can reset password successfully.
- User can log in using the new password.
- User cannot log in using the old password.
- Failed login attempts show a clear error message.
- Backend returns meaningful HTTP status codes.
- Frontend does not silently reload without feedback.
- Unit or integration tests are added for the password reset and login flow.

## Developer Notes

This task was generated from the support ticket using Ticket2Fix. IBM Bob should be used to inspect the repository context, confirm the affected files, and assist with implementation planning.
"""