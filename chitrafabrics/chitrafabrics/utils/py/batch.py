import frappe
from frappe.model.naming import parse_naming_series, make_autoname, revert_series_if_last

def batch_id_naming(doc, action):
    if doc.item:
        doc.name = make_autoname(f"{doc.item}-B.#")
        doc.batch_id = doc.name

def batch_id_trash(doc, action):
    if doc.item:
        revert_series_if_last(f"{doc.item}-B.#", doc.name)