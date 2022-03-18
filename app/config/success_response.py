class SuccessResponse:
    def __init__(self, data):
        from fastapi import status

        self.data = data
        self.result = {"message": "success", "data": data}
        self.statusCode = status.HTTP_200_OK

    def set_message(self, message: str):
        self.result['message'] = message
        return self

    def set_status_code(self, status_code: int):
        self.statusCode = status_code
        return self

    def response(self):
        from fastapi.encoders import jsonable_encoder
        from fastapi.responses import JSONResponse
        result: dict = {**self.result, 'statusCode': self.statusCode}
        return JSONResponse(content=jsonable_encoder(result), status_code=self.statusCode)

