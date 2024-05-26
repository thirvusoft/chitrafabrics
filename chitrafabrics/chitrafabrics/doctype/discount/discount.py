# Copyright (c) 2024, Thirvusoft and contributors
# For license information, please see license.txt

import frappe
from frappe import _

from frappe.model.document import Document


class Discount(Document):
    def on_submit(doc):
        for i in doc.discount_table:
            batch = frappe.get_doc("Batch" , i.batch)
            batch.custom_item_discount_percentage = i.discount_percentage
            batch.custom_item_discount_rate = batch.custom_item_price - (float(batch.custom_item_price) / 100 )* float(i.discount_percentage) 
            batch.save()
            batch.reload()
            frappe.msgprint("Discount for All Batches Updated Successfully")

@frappe.whitelist()
def discount(doc):
    doc = frappe.parse_json(doc)
    batch_names = []

    percentage = int(doc.get('percentage', 0))
    if percentage <= 0:
        frappe.throw(_("Percentage cannot be 0 or less"))

    for i in doc.get('items', []):
        item_code = i.get('item')
        item = frappe.get_doc("Item", item_code)
        if item.has_variants == 1:
            all_item = frappe.get_all("Item",filters={"variant_of":item_code},pluck="name")
            for  i in all_item:
                batch_names = add_batch(frappe.get_doc("Item", i),batch_names)
        else:
            batch_names = add_batch(item,batch_names)
        
    return batch_names

def add_batch(item,batch_names):

    if item.has_batch_no:
        batches = frappe.get_all("Batch", filters={"item": item.name}, fields=['name'])
        batch_names.extend( [batch['name'] for batch in batches if batch['name'] not in batch_names])
    else:
        frappe.throw(_("{0} has no batch enabled!").format(item.name), _("Validation Error"))

    return batch_names