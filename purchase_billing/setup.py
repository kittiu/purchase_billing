import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from sales_billing.constants import CUSTOM_FIELDS

def after_install():
	create_custom_fields(CUSTOM_FIELDS, ignore_validate=True)

def before_uninstall():
	delete_custom_fields(CUSTOM_FIELDS)

def delete_custom_fields(custom_fields: dict):
	for doctype, fields in custom_fields.items():
		frappe.db.delete(
			"Custom Field",
			{
				"fieldname": ("in", [field["fieldname"] for field in fields]),
				"dt": doctype,
			},
		)
		frappe.clear_cache(doctype=doctype)