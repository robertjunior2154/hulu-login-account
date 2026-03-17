project = 'hulu-login-account'
author = 'hulu-login-account'
release = '1.0'

extensions = []
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']   

html_js_files = [
    'chatbot.js',
]
html_favicon = '_static/favicon.png'
# Google & Bing Verification Meta Tags
html_context = {
    "meta_tags": """
    <meta name="google-site-verification" content="Cva8KgvW-eQpRtsdf8vIcSb023IJtLJfC8PxJAlQ0mc" />
    <meta name="msvalidate.01" content="739245F5D54BCBF40AC056DC0CBF5710" />
    """
}
