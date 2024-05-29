frappe.ui.form.on('Sales Invoice', {
    after_submit: function(frm) {
        branch_value=frappe.get_doc("Warehouse",frm.doc.set_warehouse)

        if (frm.doc.set_warehouse) {
        frappe.call({


            method:"frappe.client.set_value",
            args:{
                doctype:"Sales Invoice",
                name:frm.doc.name,
                fieldname:'branch',
                value:branch_value,
            }
        
        })
    }




        // if (frm.doc.branch) {
        //     branch_value=frappe.get_doc("Warehouse",frm.doc.set_warehouse)
        //     frappe.db.set_value('Sales Invoice', frm.doc.name, 'branch', frm.doc.custom_branch)
        //         .then(function() {
        //             frm.reload_doc();
        //         });  
        // }
    },


    branch: function(frm) {
        if (frm.doc.branch) {
            frm.set_value('set_warehouse', frm.doc.branch + ' - CF');
        }
   
    }});


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