import client from "./client";

const endpoint: string = "/api/v1/auth";

interface SignupProps {
  email: string;
  password: string;
  full_name: string;
}
const signup = async (data: SignupProps) =>
  await client.post(`${endpoint}/signup`, data);

const auth = { signup };
export default auth;
