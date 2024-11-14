
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from purchase_billing.constants import CUSTOM_FIELDS

def execute():
    # Create custom fields defined in CUSTOM_FIELDS
    create_custom_fields(CUSTOM_FIELDS, ignore_validate=True)
