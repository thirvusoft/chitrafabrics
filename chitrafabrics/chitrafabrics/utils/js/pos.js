frappe.pages['point-of-sale'].on_page_load = function (wrapper) {
    frappe.ui.make_app_page({
        parent: wrapper,
        title: __('Point of Sale'),
        single_column: true
    });

    frappe.require('point-of-sale.bundle.js', function () {
        frappe.require('pos.bundle.js', function () {
            wrapper.pos = new erpnext.PointOfSale.Controller(wrapper);
            window.cur_pos = wrapper.pos;
        })     
    });
};