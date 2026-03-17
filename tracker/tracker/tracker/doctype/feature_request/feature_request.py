# Copyright (c) 2026, FRAPPE_DEV and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FeatureRequest(Document):
    def validate(self):
        # Description check karega
        if self.status == "Approved" and not self.description:
            frappe.throw("Bhai, Description bharna zaroori hai!")

    def on_update(self):
        if self.status == "Approved":
            # Check karega task pehle se hai ya nahi
            exists = frappe.db.exists("Development Task", {"feature_request_ref": self.name})
            
            if not exists:
                new_task = frappe.get_doc({
                    "doctype": "Development Task",
                    "task_name": self.title,
                    "feature_request_ref": self.name,
                    "task_priority": self.priority,
                    "task_status": "Open"
                })
                new_task.insert()
                frappe.msgprint(f"Bhai, Task automatically ban gaya!")
