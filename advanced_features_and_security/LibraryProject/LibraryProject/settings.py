# SECURITY SETTINGS FOR HTTPS ENFORCEMENT

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
# Instructs browsers to only connect to your site via HTTPS for the next year (31536000 seconds)
SECURE_HSTS_SECONDS = 31536000

# Include all subdomains in HSTS policy
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allows the domain to be included in the browser preload list for HSTS
SECURE_HSTS_PRELOAD = True

# Ensure session cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True

# Ensure CSRF cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True

# Prevent your site from being framed (clickjacking protection)
X_FRAME_OPTIONS = "DENY"

# Prevent MIME type sniffing by browsers
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable the browser's XSS filtering and help prevent cross-site scripting attacks
SECURE_BROWSER_XSS_FILTER = True
