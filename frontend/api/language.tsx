import client from "./client";

const endpoint: string = "/api/v1/language";

const fetchLangauges = async () =>
  await client.get(`${endpoint}/get-all-language`);

const language = { fetchLangauges };
export default language;
