
erpnext.PointOfSale.Controller = class Controller extends erpnext.PointOfSale.Controller {
	
	make_sales_invoice_frm() {
		const doctype = "POS Invoice";
		return new Promise((resolve) => {
			if (this.frm) {
				this.set_pos_profile_data();
				this.frm = this.get_new_frm(this.frm);
				this.frm.doc.items = [];
				this.frm.doc.is_pos = 1;
				resolve();
			} else {
				frappe.model.with_doctype(doctype, () => {
					this.frm = this.get_new_frm();
					this.frm.doc.items = [];
					this.frm.doc.is_pos = 1;
					resolve();
				});
			}
		});
	}
}
