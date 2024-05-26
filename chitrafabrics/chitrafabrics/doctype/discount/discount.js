frappe.ui.form.on("Discount", {
    refresh(frm){
        frm.set_query("item","items", function (doc) {
            if(doc.item_type == "Item Template"){
                return {
                    filters: {
                        has_variants: 1,
                    },
                }
            }
            else{
                return {
                    filters: {
                        has_variants: 0,
                    },
                }
            }
		});
    },

    get_batch(frm) {
        frappe.call({
            method: "chitrafabrics.chitrafabrics.doctype.discount.discount.discount",
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
