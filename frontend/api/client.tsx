import { create } from "apisauce";
import authStorage from "../store";

const client = create({ baseURL: "http://localhost:4000" });
client.addAsyncRequestTransform(async (request) => {
  const apiKey = authStorage.getState().getApiKey();
  if (!apiKey) return;

  request.headers["api-key"] = apiKey;
});

export default client;
