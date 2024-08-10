from .base import AxisBankClient
from .models import TransferPaymentRequest, TransferPaymentResponse

class TransferPaymentClient(AxisBankClient):
    def transfer_payment(self, request: TransferPaymentRequest, test_id: int = None) -> TransferPaymentResponse:
        endpoint = "/transfer"
        headers = self._prepare_headers({"X-AXIS-TEST-ID": str(test_id)}) if test_id else self._prepare_headers()
        data = request.model_dump()
        response_data = self._make_request(endpoint, data, headers)
        return TransferPaymentResponse(**response_data)
