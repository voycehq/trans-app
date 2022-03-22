import client from "./client";

const endpoint: string = "/api/v1/language";

const fetchLangauges = async (apiKey: any) =>
  await client.setHeader("api-key", apiKey).get(`${endpoint}/get-all-language`);

const language = { fetchLangauges };
export default language;
