import frappe
from frappe import _

@frappe.whitelist()
def discount(doc):
    # Parse the incoming doc string into a Python dictionary
    doc = frappe.parse_json(doc)
    batch_names = []

    # Validate the percentage field
    percentage = int(doc.get('percentage', 0))
    if percentage <= 0:
        frappe.throw(_("Percentage cannot be 0 or less"))

    # Iterate over items in the document
    for i in doc.get('items', []):
        item_code = i.get('item')
        item = frappe.get_doc("Item", item_code)

        if item.has_batch_no:
            # Fetch batch names for the item
            batches = frappe.get_all("Batch", filters={"item": item_code}, fields=['name'])
            batch_names.extend([batch['name'] for batch in batches])
        else:
            frappe.throw(_("{0} has no batch enabled!").format(item_code), _("Validation Error"))
    
    # Return the list of batch names
    return batch_names



def set_discount(doc , events):
    for i in doc.discount_table:
        batch = frappe.get_doc("Batch" , i.batch)
        batch.custom_item_discount_percentage = i.discount_percentage
        batch.custom_item_discount_rate = (float(i.rate) / 100 )* float(i.discount_percentage)
        batch.save()
        batch.reload()
        frappe.msgprint("Discount for All Batches Updated Successfully")