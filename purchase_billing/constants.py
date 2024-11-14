CUSTOM_FIELDS = {
    "Payment Entry": [
        {
            "fieldname": "column_break_42",
            "fieldtype": "Column Break",
            "insert_after": "get_outstanding_orders",
        },
        {
            "depends_on": 'eval:doc.docstatus == 0 && doc.payment_type == "Pay" && doc.party_type == "Supplier" && doc.party',
            "fieldname": "get_invoices_from_purchase_billing",
            "fieldtype": "Button",
            "insert_after": "column_break_42",
            "label": "Get Invoices from Purchase Billing",
        },
        {
            "fieldname": "purchase_billing",
            "fieldtype": "Link",
            "read_only": 1,
            "insert_after": "get_invoices_from_purchase_billing",
            "label": "Purchase Billing",
            "options": "Purchase Billing",
        },
        {
            "fieldname": "section_break_44",
            "fieldtype": "Section Break",
            "insert_after": "purchase_billing",
        },
    ],
}
