import frappe

# def last_rate(doc, event):
#     for i in doc.items:
#         last_rate = frappe.db.get_value('Purchase Receipt Item', {
#             'item_code': i.item_code,
#             'docstatus': 1  # Consider only submitted documents
#         }, 'rate', {
#             'order_by': 'creation',
#             'limit': 1,
#             'order': 'desc'
#         })
#         if last_rate != i.rate:
#             item = frappe.get_doc("Item" , i.item_code)
#             for j in item.custom_price_table:
#                 price_list = frappe.get_all("Item Price", filters={"price_list": j.price_list, "item_code": i.item_code , "custom_branch" : j.branch})
#                 frappe.set_value("Item" , i.item_name , "valuation_rate" , float(i.rate) * (1 + float(j.percentage) / 100))
#                 frappe.db.commit()
#                 if price_list:
#                     frappe.set_value("Item Price" , price_list[0] , "price_list_rate" , float(i.rate) * (1 + float(j.percentage) / 100))
#                     frappe.db.commit()
#                     frappe.errprint(i.rate)
#                 else : 
#                     pr = frappe.new_doc("Item Price")
#                     pr.item_code = i.item_code
#                     pr.price_list = j.price_list
#                     pr.selling = 1
#                     pr.custom_branch = j.branch
#                     pr.price_list_rate = float(i.rate) * (1 + float(j.percentage) / 100)
#                     pr.save()


def new_rate(doc, event):
    if doc.valuation_rate and not doc.has_variants:
        for j in doc.custom_price_table:
                price_list = frappe.get_all("Item Price", filters={"price_list": j.price_list, "item_code": doc.item_code , "custom_branch" : j.branch})
                if price_list:
                    frappe.set_value("Item Price" , price_list[0] , "price_list_rate" , round(float(doc.valuation_rate) * (1 + float(j.percentage) / 100) , 0))
                    frappe.db.commit()

                else : 
                    pr = frappe.new_doc("Item Price")
                    pr.item_code = doc.item_code
                    pr.price_list = j.price_list
                    pr.selling = 1
                    pr.custom_branch = j.branch
                    pr.price_list_rate = round (float(doc.valuation_rate) * (1 + float(j.percentage) / 100 ),0)
                    pr.save()        
                    frappe.errprint(round (float(doc.valuation_rate) * (1 + float(j.percentage) / 100)))

                    
def update_item_price():
    item_price_list = frappe.get_all('Item Price',{'custom_updated':0})
    a=len(item_price_list)
    for i in item_price_list:
        print(a)
        a = a - 1
        doc = frappe.get_doc('Item Price',i.name)

        frappe.db.set_value(doc.doctype,doc.name,'price_list_rate',round(doc.price_list_rate,0),update_modified = 0)
        frappe.db.set_value(doc.doctype,doc.name,'custom_updated',1,update_modified = 0)
        frappe.db.commit()
        # print(doc.name)
        # break
        # doc.save()
                        
def update_batch_price():
    item_price_list = frappe.get_all('Batch',{'custom_item_discount_percentage':['is','set'],'custom_item_discount_percentage':['!=',0]})
    a=len(item_price_list)
    for i in item_price_list:
        a = a - 1
        doc = frappe.get_doc('Batch',i.name)
        print(a)

        frappe.db.set_value(doc.doctype,doc.name,'custom_item_discount_rate',int(round(float(doc.custom_item_discount_rate),0)),update_modified = 0)
        # # frappe.db.set_value(doc.doctype,doc.name,'custom_updated',1,update_modified = 0)
        frappe.db.commit()