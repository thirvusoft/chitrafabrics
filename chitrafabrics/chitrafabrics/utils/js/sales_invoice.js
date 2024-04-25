frappe.ui.form.on('Sales Invoice Item', {
    item_code(frm, cdt, cdn) {
        console.log("fffffffffffffffffffffffffff")
        var child_doc = locals[cdt][cdn];

        frappe.call({
            method: "chitrafabrics.chitrafabrics.utils.py.sales_invoice.sales_invoice",
            args: {
             "price_list" : frm.doc.selling_price_list ,
             "branch" : "B1" , 
             "item" : frm.doc.item_code
            },
            callback: function(response) {
                console.log(response.rate)
                frappe.modal.set_value(child_doc.rate , "rr" , response.rate)
            }
        });
    }
});


frappe.ui.form.on('Sales Invoice', {
    refresh(frm){
        console.log("ffffff--------ffffff")
    }

});

