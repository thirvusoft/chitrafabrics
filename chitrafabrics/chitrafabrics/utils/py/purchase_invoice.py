import frappe
def last_rate(doc, event):
    for i in doc.items:
        last_rate = frappe.db.get_value('Purchase Invoice Item', {
            'item_code': i.item_code,
            'docstatus': 1  # Consider only submitted documents
        }, 'rate', {
            'order_by': 'creation',
            'limit': 1,
            'order': 'desc'
        })
        if last_rate != i.rate:
            item = frappe.get_doc("Item" , i.item_code)
            for j in item.custom_price_list_table:
                price_list = frappe.get_all("Item Price", filters={"price_list": j.price_list, "item_code": i.item_code})

                if price_list:
                    frappe.set_value("Item Price" , price_list[0] , "price_list_rate" , float(i.rate) * (1 + float(j.percentage) / 100))
                    frappe.db.commit()
                    frappe.errprint(i.rate)
                else : 
                    pr = frappe.new_doc("Item Price")
                    pr.item_code = i.item_code
                    pr.price_list = j.price_list
                    pr.selling = 1
                    pr.price_list_rate = float(i.rate) * (1 + float(j.percentage) / 100)
                    pr.save()


def new_rate(doc, event):
    if doc.valuation_rate:
        for j in doc.custom_price_list_table:
                price_list = frappe.get_all("Item Price", filters={"price_list": j.price_list, "item_code": doc.item_code})

                if price_list:
                    frappe.set_value("Item Price" , price_list[0] , "price_list_rate" , float(doc.valuation_rate) * (1 + float(j.percentage) / 100))
                    frappe.db.commit()
                    frappe.errprint(doc.valuation_rate)

                else : 
                    pr = frappe.new_doc("Item Price")
                    pr.item_code = doc.item_code
                    pr.price_list = j.price_list
                    pr.selling = 1
                    pr.price_list_rate = float(doc.valuation_rate) * (1 + float(j.percentage) / 100)
                    pr.save()