/* eslint-disable react-hooks/exhaustive-deps */
import { NextPage } from "next";
import Link from "next/link";
import { useRouter } from "next/router";
import { FormEvent, useEffect, useRef, useState } from "react";
import auth from "../api/auth";
import Alert from "../components/Alert";

import { InputEmail, InputPassword } from "../components/Inputs";
import Logo from "../components/Logo";
import Spinner from "../components/Spinner";
import useApi from "../libs/useApi";
import authStorage from "../store";
import style from "../styles/pages/Login.module.sass";

const Login: NextPage = () => {
  const router = useRouter();
  const inputTextRef = useRef<HTMLInputElement>(null);
  const s: any = { width: "100%", marginBottom: "20px" };
  const [state, setState] = useState({ email: "", password: "" });
  const { setUser, user, apiKey, getUser } = authStorage();

  const { request, loading, error, message, status, data } = useApi(auth.login);

  const onChange = ({ target: { id, value } }: any) =>
    setState({ ...state, [id]: value });

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    request(state);
  };

  // Hooks
  useEffect(() => inputTextRef.current?.focus(), []);

  useEffect(() => {
    if (status == 403) router.push("/verify");
    if (status == 200 && data) setUser(data.data);
  }, [data]);

  useEffect(() => {
    const user = getUser();
    if (user) {
      if (!user.is_verified) router.push("/verify");

      if (apiKey && user.is_verified) router.push("/dashboard");
    }
  }, [user]);

  return (
    <main className={style.main}>
      <div className={style.main__wrapper}>
        <header className={style.header}>
          <Logo />
        </header>
        <form
          style={{ gap: "1rem" }}
          className={style.form}
          onSubmit={onSubmit}
        >
          <header>
            <h2>Sign in</h2>
            <p>One account across all workspaces.</p>
          </header>

          <div>
            <Alert className={error ? "danger" : "success"} visible={error}>
              {message}
            </Alert>
            <InputEmail
              height={50}
              s={s}
              label="Email"
              inputRef={inputTextRef}
              onChange={onChange}
              id="email"
              value={state.email}
            />
            <InputPassword
              height={50}
              s={s}
              label="Password"
              onChange={onChange}
              id="password"
              value={state.password}
            />
          </div>

          <footer>
            <Link href="/reset">
              <a>Forgot Password</a>
            </Link>
            <button type={loading ? "button" : "submit"}>
              {loading && <Spinner visible bgColor="#fff" />}
              {!loading && <span>Sign in</span>}
            </button>
          </footer>
        </form>

        <footer className={style.footer}>
          <p>
            Don&apos;t have an account?{" "}
            <Link href="/signup">
              <a>Sign up here</a>
            </Link>
          </p>
        </footer>
      </div>
    </main>
  );
};

export default Login;
