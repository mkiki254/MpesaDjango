from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_index(request):
    cl = MpesaClient()
    reference = "FundisConnect"
    amount = 1
    phone_number = "254712345678"
    transaction_description = "Description"
    callback_url = 'https://91a5-41-89-10-241.ngrok-free.app/mpesa/'
    response = cl.stk_push(phone_number, amount,reference, transaction_description, callback_url)

    if request.method == 'POST':
        result = cl.parse_stk_result(request.body)
        if result["ResultCode"] == 0:
            print(result)

    return HttpResponse(response)

# {'ResultCode': 0, 'ResultDesc': 'The service request is processed successfully.', 'MerchantRequestID': '129072-144816073-1', 'CheckoutRequestID': 'ws_CO_18062023131110046741518186', 'Amount': 1.0, 'MpesaReceiptNumber': 'RFI6CV23K8', 'Balance': None, 'TransactionDate': 20230618131010, 'PhoneNumber': 254741518186}

