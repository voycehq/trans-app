/* eslint-disable react-hooks/exhaustive-deps */
import { NextPage } from "next";
import { useRouter } from "next/router";
import { FormEvent, useEffect, useRef, useState } from "react";

import workspace from "../../../api/workspace";
import language from "../../../api/language";
import Alert from "../../../components/Alert";
import { InputText } from "../../../components/Inputs";
import Logo from "../../../components/Logo";
import SelectMenu from "../../../components/SelectMenu";
import Spinner from "../../../components/Spinner";
import useApi from "../../../libs/useApi";
import authStorage from "../../../store";
import style from "../../../styles/pages/Dashboard.module.sass";

const NewWorkspace: NextPage = ({ languages }: any) => {
  const router = useRouter();
  const inputTextRef = useRef<HTMLInputElement>(null);
  const [state, setState]: any = useState({
    name: "",
    default_language: null,
  });
  const { setUser, user, apiKey, getUser } = authStorage();
  const { request, loading, error, message, status, data, _private } = useApi(
    workspace.newWorkspace
  );

  const handleOnChange = ({ target: { value } }: any) =>
    setState({ ...state, name: value });

  const onLanguageChange = (arr: any) => {
    if (!arr) return setState({ ...state, default_language: arr });
    if (state.default_language && state.default_language.value == arr.value)
      return;

    setState({ ...state, default_language: arr });
  };

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (state.default_language == null) {
      setTimeout(() => {
        _private._reset();
      }, 5000);
      _private._setError(true)._setMessage("Please select a defualt language");
      return;
    }
    request({
      name: state.name,
      default_language: state.default_language.value,
    });
  };

  // Hooks
  useEffect(() => inputTextRef.current?.focus(), []);

  useEffect(() => {
    if (status == 200 && data) console.log(data);
  }, [data]);

  useEffect(() => {
    const user = getUser();
    if (!user || !apiKey) router.push("/login");
  }, [user]);

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
          {error && (
            <Alert className={error ? "danger" : "success"} visible={error}>
              {message}
            </Alert>
          )}
          <form onSubmit={onSubmit}>
            <div
              style={{ display: "flex", flexDirection: "column", gap: ".5rem" }}
            >
              <InputText
                label="New workspace"
                id="name"
                value={state.name}
                inputRef={inputTextRef}
                onChange={handleOnChange}
              />
              <SelectMenu
                id="translated_text"
                palceholder="Select default langue"
                onChange={onLanguageChange}
                options={languages}
                value={[state.default_language]}
                width="100%"
              />
            </div>
            <button type={loading ? "button" : "submit"}>
              {loading && <Spinner visible bgColor="#fff" />}
              {!loading && <span>Create workspace</span>}
            </button>
          </form>
          <p style={{ textAlign: "left", marginTop: "4rem" }}>
            Hi {getUser().full_name.split(" ")[0]}! <br />
            Waving you greetings
          </p>
        </section>
      </div>
    </main>
  );
};

export const getStaticProps = async () => {
  const response: any = await language.fetchLangauges(
    authStorage.getState().getApiKey()
  );

  const languages = response.data.data.map((language: any) => ({
    id: language.id,
    label: language.name,
    value: language.code,
    html_code: language.html_code,
    created_on: language.created_on,
    updated_on: language.updated_on,
    deleted_on: language.deleted_on,
  }));

  return {
    props: { languages: languages },
  };
};

export default NewWorkspace;
