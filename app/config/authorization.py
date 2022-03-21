from starlette_context import context
from app.dto.model.customer import CustomerDTO


class Authorization:
    from fastapi import Header
    from typing import Optional

    @staticmethod
    def authenticate(api_key: Optional[str] = Header(None, title="the api key")):
        """
        Authenticate any party request and set user to route context
        Args:
            api_key:

        Returns:

        """
        from app.logs import logger
        from fastapi import HTTPException, status
        from app.service.model.customer import CustomerLib

        if not api_key:
            logger.error("api-key is required")
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="api-key is required")

        # get customer information
        customer = CustomerLib.find_by(where={"api_key": api_key})
        if not customer or api_key != customer.api_key:

            logger.error("invalid api-key")
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid api-key")

        context['customer'] = customer

    @staticmethod
    def get_customer() -> CustomerDTO:

        """
        Get customer object from request context
        Returns: -> CustomerDTO

        """

        return context.get("customer")
