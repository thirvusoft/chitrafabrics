import frappe
from frappe.model.naming import parse_naming_series, make_autoname, revert_series_if_last

def batch_id_naming(doc, action):
    if doc.item:
        doc.name = make_autoname(f"{doc.item}-A.#")
        doc.batch_id = doc.name

def batch_id_trash(doc, action):
    if doc.item:
        revert_series_if_last(f"{doc.item}-A.#", doc.name)

def price_updation(doc, action):
    if doc.docstatus == 1:
        for entry in doc.entries:
            if entry.batch_no:
                batch=frappe.get_doc("Batch", entry.batch_no)
                if batch.item == doc.item_code and entry.batch_no == batch.name:
                    branch = frappe.db.get_value("Warehouse", entry.warehouse, "custom_branch")
                    item_price = frappe.db.get_list("Item Price", 
                                                         filters={"item_code": doc.item_code, 
                                                                  "custom_branch": branch, 
                                                                  "price_list": "Retail Selling", 
                                                                  "selling": 1}, 
                                                         fields=["price_list_rate"])
                    if item_price:
                            price_list_rate = item_price[0].get("price_list_rate")
                            rounded_price = round(price_list_rate)
                            batch.custom_item_price = rounded_price
                            batch.save()

