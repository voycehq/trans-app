import { NextPage } from "next";
import Link from "next/link";
import { FormEvent, useRef, useState } from "react";

import { InputEmail, InputPassword, InputText } from "../components/Inputs";
import Logo from "../components/Logo";
import Spinner from "../components/Spinner";
import style from "../styles/pages/Login.module.sass";

const Signup: NextPage = () => {
  const inputTextRef = useRef<HTMLInputElement>(null);
  const s: any = { width: "100%", marginBottom: "20px" };
  const [state, setState] = useState({
    email: "",
    password: "",
    full_name: "",
  });
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
            <h2>Sign up</h2>
            <p>One account across all workspaces.</p>
          </header>

          <div>
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
