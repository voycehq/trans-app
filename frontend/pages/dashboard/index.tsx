import { NextPage } from "next";
import { FormEvent, useEffect, useRef, useState } from "react";

import { InputText } from "../../components/Inputs";
import Logo from "../../components/Logo";
import Spinner from "../../components/Spinner";
import style from "../../styles/pages/Dashboard.module.sass";

const Home: NextPage = () => {
  const inputTextRef = useRef<HTMLInputElement>(null);
  const [state, setState] = useState({ name: "" });
  const [loading, setLoading] = useState(false);

  const handleOnChange = ({ target: { value } }: any) =>
    setState({ name: value });

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setLoading(!loading);
    console.log(state);
  };

  useEffect(() => inputTextRef.current?.focus(), []);

  return (
    <main className={style.dashboard}>
      <div className={style.wrapper}>
        <header>
          <Logo />
          <p>
            A Voyce workspace is made up of teams, where members can communicate
            and work together. <br /> When you join a workspace, you&apos;ll be
            able to collaborate on that workspace.
          </p>
        </header>
        <section className={style.workspace}>
          <header>
            <h3>Create a workspace</h3>
          </header>
          <form onSubmit={onSubmit}>
            <InputText
              label="New workspace"
              id="name"
              value={state.name}
              inputRef={inputTextRef}
              onChange={handleOnChange}
            />
            <button type={loading ? "button" : "submit"}>
              {loading && <Spinner visible bgColor="#fff" />}
              {!loading && <span>Sign in</span>}
            </button>
          </form>
          <p style={{ textAlign: "left", marginTop: "4rem" }}>
            Hi Raymon! <br />
            Welcome to your dashboard.
          </p>
        </section>
      </div>
    </main>
  );
};

export default Home;
