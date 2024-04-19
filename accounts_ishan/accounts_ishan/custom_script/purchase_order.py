import frappe
import requests

def before_save(doc,method=None):
    
    pan = frappe.db.get_value('Supplier', doc.supplier, 'pan')
    if not pan:
        return

    url = f"{frappe.utils.get_url()}/api/method/crm_ishan.api.lead_api.validate_docs"
    params = {
        "reference_id": doc.name,
        "document_type": 'PAN-DETAILED',
        "id_number": pan
    }

    # response = requests.get(url, params=params)
    # json_data = response.json()
    # frappe.errprint(json_data)
    # id_status = json_data['message']['kycResult']['idStatus']

    # if id_status == 'VALID':
    #     return
    tds_section = frappe.db.get_value('Supplier', doc.supplier, 'tax_withholding_category.tds_section')
    non_pan_section = frappe.db.get_value('Tax Withholding Category', {'entity_type': 'No PAN / Invalid PAN', 'tds_section': tds_section})
    doc.tax_withholding_category = non_pan_section