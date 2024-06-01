from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def after_migrate():
    fields = {
        "Sales Invoice": [
            {
                "fieldname": "invoice_barcode",
                "label": "Invoice Barcode",
                "fieldtype": "Attach Image",
                "hidden": 1,
                "insert_after":"title"
            }
        ]
    }
    create_custom_fields(fields)
