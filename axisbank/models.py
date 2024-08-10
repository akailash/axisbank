from pydantic import BaseModel, Field
from typing import List, Optional

class SubHeader(BaseModel):
    requestUUID: str
    serviceRequestId: str
    serviceRequestVersion: str
    channelId: str

# GetStatus

class GetStatusRequestBody(BaseModel):
    channelId: str
    corpCode: str
    checksum: str
    crn: str

class GetStatusRequest(BaseModel):
    SubHeader: SubHeader
    GetStatusRequestBody: GetStatusRequestBody

class ArrayField(BaseModel):
    corpCode: str
    statusDescription: str
    batchNo: str
    utrNo: str
    processingDate: str
    responeCode: str
    crn: str
    transactionStatus: str

class Data(BaseModel):
    CUR_TXN_ENQ: Optional[List[ArrayField]]
    errorMessage: str
    checksum: str

class GetStatusResponseBody(BaseModel):
    status: str
    data: Data
    message: str

class GetStatusResponse(BaseModel):
    SubHeader: SubHeader
    GetStatusResponseBody: GetStatusResponseBody

# TransferPayment

class TransferPaymentRequestBody(BaseModel):
    accountNumber: str
    beneficiaryAccountNumber: str
    amount: float
    currency: str
    paymentDate: str

class TransferPaymentRequest(BaseModel):
    SubHeader: SubHeader
    TransferPaymentRequestBody: TransferPaymentRequestBody


class TransferPaymentResponseBody(BaseModel):
    transactionStatus: str
    transactionReference: str
    message: Optional[str]

class TransferPaymentResponse(BaseModel):
    SubHeader: SubHeader
    TransferPaymentResponseBody: TransferPaymentResponseBody

class RequestData(BaseModel):
    corpCode: str
    channelId: str
    remitterAcc: str
    beneAccNum: str
    beneIFSC: str
    checksum: str

class AccountValidationAPIRequest(BaseModel):
    Data: RequestData
    Risks: dict = Field(default_factory=dict)  # Assuming Risks is an optional object

class ResponseData(BaseModel):
    code: str
    message: str
    data: str
    status: str

class AccountValidationAPIResponse(BaseModel):
    Data: ResponseData
