import frappe

def fetchdata(doc , events):
    if(doc.stock_entry_type == "Opening Entry"):
        doc.is_opening = "Yes"
        for i in doc.items:
            i.expense_account = "Temporary Opening - CF"
            i.branch = doc.branch
        frappe.msgprint("Difference Account set to Temporary Opening - CF")
   



