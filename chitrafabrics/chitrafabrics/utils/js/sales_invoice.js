frappe.ui.form.on('Sales Invoice', {
    refresh(frm){
        console.log("lllll")
    } ,
    branch(frm){
        if (frm.doc.branch) {
            frm.set_value("set_warehouse" , frm.doc.branch + " - CF" )
        }
        
    },

});


