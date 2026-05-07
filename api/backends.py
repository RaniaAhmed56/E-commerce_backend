"""
Custom authentication backend — يسمح بالدخول بالـ email أو username
"""
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Try email first
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # Fall back to username
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None


# ── Silent JWT Authentication ─────────────────────────
# بيتجاهل الـ token الغلط أو المنتهي بدل ما يرفض الـ request
# ده مهم لأن AllowAny endpoints محتاجة تشتغل حتى لو في token غلط
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class SilentJWTAuthentication(JWTAuthentication):
    """
    Same as JWTAuthentication but returns None instead of raising
    an exception when the token is invalid or expired.
    This lets AllowAny endpoints work even with a stale token in the header.
    """
    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except (InvalidToken, TokenError):
            return None