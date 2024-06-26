app_name = "chitrafabrics"
app_title = "chitrafabrics"
app_publisher = "Thirvusoft"
app_description = "chitra fabrics - textile industry"
app_email = "thirvusoft@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/chitrafabrics/css/chitrafabrics.css"
# app_include_js = "/assets/chitrafabrics/js/chitrafabrics.js"

# include js, css files in header of web template
# web_include_css = "/assets/chitrafabrics/css/chitrafabrics.css"
# web_include_js = "/assets/chitrafabrics/js/chitrafabrics.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "chitrafabrics/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
page_js = {
    "point-of-sale" : "chitrafabrics/utils/js/pos.js"
}

# include js in doctype views
doctype_js = {"Sales Invoice" : "chitrafabrics/utils/js/sales_invoice.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "chitrafabrics/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generatorsapps
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "chitrafabrics.utils.jinja_methods",
# 	"filters": "chitrafabrics.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "chitrafabrics.install.before_install"
# after_install = "chitrafabrics.migrate.after_migrate"
# after_migrate = "chitrafabrics.migrate.after_migrate"

# Uninstallation
# ------------

# before_uninstall = "chitrafabrics.uninstall.before_uninstall"
# after_uninstall = "chitrafabrics.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "chitrafabrics.utils.before_app_install"
# after_app_install = "chitrafabrics.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "chitrafabrics.utils.before_app_uninstall"
# after_app_uninstall = "chitrafabrics.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "chitrafabrics.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {  
    "Stock Entry" : {
        "on_update":"chitrafabrics.chitrafabrics.utils.py.stock_entry.fetchdata"
	},
	"Item": {
        "on_update": "chitrafabrics.chitrafabrics.utils.py.purchase_invoice.new_rate",
		"autoname": "chitrafabrics.chitrafabrics.utils.py.item.item_name",
        "on_trash":"chitrafabrics.chitrafabrics.utils.py.item.item_name_delete"
	} ,
    # "Purchase Receipt": {
	# 	"on_update": "chitrafabrics.chitrafabrics.utils.py.purchase_invoice.last_rate",
	# } ,
	"Batch":{
		"autoname":"chitrafabrics.chitrafabrics.utils.py.batch.batch_id_naming",
		"on_trash":"chitrafabrics.chitrafabrics.utils.py.batch.batch_id_trash"
	},
	"Serial and Batch Bundle": {
		"on_submit":"chitrafabrics.chitrafabrics.utils.py.batch.price_updation"
	},
	"Sales Invoice": {
		"autoname":"chitrafabrics.chitrafabrics.utils.py.sales_invoice.sales_invoice_naming",
		"on_trash":"chitrafabrics.chitrafabrics.utils.py.sales_invoice.sales_invoice_naming_deletion",
        "before_cancel": "chitrafabrics.chitrafabrics.utils.py.sales_invoice.before_cancel",
        # "validate": "chitrafabrics.chitrafabrics.utils.py.sales_invoice.validate"

	},
    "POS Invoice":{
        "on_submit": "chitrafabrics.chitrafabrics.utils.py.pos_invoice.on_submit"
	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {

	# "cron" : {
	# 	"0 22 * * *": "chitrafabrics.chitrafabrics.utils.py.item.test"
	# } , 



# 	"all": [
# 		"chitrafabrics.tasks.all"
# 	],
	"daily": [
		"chitrafabrics.chitrafabrics.doctype.discount.discount.discount_end"
	],
# 	"hourly": [
# 		"chitrafabrics.tasks.hourly"
# 	],
# 	"weekly": [
# 		"chitrafabrics.tasks.weekly"
# 	],
# 	"monthly": [
# 		"chitrafabrics.tasks.monthly"
# 	],
}

# Testing
# -------

# before_tests = "chitrafabrics.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "chitrafabrics.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "chitrafabrics.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["chitrafabrics.utils.before_request"]
# after_request = ["chitrafabrics.utils.after_request"]

# Job Events
# ----------
# before_job = ["chitrafabrics.utils.before_job"]
# after_job = ["chitrafabrics.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"chitrafabrics.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

