from .base import AxisBankClient
from .models import AccountValidationAPIRequest, AccountValidationAPIResponse


class AccountValidationClient(AxisBankClient):
    def validate_account(
        self, 
        x_fapi_epoch_millis: str,
        x_fapi_channel_id: str,
        x_fapi_uuid: str,
        x_fapi_service_id: str,
        x_fapi_service_version: str,
        x_axis_test_id: int,
        request_body: AccountValidationAPIRequest
    ):
        headers = {
            "x-fapi-epoch-millis": x_fapi_epoch_millis,
            "x-fapi-channel-id": x_fapi_channel_id,
            "x-fapi-uuid": x_fapi_uuid,
            "x-fapi-serviceId": x_fapi_service_id,
            "x-fapi-serviceVersion": x_fapi_service_version,
            "X-AXIS-TEST-ID": str(x_axis_test_id),
        }
        return self._make_request(
            endpoint="account-validation",
            headers=headers,
            json_body=request_body.model_dump(),
        )
