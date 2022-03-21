import client from "./client";

const endpoint: string = "/api/v1/auth";

interface SignupProps {
  email: string;
  password: string;
  full_name: string;
}
const signup = async (data: SignupProps) =>
  await client.post(`${endpoint}/signup`, data);

interface EmailProps {
  email: string;
  code: string;
}
const verifyEmail = async (data: EmailProps) =>
  await client.post(`${endpoint}/verify-email`, data);

interface CodeProps {
  email: string;
}
const resendCode = async (data: CodeProps) =>
  await client.post(`${endpoint}/resend-verification-code`, data);

interface LoginProps {
  email: string;
  password: string;
}
const login = async (data: LoginProps) =>
  await client.post(`${endpoint}/login`, data);

const auth = { signup, verifyEmail, resendCode, login };
export default auth;
