frappe.ui.form.on("Discount", {
    item_type: function(frm) {
        if (frm.doc.item_type == "Item Template") {
            frm.fields_dict['items'].grid.get_field('item').get_query = function(doc, cdt, cdn) {
                return {
                    filters: [
                        ['Item', 'has_variants', '=', 1]
                    ]
                };
            };
        } else {
            frm.fields_dict['items'].grid.get_field('item').get_query = function(doc, cdt, cdn) {
                return {
                    filters: [
                        ['Item', 'has_variants', '=', 0]
                    ]
                };
            };
        }
    } ,
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
