import frappe
from frappe.model.naming import parse_naming_series, make_autoname, revert_series_if_last

def item_name(doc, action):
    if not doc.variant_of:
        if doc.custom_gender:
            code=frappe.db.get_value("Gender", doc.custom_gender, "custom_item_code")
            if code:
                doc.name = make_autoname(f"{code}.####")
                doc.item_code = doc.name
            else:
                frappe.throw(f"The Gender Not Have Item Code-{doc.custom_gender}")
        else:
            frappe.throw(f"Must Select Gender")

def item_name_delete(doc, action):
    if not doc.variant_of:
        if doc.custom_gender:
            code=frappe.db.get_value("Gender", doc.custom_gender, "custom_item_code")
            if code:
                revert_series_if_last(f"{code}.####", doc.name)
