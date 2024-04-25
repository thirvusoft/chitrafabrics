def sales_invoice(price_list , branch , item):
    rate = frappe.db.get_value("Item Price" , { "item_code" : item , "custom_branch" : Branch , "price_list" : price_list ) ,  "price_list_rate"
    return rate



