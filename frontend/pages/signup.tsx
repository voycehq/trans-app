/* eslint-disable react-hooks/exhaustive-deps */
import { NextPage } from "next";
import { useRouter } from "next/router";
import Link from "next/link";
import { FormEvent, useEffect, useRef, useState } from "react";

import { InputEmail, InputPassword, InputText } from "../components/Inputs";
import auth from "../api/auth";
import Logo from "../components/Logo";
import Spinner from "../components/Spinner";
import useApi from "../libs/useApi";
import style from "../styles/pages/Login.module.sass";
import authStorage, { User } from "../store";
import Alert from "../components/Alert";

const Signup: NextPage = () => {
  const router = useRouter();
  const inputTextRef = useRef<HTMLInputElement>(null);
  const s: any = { width: "100%", marginBottom: "20px" };
  const { setUser, user, apiKey, getUser } = authStorage();

  const [state, setState] = useState({
    email: "",
    password: "",
    full_name: "",
  });
  const { request, loading, error, message, status, data } = useApi(
    auth.signup
  );

  const onChange = ({ target: { id, value } }: any) =>
    setState({ ...state, [id]: value });

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    request(state);
  };

  // Hooks
  useEffect(() => inputTextRef.current?.focus(), []);

  useEffect(() => {
    if (status !== 200) return;
    setUser(data?.data);

    router.push("/verify");
  }, [data]);

  useEffect(() => {
    const user = getUser();
    if (user) {
      if (!user.is_verified) router.push("/verify");

      if (apiKey && user.is_verified) router.push("/workspace");
      else router.push("/login");
    }
  }, [user]);

  return (
    <main className={style.main}>
      <div className={style.main__wrapper}>
        <header className={style.header}>
          <Logo />
        </header>
        <form
          className={style.form}
          style={{ gap: "0rem" }}
          onSubmit={onSubmit}
        >
          <header>
            <h2>Sign up</h2>
            <p>One account across all workspaces.</p>
          </header>

          <div style={{ marginTop: ".5rem" }}>
            <Alert className={error ? "danger" : "success"} visible={error}>
              {message}
            </Alert>
            <InputText
              height={50}
              s={s}
              label="Full name"
              inputRef={inputTextRef}
              onChange={onChange}
              id="full_name"
              value={state.full_name}
            />
            <InputEmail
              height={50}
              s={s}
              label="Email"
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
            {/* Checkbox about agreement to privacy policy */}
            <span></span>

            <button type={loading ? "button" : "submit"}>
              {loading && <Spinner visible bgColor="#fff" />}
              {!loading && <span>Sign up now</span>}
            </button>
          </footer>
        </form>

        <footer className={style.footer} style={{ marginTop: "2rem" }}>
          <p>
            Already have an account?{" "}
            <Link href="/login">
              <a>Sign in here</a>
            </Link>
          </p>
        </footer>
      </div>
    </main>
  );
};

export default Signup;
