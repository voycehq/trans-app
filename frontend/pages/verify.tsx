/* eslint-disable react-hooks/exhaustive-deps */
import { NextPage } from "next";
import Link from "next/link";
import { useRouter } from "next/router";
import { FormEvent, useEffect, useRef, useState } from "react";

import { InputText } from "../components/Inputs";
import Logo from "../components/Logo";
import Spinner from "../components/Spinner";
import useApi from "../libs/useApi";
import authStorage from "../store";
import style from "../styles/pages/Login.module.sass";
import auth from "../api/auth";
import Alert from "../components/Alert";

const Verification: NextPage = () => {
  const router = useRouter();
  const inputTextRef = useRef<HTMLInputElement>(null);
  const s: any = { width: "100%", marginBottom: "20px" };
  const [state, setState] = useState({ code: "" });
  const { updateUser, getUser, user, apiKey } = authStorage();

  const resendCodeApi = useApi(auth.resendCode);
  const { request, loading, message, status, data, _private } = useApi(
    auth.verifyEmail
  );

  const onChange = ({ target: { value } }: any) => setState({ code: value });
  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const user = getUser();
    request({ ...state, email: user.email });
  };
  const handleResendCode = () => {
    if (resendCodeApi.loading) return;
    resendCodeApi.request({ email: getUser().email });
  };

  // Hooks
  useEffect(() => inputTextRef.current?.focus(), []);
  useEffect(() => {
    if (status !== 200) return;
    updateUser({ is_verified: true });

    setTimeout(() => router.push("/login"), 5000);
  }, [data]);

  useEffect(() => {
    const user = getUser();
    if (user) {
      if (!user.is_verified) return;

      if (apiKey) router.push("/workspace");
      else router.push("/login");
    } else router.push("/login");
  }, [user]);

  // useEffect(() => {
  //   setTimeout(() => {
  //     resendCodeApi._private._reset();
  //     _private._reset();
  //   }, 5000);
  // }, [resendCodeApi.status, status]);

  return (
    <main className={style.main}>
      <div className={style.main__wrapper}>
        <header className={style.header}>
          <Logo />
        </header>
        <form
          className={style.form}
          style={{ gap: ".5rem" }}
          onSubmit={onSubmit}
        >
          <header>
            <h2>Email Verification</h2>
            <p>Enter the code sent to your email to verify your account.</p>
          </header>

          <div>
            <Alert
              className={status !== 200 ? "danger" : "success"}
              visible={status !== null}
            >
              {message}
            </Alert>
            {resendCodeApi.status !== null && (
              <Alert
                className={resendCodeApi.status !== 200 ? "danger" : "success"}
                visible={resendCodeApi.status == 200}
              >
                {resendCodeApi.message}
              </Alert>
            )}
            <InputText
              height={50}
              s={s}
              label="code"
              inputRef={inputTextRef}
              onChange={onChange}
              id="code"
              value={state.code}
            />
          </div>

          <footer>
            <button type="button" onClick={handleResendCode}>
              {resendCodeApi.loading && <Spinner visible bgColor="#fff" />}
              {!resendCodeApi.loading && <span>Resend code</span>}
            </button>

            <button type={status == 200 ? "button" : "submit"}>
              {loading && <Spinner visible bgColor="#fff" />}
              {!loading && <span>Verify account</span>}
            </button>
          </footer>
        </form>

        <footer className={style.footer}>
          <p>Voyce wants to make sure it&apos;s you.</p>
        </footer>
      </div>
    </main>
  );
};

export default Verification;
