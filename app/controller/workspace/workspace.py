from fastapi import APIRouter, Depends, Body

from app.config.authorization import Authorization
from app.dto.controller.workspace import CreateWorkspaceDTO

router = APIRouter(dependencies=[Depends(Authorization.authenticate)], tags=["workspace"])


@router.post('/api/v1/create-new-workspace')
def create_workspace(data: CreateWorkspaceDTO = Body(...)):
    from app.config.authorization import Authorization
    from app.dto.model.customer import CustomerDTO
    from app.service.model.workspace import WorkspaceLib
    from app.service.model.workspace_role import WorkspaceRoleLib
    from app.service.model.workspace_detail import WorkspaceDetailLib
    from app.service.model.language import LanguageLib
    from app.dto.model.workspace import WorkspaceDTO
    from fastapi.encoders import jsonable_encoder
    from app.config.success_response import SuccessResponse
    from fastapi import status

    # check default language if exist
    language = LanguageLib.find_by(where={"name": data.default_language})
    if not language:
        return SuccessResponse(data=None).set_message("language not available for now"). \
            set_status_code(status.HTTP_400_BAD_REQUEST).response()

    customer: CustomerDTO = Authorization.get_customer()

    record: dict = jsonable_encoder(data)
    record["default_language"] = language.id
    record["customer_id"] = customer.id
    record["customer_count"] = 1

    # create workspace
    workspace: WorkspaceDTO = WorkspaceLib.create(data=record)

    workspace_role = WorkspaceRoleLib.find_by({"name": "Admin"})

    # create workspace detail
    WorkspaceDetailLib.create(data={"workspace_id": workspace.id,
                                    "customer_id": customer.id,
                                    "workspace_role_id": workspace_role.id}
                              )

    return SuccessResponse(data={"workspace": workspace}
                           ).set_message("workspace created").response()
