from .base import AxisBankClient
from .models import GetStatusRequest, GetStatusResponse

class TransactionStatusClient(AxisBankClient):
    def get_status(self, request: GetStatusRequest, test_id: int = None) -> GetStatusResponse:
        endpoint = "/get-status"
        headers = self._prepare_headers({"X-AXIS-TEST-ID": str(test_id)}) if test_id else self._prepare_headers()
        data = request.model_dump()
        response_data = self._make_request(endpoint, data, headers)
        return GetStatusResponse(**response_data)
