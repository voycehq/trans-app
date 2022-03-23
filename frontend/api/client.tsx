import { create } from "apisauce";
import authStorage from "../store";
import { http } from "../libs/utils";

const client = create({ baseURL: http });
client.addAsyncRequestTransform(async (request) => {
  const apiKey = authStorage.getState().getApiKey();
  if (!apiKey) return;

  request.headers["api-key"] = apiKey;
});

export default client;
