# Frappe Task Automation App

This app automatically creates a **Development Task** whenever a **Feature Request** is set to "Approved".

### Key Features:
- **Custom DocTypes:** Created 'Feature Request' and 'Development Task'.
- **Automated Logic:** Used Python hooks (`on_update`) to trigger task creation.
- **Validation:** Added checks to ensure descriptions are provided before approval.

### How to Install:
1. Copy the `tracker` folder to your `frappe-bench/apps/` directory.
2. Run `bench get-app tracker`.
3. Run `bench --site [your-site] install-app tracker`.
4. Run `bench migrate`.
