frappe.ui.form.on('Sales Invoice', {
    branch(frm){
        if (frm.doc.branch) {
            frm.set_value("set_warehouse" , frm.doc.branch + " - CF" )
        }
        
    },

});
frappe.ui.form.on('Sales Invoice Item', {
    batch_no(frm,cdt,cdn){
        let row = locals[cdt][cdn]
        if (row.batch_no) {
            frappe.call({
                method: "chitrafabrics.chitrafabrics.utils.py.sales_invoice.set_rate",
                args: {
                    batch_name: row.batch_no
                },
                callback: function(response) {
                    if (response.message) {
                        frappe.model.set_value(cdt,cdn,"rate",response.message)
                    }
                }
            });
        }
        
    },

});