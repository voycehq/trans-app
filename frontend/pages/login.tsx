import { NextPage } from "next";
import Link from "next/link";
import { FormEvent, useRef, useState } from "react";

import { InputEmail, InputPassword } from "../components/Inputs";
import Logo from "../components/Logo";
import Spinner from "../components/Spinner";
import style from "../styles/pages/Login.module.sass";

const Login: NextPage = () => {
  const inputTextRef = useRef<HTMLInputElement>(null);
  const s: any = { width: "100%", marginBottom: "20px" };
  const [state, setState] = useState({ email: "", password: "" });
  const [loading, setLoading] = useState(false);

  const onChange = ({ target: { id, value } }: any) =>
    setState({ ...state, [id]: value });

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    setLoading(!loading);
    console.log(state);
  };

  return (
    <main className={style.main}>
      <div className={style.main__wrapper}>
        <header className={style.header}>
          <Logo />
        </header>
        <form className={style.form} onSubmit={onSubmit}>
          <header>
            <h2>Sign in</h2>
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
