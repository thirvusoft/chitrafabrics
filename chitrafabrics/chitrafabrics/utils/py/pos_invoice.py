import frappe
from frappe.utils.data import nowdate, nowtime

def on_submit(self, event):
    new_doc = frappe.new_doc("POS Invoice Merge Log")
    new_doc.posting_date = nowdate()
    new_doc.posting_time = nowtime()
    new_doc.customer = self.customer
    new_doc.update({
        "pos_invoices": [{
            "pos_invoice": self.name,
            "posting_date": self.posting_date
        }]
    })

    new_doc.save()
    new_doc.submit()