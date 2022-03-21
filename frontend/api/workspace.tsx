import client from "./client";

const endpoint: string = "/api/v1/workspace";

const newWorkspace = async (data: any) =>
  await client.post(`${endpoint}/create-new-workspace`, data);

const workspace = { newWorkspace };
export default workspace;
