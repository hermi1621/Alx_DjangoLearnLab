DEBUG = False  # Always False in production

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Optionally force HTTPS by uncommenting when you have HTTPS configured
# SECURE_SSL_REDIRECT = True

# Content Security Policy (CSP) middleware setup (Step 4)
MIDDLEWARE = [
    # ... existing middleware ...
    'csp.middleware.CSPMiddleware',  # add this line for CSP
]

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'",)
