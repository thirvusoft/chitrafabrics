import frappe
import os
from frappe.model.naming import parse_naming_series, make_autoname, revert_series_if_last
from barcode import Code128

def validate(doc, event=None):
    generate_bar_code(doc)

def generate_bar_code(doc):
    if frappe.db.exists("File", {
        "attached_to_doctype": "Sales Invoice",
        "attached_to_name": doc.name,
        "attached_to_field":'invoice_barcode',
    }):
        frappe.errprint("Return")
        return
    _file = frappe.new_doc("File")
    _file.update({
            "file_name": f"{doc.name}.svg",
            "content":doc.name,
            "attached_to_doctype": "Sales Invoice",
            "attached_to_name": doc.name,
            "attached_to_field":'invoice_barcode',
    })
    _file.save()

    file_path = os.path.join(frappe.get_site_path("public", "files"), _file.file_name)

    with open(file_path, "wb") as f:
        f.write(Code128(doc.name).render())
    doc.invoice_barcode = _file.file_url

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
    
    delete_merge_log_pos(self)

def before_cancel(self, event):
    unlink_serial_batch_bundle(self)

    cancel_merge_log_pos(self)

def cancel_merge_log_pos(self):

    if self.is_pos and not self.amended_from and frappe.db.exists("POS Invoice", {"consolidated_invoice": self.name}):
        pos_invoice_doc = frappe.get_doc("POS Invoice", {"consolidated_invoice": self.name})
        merge_log_name = frappe.get_value("POS Invoice Reference", {"pos_invoice": pos_invoice_doc.name}, "parent")
        merge_log_doc = frappe.get_doc("POS Invoice Merge Log", merge_log_name)
        merge_log_doc.cancel()
        pos_invoice_doc.reload()
        pos_invoice_doc.cancel()

def unlink_serial_batch_bundle(self):
    if self.is_pos and not self.amended_from:
        if frappe.db.exists("POS Invoice", {"consolidated_invoice": self.name}):
            # pos_invoice_doc = frappe.get_doc("POS Invoice", {"consolidated_invoice": self.name})
            for row in self.items:
                if row.serial_and_batch_bundle:
                    frappe.db.set_value(
                        "Serial and Batch Bundle", row.serial_and_batch_bundle, {"is_cancelled": 1}
                    )
                    row.db_set("serial_and_batch_bundle", None)


def delete_merge_log_pos(self):

    if self.is_pos and not self.amended_from:
        
        if frappe.db.exists("POS Invoice Merge Log", {"consolidated_invoice": self.name}):

            merge_log_doc = frappe.get_doc("POS Invoice Merge Log", {"consolidated_invoice": self.name})
            pos_invoices = merge_log_doc.pos_invoices
            frappe.delete_doc(merge_log_doc.doctype, merge_log_doc.name)
            
            for i in pos_invoices:
                frappe.delete_doc('POS Invoice', i.pos_invoice)


@frappe.whitelist()
def set_rate(batch_name):
    batch_no = frappe.get_doc("Batch",batch_name)
    if batch_no.custom_item_discount_rate:
        return batch_no.custom_item_discount_rate
    else:
        return batch_no.custom_item_price
        
