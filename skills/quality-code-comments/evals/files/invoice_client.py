class InvoiceNotFound(Exception):
    pass


def fetch_invoice(invoice_id, include_line_items=False):
    record = store.get(invoice_id)
    if record is None:
        raise InvoiceNotFound(invoice_id)
    if include_line_items:
        record = {**record, "line_items": store.line_items(invoice_id)}
    return record
