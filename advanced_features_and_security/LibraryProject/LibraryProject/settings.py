# settings.py (relevant security additions/updates)

import os
from django.core.exceptions import ImproperlyConfigured

def env_bool(name, default=False):
    return os.getenv(name, str(default)).lower() in ("1", "true", "yes")

# ----- Basic production toggles -----
DEBUG = env_bool("DJANGO_DEBUG", False)  # Always False in production
if DEBUG:
    # In dev you might allow localhost
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
else:
    # Replace with your real hostnames (example below)
    ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "example.com").split(",")

# ----- HTTPS / cookies / HSTS -----
# Redirect HTTP to HTTPS (set True in production behind TLS)
SECURE_SSL_REDIRECT = env_bool("SECURE_SSL_REDIRECT", True)

# Ensure cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = env_bool("SESSION_COOKIE_SECURE", True)
CSRF_COOKIE_SECURE = env_bool("CSRF_COOKIE_SECURE", True)

# Prevent browser from guessing content types — reduces MIME sniffing attacks
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable XSS protection header
SECURE_BROWSER_XSS_FILTER = True

# Prevent clickjacking
X_FRAME_OPTIONS = "DENY"  # or "SAMEORIGIN" if you need frames in same site

# HSTS — instruct browsers to use HTTPS. Only enable in production after HTTPS is working.
SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", 31536000))  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# ----- CSRF settings -----
# Uses the secure cookie above; also ensure CSRF_TRUSTED_ORIGINS if your host uses custom domain or proxy.
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "https://example.com").split(",")

# ----- Content Security Policy options (if using django-csp) -----
# If you install django-csp, add 'csp' to INSTALLED_APPS and 'csp.middleware.CSPMiddleware' near top of MIDDLEWARE.
# Example shown in CSP section below.
