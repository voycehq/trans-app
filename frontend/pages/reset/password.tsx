import { NextPage } from "next";
import Link from "next/link";
import { FormEvent, useRef, useState } from "react";

import { InputEmail, InputPassword, InputText } from "../../components/Inputs";
import Logo from "../../components/Logo";
import Spinner from "../../components/Spinner";
import style from "../../styles/pages/Login.module.sass";

const Signup: NextPage = () => {
  const inputTextRef = useRef<HTMLInputElement>(null);
  const s: any = { width: "100%", marginBottom: "20px" };
  const [state, setState] = useState({
    password: "",
    code: "",
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
            <h2>Password Reset</h2>
            <p>
              Enter the code sent to your email <br /> and a new password to
              reset your account password.
            </p>
          </header>

          <div>
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
            {/* Checkbox about agreement to privacy policy */}
            <span></span>

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
