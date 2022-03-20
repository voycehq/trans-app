import { NextPage } from "next";
import Link from "next/link";
import { FormEvent, useRef, useState } from "react";

import { InputEmail, InputText } from "../../components/Inputs";
import Logo from "../../components/Logo";
import Spinner from "../../components/Spinner";
import style from "../../styles/pages/Login.module.sass";

const ResetPassword: NextPage = () => {
  const inputTextRef = useRef<HTMLInputElement>(null);
  const s: any = { width: "100%", marginBottom: "20px" };
  const [state, setState] = useState({ email: "" });
  const [loading, setLoading] = useState(false);

  const onChange = ({ target: { id, value } }: any) => setState(value);

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
            <h2>Account Recovery</h2>
            <p>Please enter your account email to continue.</p>
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
