import client from "./client";

const endpoint: string = "/api/v1/workspace";

const newWorkspace = async (data: any) =>
  await client.post(`${endpoint}/create-new-workspace`, data);

const getUserWorkspace = async () =>
  await client.get(`${endpoint}/get-user-workspace`);

const getWorkspaceById = async (id: number) =>
  await client.get(`${endpoint}/${id}`);

const workspace = { newWorkspace, getUserWorkspace, getWorkspaceById };
export default workspace;
