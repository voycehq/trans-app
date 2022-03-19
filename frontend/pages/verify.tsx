import { NextPage } from "next";
import Link from "next/link";
import { FormEvent, useRef, useState } from "react";

import { InputText } from "../components/Inputs";
import Spinner from "../components/Spinner";
import style from "../styles/pages/Login.module.sass";

const Verification: NextPage = () => {
  const inputTextRef = useRef<HTMLInputElement>(null);
  const s: any = { width: "100%", marginBottom: "20px" };
  const [state, setState] = useState("");
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
          <h1>Voyce</h1>
        </header>
        <form className={style.form} onSubmit={onSubmit}>
          <header>
            <h2>Email Verification</h2>
            <p>Enter the code sent to your email to verify your account.</p>
          </header>

          <div>
            <InputText
              height={50}
              s={s}
              label="code"
              inputRef={inputTextRef}
              onChange={onChange}
              id="code"
              value={state}
            />
          </div>

          <footer>
            <Link href="/">
              <a>Resend code</a>
            </Link>
            <button type={loading ? "button" : "submit"}>
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
