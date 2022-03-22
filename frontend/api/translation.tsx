import client from "./client";

const endpoint: string = "/api/v1/translation";

const oneToone = async (data: any) =>
  await client.post(`${endpoint}/one-to-one`, data);

const translation = { oneToone };
export default translation;
