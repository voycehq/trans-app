from fastapi import APIRouter, Depends

from app.config.authorization import Authorization

router = APIRouter(dependencies=[Depends(Authorization.authenticate)], tags=["workspace"])


@router.get('/api/v1/workspace/get-user-workspace')
def get_user_workspaces():
    from app.service.model.workspace import WorkspaceLib
    from app.config.success_response import SuccessResponse
    from fastapi import status

    customer = Authorization.get_customer()

    workspaces = WorkspaceLib.find_by(where={"customer_id": customer.id}, get_all=True)

    return SuccessResponse(data=workspaces).set_status_code(status.HTTP_200_OK).response()


