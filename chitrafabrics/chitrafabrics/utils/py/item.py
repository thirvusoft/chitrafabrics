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


# def test():
#     frappe.log_error("Process ok")
#     try:
#         ls = frappe.get_all("Item Price", fields=["price_list_rate", "name"])
#         for i in ls:
#             try:
#                 doc = frappe.get_doc("Item Price", i.name)
#                 doc.price_list_rate = round(i.price_list_rate)
#                 doc.save()
#                 doc.reload()
#             except Exception as e:
#                 frappe.log_error(f"Error updating Item Price {i.name}: {str(e)}", "Item Price Update Error")
#     except Exception as e:
#         frappe.log_error(f"Error fetching Item Prices: {str(e)}", "Item Price Fetch Error")