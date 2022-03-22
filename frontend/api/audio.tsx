import client from "./client";

const endpoint: string = "/api/v1/audio";

const oneToMany = async (data: any) =>
  await client.post(`${endpoint}/one-to-many`, data);

const audio = { oneToMany };
export default audio;
