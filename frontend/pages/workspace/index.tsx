/* eslint-disable react-hooks/exhaustive-deps */
import { NextPage } from "next";
import { useRouter } from "next/router";
import Link from "next/link";
import { FormEvent, useEffect, useRef, useState } from "react";

import workspace from "../../api/workspace";
import language from "../../api/language";
import Logo from "../../components/Logo";
import Spinner from "../../components/Spinner";
import useApi from "../../libs/useApi";
import authStorage from "../../store";
import style from "../../styles/pages/Dashboard.module.sass";
import workspaceStore from "../../store/workspace";
import Layout from "../../components/dashboard/Layout";
import NewWorkspace from "../../components/dashboard/NewWorkspace";

const Workspace: NextPage = ({ languages }: any) => {
  const router = useRouter();
  const { user, apiKey, getUser } = authStorage();
  const { request, loading, status, data } = useApi(workspace.getUserWorkspace);
  const { addWorkspace } = workspaceStore();

  // New Workspace
  const inputTextRef = useRef<HTMLInputElement>(null);
  const [state, setState]: any = useState({
    name: "",
    default_language: null,
  });

  const handleOnChange = ({ target: { value } }: any) =>
    setState({ ...state, name: value });

  const onLanguageChange = (arr: any) => {
    if (!arr) return setState({ ...state, default_language: arr });
    if (state.default_language && state.default_language.value == arr.value)
      return;

    setState({ ...state, default_language: arr });
  };

  const workspaceApi = useApi(workspace.newWorkspace);

  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (state.default_language == null) {
      setTimeout(() => {
        workspaceApi._private._reset();
      }, 5000);
      workspaceApi._private
        ._setError(true)
        ._setStatus(400)
        ._setMessage("Please select a defualt language");
      return;
    }
    workspaceApi
      .request({
        name: state.name,
        default_language: state.default_language.value,
      })
      .then((response) => {
        request();
      });
  };

  // Hooks
  useEffect(() => {
    request();
    inputTextRef.current?.focus();
  }, []);

  useEffect(() => {
    if (status == 200 && data) {
      if (data.data) return addWorkspace(data.data);
    }
  }, [data]);

  useEffect(() => {
    const user = getUser();
    if (!user || !apiKey) router.push("/login");
  }, [user]);

  useEffect(() => {
    if (workspaceApi.status == 200 && workspaceApi.data.data)
      addWorkspace(workspaceApi.data.data);
  }, [workspaceApi.data]);

  return (
    <Layout workspaceNav={false} sideNav={false}>
      <main className={style.dashboard}>
        <div className={style.wrapper}>
          <header>
            <Logo />
            <p>
              A Voyce workspace is made up of teams, where members can
              communicate and work together. <br /> When you join a workspace,
              you&apos;ll be able to collaborate on that workspace.
            </p>
          </header>
          <section className={style.workspace}>
            <header>
              {!loading && data && !data.data ? (
                <h3>Creat workspace to continue.</h3>
              ) : (
                <h3>Select a workspace.</h3>
              )}
            </header>
            <ul className={style.workspace__list}>
              {!loading && data && !data.data && (
                <NewWorkspace
                  inputRef={inputTextRef}
                  api={workspaceApi}
                  state={state}
                  onSubmit={onSubmit}
                  onChange={handleOnChange}
                  onOptionChange={onLanguageChange}
                  loading={workspaceApi.loading}
                  options={languages}
                />
              )}
              {loading && (
                <li style={{ pointerEvents: "none" }}>
                  <p>loading...</p>
                  <Link href="/workspace">
                    <a title="Hello">
                      <Spinner visible />
                    </a>
                  </Link>
                </li>
              )}

              {data &&
                data.data &&
                data.data.map((workspace: any) => (
                  <li key={workspace.id}>
                    <p>{workspace.name}</p>
                    <Link href={`/workspace/${workspace.id}`}>
                      <a title={workspace.name}>
                        <h1>{String(workspace.name).split("")[0]}</h1>
                      </a>
                    </Link>
                  </li>
                ))}
            </ul>
            {/* {user && (
              <p style={{ textAlign: "left", marginTop: "4rem" }}>
                Hi {getUser().full_name.split(" ")[0]} {"!"} <br />
                Welcome to your Dashboard -:)
              </p>
            )} */}
          </section>
        </div>
      </main>
    </Layout>
  );
};

export const getServerSideProps = async () => {
  const response: any = await language.fetchLangauges();

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

export default Workspace;
