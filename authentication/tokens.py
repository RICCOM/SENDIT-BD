from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from flask import current_app

serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])


def generate_password_reset_token(email):
    """
    Generate a password reset token for the given email address.
    The token is valid for 1 hour by default.
    """
    return serializer.dumps(
        email,
        salt=current_app.config['SECURITY_PASSWORD_SALT']
    )


def confirm_password_reset_token(token, expiration=3600):
    """
    Confirm the password reset token and extract the email address.
    Raises an exception if the token is invalid or expired.
    """
    try:
        email = serializer.loads(
            token,
            salt=current_app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except (SignatureExpired, BadSignature):
        raise Exception('Invalid or expired token')
    return email
