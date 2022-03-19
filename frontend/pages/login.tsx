import { NextPage } from "next";
import Link from "next/link";
import { FormEvent, useRef, useState } from "react";
import { InputEmail, InputPassword } from "../components/Inputs";

import style from "../styles/pages/Login.module.sass";

const Login: NextPage = () => {
  const inputTextRef = useRef<HTMLInputElement>(null);
  const s: any = { width: "100%" };
  const [state, setState] = useState({ email: "", password: "" });

  const onChange = ({ target: { id, value } }: any) =>
    setState({ ...state, [id]: value });

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    // setLoading(!loading);
    // setOpen(true);
    console.log(state);
  };

  return (
    <main className={style.main}>
      <div className={style.main__wrapper}>
        <header className={style.header}>
          <h1>Voyce</h1>
        </header>
        <form className={style.form} onSubmit={onSubmit}>
          <header>
            <h2>Sing in</h2>
            <p>One account across all workspaces.</p>
          </header>

          <div>
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
            <Link href="/">
              <a>Forgot Password</a>
            </Link>
            <button type="submit">Sign in</button>
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
