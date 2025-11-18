mCaffeine Shopify Upload Script
================================

Overview
--------
This repository contains a small utility that reads product rows from an Excel
file and creates/updates products on a Shopify store using the Admin GraphQL API.

Files
-----
- `credentials.py` - Configuration values (shop domain, Admin API token, excel filename, API version). Update this file before running.
- `upload_products.py` - Main script that reads the Excel file and applies create/update operations to Shopify.
- `products.xlsx` - (Not included) Example Excel file expected by the script. It should contain columns like `handle`, `title`, `variant_sku`, `variant_price`, and optional image/metafield columns.

Security note
-------------
The repository currently stores the `ADMIN_API_TOKEN` directly in
`credentials.py` for convenience. This is insecure for shared or
production environments. For real deployments, use environment variables
or a secrets manager and do NOT commit tokens to source control.

Requirements
------------
- Python 3.8+
- `pandas` and `requests` Python packages

Quick setup (Windows PowerShell)
--------------------------------
# Create and activate a virtual environment (one-time)
python -m venv .venv
& .\.venv\Scripts\Activate.ps1

# Install packages
pip install pandas requests openpyxl

Running the script
------------------
1. Update `credentials.py` with your Shopify store domain and Admin API token.
2. Place the Excel file (default: `products.xlsx`) next to the script or update the filename in `credentials.py`.
3. Run the script:

python upload_products.py

Excel file expectations
-----------------------
Minimum required columns:
- `handle` (string) — product handle (unique per product)
- `title` (string) — product title
- `variant_sku` (string) — SKU for each variant
- `variant_price` (numeric/string) — price for each variant

Optional columns supported by the script:
- `variant_option1_name` and `variant_option1_value` — to create product options (e.g., "Size")
- `images` — comma-separated image paths or URLs
- `metafield_<namespace>_<key>[_<type>]` — custom metafields to add to each product

Notes & troubleshooting
-----------------------
- If you encounter rate-limiting errors, the script does simple backoff
  pauses but may need to be adjusted for large bulk imports.
- Ensure the Admin API token has the required scopes (products, content/files, inventory, etc.).

If you want, I can also:
- Convert `credentials.py` to read from environment variables.
- Add a sample `products.xlsx` template.
- Add unit tests or safety dry-run mode.




