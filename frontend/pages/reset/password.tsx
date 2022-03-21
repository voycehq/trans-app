/* eslint-disable react-hooks/exhaustive-deps */
import { NextPage } from "next";
import Link from "next/link";
import { useRouter } from "next/router";
import { FormEvent, useEffect, useRef, useState } from "react";
import auth from "../../api/auth";
import Alert from "../../components/Alert";

import { InputPassword, InputText } from "../../components/Inputs";
import Logo from "../../components/Logo";
import Spinner from "../../components/Spinner";
import useApi from "../../libs/useApi";
import authStorage from "../../store";
import style from "../../styles/pages/Login.module.sass";

const Signup: NextPage = () => {
  const router = useRouter();
  const inputTextRef = useRef<HTMLInputElement>(null);
  const s: any = { width: "100%", marginBottom: "20px" };
  const [state, setState] = useState({
    password: "",
    code: "",
  });
  const { setEmail, recoveryEmail, getUser, user } = authStorage();
  const { request, loading, message, status, error, data } = useApi(
    auth.resetPassword
  );

  const onChange = ({ target: { id, value } }: any) =>
    setState({ ...state, [id]: value });

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    request({ ...state, email: recoveryEmail });
  };

  // Hooks
  useEffect(() => inputTextRef.current?.focus(), []);
  useEffect(() => {
    if (status !== 200) return;
    setEmail(null);
    setTimeout(() => router.push("/login"), 5000);
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
            <h2>Password Reset</h2>
            <p>
              Enter the code sent to your email <br /> and a new password to
              reset your account password.
            </p>
          </header>

          <div>
            <Alert
              className={status !== 200 ? "danger" : "success"}
              visible={status !== null}
            >
              {message}
            </Alert>
            <InputText
              height={50}
              s={s}
              label="Code"
              inputRef={inputTextRef}
              onChange={onChange}
              id="code"
              value={state.code}
            />
            <InputPassword
              height={50}
              s={s}
              label="New Password"
              onChange={onChange}
              id="password"
              value={state.password}
            />
          </div>

          <footer>
            <Link href="/login">
              <a>Back to login</a>
            </Link>

            <button type={loading ? "button" : "submit"}>
              {loading && <Spinner visible bgColor="#fff" />}
              {!loading && <span>Reset password</span>}
            </button>
          </footer>
        </form>

        <footer className={style.footer} style={{ marginLeft: "0" }}>
          <p>
            Voyce advice! <br /> Try not to forget your password again. -:)
          </p>
        </footer>
      </div>
    </main>
  );
};

export default Signup;
