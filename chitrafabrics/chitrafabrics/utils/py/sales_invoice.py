import frappe
from frappe.model.naming import parse_naming_series, make_autoname, revert_series_if_last

def sales_invoice(price_list , branch , item):
    rate = frappe.db.get_value("Item Price" , { "item_code" : item , "custom_branch" : Branch , "price_list" : price_list}  ,  "price_list_rate")
    return rate

def sales_invoice_naming(self, event):
    if self.branch and not self.is_return:
        if self.branch == "Warehouse 1":
            self.name = make_autoname("CKW-2425-.#####")
        if self.branch == "Kalachar Outlet":
            self.name = make_autoname("CFS1-2425-.#####")
        if self.branch == "Kalachar Texvalley":
            self.name = make_autoname("TEX-2425-.#####")
        if self.branch == "Kalachar Sathy":
            self.name = make_autoname("CKS-2425-.#####")

def sales_invoice_naming_deletion(self, event):
    if self.branch and not self.is_return:
        if self.branch == "Warehouse 1":
            revert_series_if_last("CKW-2425-.#####", self.name)
        if self.branch == "Kalachar Outlet":
            revert_series_if_last("CFS1-2425-.#####", self.name)
        if self.branch == "Kalachar Texvalley":
            revert_series_if_last("TEX-2425-.#####", self.name)
        if self.branch == "Kalachar Sathy":
            revert_series_if_last("CKS-2425-.#####", self.name)

@frappe.whitelist()
def set_rate(batch_name):
    batch_no = frappe.get_doc("Batch",batch_name)
    if batch_no.custom_item_discount_rate:
        return batch_no.custom_item_discount_rate
    else:
        return batch_no.custom_item_price
        