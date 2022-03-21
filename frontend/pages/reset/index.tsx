/* eslint-disable react-hooks/exhaustive-deps */
import { NextPage } from "next";
import Link from "next/link";
import { useRouter } from "next/router";
import { FormEvent, useEffect, useRef, useState } from "react";
import auth from "../../api/auth";
import Alert from "../../components/Alert";

import { InputEmail, InputText } from "../../components/Inputs";
import Logo from "../../components/Logo";
import Spinner from "../../components/Spinner";
import useApi from "../../libs/useApi";
import authStorage from "../../store";
import style from "../../styles/pages/Login.module.sass";

const ResetPassword: NextPage = () => {
  const router = useRouter();
  const inputTextRef = useRef<HTMLInputElement>(null);
  const s: any = { width: "100%", marginBottom: "20px" };
  const [state, setState] = useState({ email: "" });
  const { setEmail, user, getUser } = authStorage();

  const { request, loading, error, message, status, data } = useApi(
    auth.forgotPassword
  );

  const onChange = ({ target: { value } }: any) => setState({ email: value });

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    request(state);
  };

  // Hooks
  useEffect(() => inputTextRef.current?.focus(), []);
  useEffect(() => {
    if (status !== 200) return;
    setEmail(state.email);
    router.push("/reset/password");
  }, [data]);

  useEffect(() => {
    const user = getUser();
    if (user) router.push("/login");
  }, [user]);

  return (
    <main className={style.main}>
      <div className={style.main__wrapper}>
        <header className={style.header}>
          <Logo />
        </header>
        <form
          style={{ gap: ".5rem" }}
          className={style.form}
          onSubmit={onSubmit}
        >
          <header>
            <h2>Account Recovery</h2>
            <p>Please enter your account email to continue.</p>
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
          </div>

          <footer>
            <Link href="/login">
              <a>Back to login</a>
            </Link>
            <button type={loading ? "button" : "submit"}>
              {loading && <Spinner visible bgColor="#fff" />}
              {!loading && <span>Next</span>}
            </button>
          </footer>
        </form>

        <footer className={style.footer} style={{ marginLeft: "0" }}>
          <p>
            Voyce get it. <br /> Sometimes it&apos;s hard to remember password.
          </p>
        </footer>
      </div>
    </main>
  );
};

export default ResetPassword;
