from fastapi import APIRouter, Depends, Path

from app.config.authorization import Authorization

router = APIRouter(dependencies=[Depends(Authorization.authenticate)], tags=["workspace"])


@router.get('/api/v1/workspace/{workspace_id}')
def get_workspaces_by_id(workspace_id: int):
    from app.service.model.workspace import WorkspaceLib
    from app.config.success_response import SuccessResponse
    from fastapi import status

    customer = Authorization.get_customer()
    workspace = WorkspaceLib.find_by(where={"customer_id": customer.id, "id": workspace_id}, get_all=False)
    if not workspace:
        return SuccessResponse(data=None).set_message(f"No workspace with id: {workspace_id}").set_status_code(status.HTTP_400_BAD_REQUEST).response()

    return SuccessResponse(data=workspace).set_status_code(status.HTTP_200_OK).response()


