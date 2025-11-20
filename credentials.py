# --- CONFIGURATION ---
# This file centralizes configuration values used by the upload script.
# Keep credentials and environment-specific values here so the main
# script (`upload_products.py`) can import them from a single place.
# NOTE: Storing tokens directly in source code is convenient for
# local testing but insecure for production or shared repos. Prefer
# using environment variables or a secrets manager for real projects.

# The shop domain for your Shopify store. It may or may not include
# a trailing slash; the main code expects a domain-like string.
CONFIG_SHOP_URL = "ashishkumarsinha22je0186-ism.myshopify.com/"

# The Shopify Admin API token (private app / access token). This token
# allows the script to authenticate to Shopify and perform product/file
# operations. Do NOT share this token publicly.
CONFIG_ADMIN_API_TOKEN = "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"

# The Excel file name (relative to the script working directory) that
# contains product rows to be uploaded/updated. The file should have
# columns like `handle`, `title`, `variant_sku`, `variant_price`, etc.
CONFIG_EXCEL_FILE = "products.xlsx"

# Shopify Admin API version to target (GraphQL endpoint). Update this
# when Shopify deprecates older API versions. Format example: "2025-10".
CONFIG_API_VERSION = "2025-10"