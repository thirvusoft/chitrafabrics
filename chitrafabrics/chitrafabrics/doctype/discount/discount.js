frappe.ui.form.on("Discount", {
    get_batch(frm) {
        frappe.call({
            method: "chitrafabrics.chitrafabrics.utils.py.discount.discount",
            args: {
                doc: frm.doc
            },
            callback: function(response) {
                if (response.message) {
                    const batch_names = response.message;  
                    frm.clear_table("discount_table");  
                    batch_names.forEach(batch_name => {
                        let row = frm.add_child("discount_table");  
                        row.batch = batch_name;  
                        row.discount_percentage =  frm.doc.percentage
                    });
                    frm.refresh_field("discount_table");  
                }
            }
        });
    }
});
