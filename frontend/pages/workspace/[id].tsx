/* eslint-disable react-hooks/exhaustive-deps */
import { NextPage } from "next";
import { FormEvent, useEffect, useState } from "react";
import audio from "../../api/audio";
import language from "../../api/language";
import translation from "../../api/translation";
import workspace from "../../api/workspace";
import Layout from "../../components/dashboard/Layout";
import SelectMenu from "../../components/SelectMenu";
import Spinner from "../../components/Spinner";
import useApi from "../../libs/useApi";
import { colors } from "../../libs/utils";
import workspaceStore from "../../store/workspace";
import style from "../../styles/pages/Workspace.module.sass";

const WorkspaceDetails: NextPage = ({ workspaceId, languages }: any) => {
  const translationApi = useApi(translation.oneToone);
  const { request, status, data } = useApi(workspace.getWorkspaceById);
  const audioApi = useApi(audio.oneToMany);
  const {
    setWorkspace,
    setTextAndTransText,
    text: textObject,
    translatedText,
    setAudio,
    audio: audioObject,
  }: any = workspaceStore();
  const [text, setText] = useState({
    raw_text: "",
    translation_text: "",
  });

  const [state, setState]: any = useState([{ value: "en", label: "English" }]);
  const [outputText, setOutputText]: any = useState([
    { value: "fr", label: "French" },
  ]);
  const handleSelectChange = (arr: any) => setState([arr]);
  const onOutputChange = (arr: any) => {
    if (state[0].value == arr.value) return;
    setOutputText([arr]);
  };

  const onChange = ({ target: { value, id } }: any) =>
    setText({ ...text, [id]: value });
  const onSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const data = {
      workspace_id: workspaceId,
      raw_text: text.raw_text,
      raw_text_language_id: state[0].id,
      translation_text_language_id: outputText[0].id,
    };

    // Translate user input
    translationApi.request(data).then((res: any) => {
      const data = res.data.data;
      setTextAndTransText(data.text, data.translation[0]);
      setText({ ...text, translation_text: data.translation[0].body });
    });
  };

  // Audio
  const onGetAudio = () => {
    const data = {
      raw_text_id: textObject.id,
      workspace_id: workspaceId,
      raw_text: text.raw_text,
      raw_text_language_id: state[0].id,
      translation_text_id: translatedText.id,
      translation_text: translatedText.body,
      translation_text_language_id: outputText[0].id,
    };
    audioApi.request(data).then((res) => {
      console.log(res.data);
      setAudio(res.data.data);
    });
  };

  useEffect(() => {
    setOutputText([
      languages.filter((ele: any) => ele.value != state[0].value)[0],
    ]);
  }, [state]);

  useEffect(() => {
    request(workspaceId).then((res) => {
      const data: any = res.data.data;
      const defaultLanguage = languages.filter(
        (lang: any) => lang.id == data.default_language
      );

      setState(defaultLanguage);
    });
  }, [workspaceId]);

  useEffect(() => {
    if (data && status == 200) setWorkspace(data.data);
  }, [data]);

  useEffect(() => {
    console.log(audioObject);
  }, [audioObject]);

  return (
    <Layout>
      <section className={style.body__content}>
        <header>
          <div>
            <SelectMenu
              id="text"
              onChange={handleSelectChange}
              options={languages}
              value={state}
              isClearable={false}
            />
          </div>
          <span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              height="24px"
              viewBox="0 0 24 24"
              width="24px"
              fill="#64676c"
            >
              <path d="M0 0h24v24H0z" fill="none" />
              <path d="M16.01 11H4v2h12.01v3L20 12l-3.99-4z" />
            </svg>
          </span>
          <div>
            <SelectMenu
              id="translated_text"
              onChange={onOutputChange}
              options={languages}
              value={outputText}
              isClearable={false}
            />
          </div>

          {!translationApi.loading && translatedText && (
            <button disabled={audioApi.loading} onClick={onGetAudio}>
              {audioApi.loading && (
                <Spinner visible bgColor={colors.white_color} />
              )}
              <svg
                xmlns="http://www.w3.org/2000/svg"
                height="17px"
                viewBox="0 0 24 24"
                width="17px"
                fill="#FFFFFF"
              >
                <path d="M0 0h24v24H0z" fill="none" />
                <path d="M7 18h2V6H7v12zm4 4h2V2h-2v20zm-8-8h2v-4H3v4zm12 4h2V6h-2v12zm4-8v4h2v-4h-2z" />
              </svg>
              <span>Generate audio</span>
            </button>
          )}
        </header>

        <form onSubmit={onSubmit}>
          <textarea
            placeholder="Type to translate"
            name="original"
            id="raw_text"
            value={text.raw_text}
            onChange={onChange}
            required
          ></textarea>
          <div>
            <button
              title="Translate"
              type={translationApi.loading ? "button" : "submit"}
            >
              {translationApi.loading && (
                <Spinner visible bgColor={colors.white_color} />
              )}
              {!translationApi.loading && (
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  height="18px"
                  viewBox="0 0 24 24"
                  width="18px"
                  fill="#64676c"
                >
                  <path d="M21 4H11l-1-3H3c-1.1 0-2 .9-2 2v15c0 1.1.9 2 2 2h8l1 3h9c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zM7 16c-2.76 0-5-2.24-5-5s2.24-5 5-5c1.35 0 2.48.5 3.35 1.3L9.03 8.57c-.38-.36-1.04-.78-2.03-.78-1.74 0-3.15 1.44-3.15 3.21S5.26 14.21 7 14.21c2.01 0 2.84-1.44 2.92-2.41H7v-1.71h4.68c.07.31.12.61.12 1.02C11.8 13.97 9.89 16 7 16zm6.17-5.42h3.7c-.43 1.25-1.11 2.43-2.05 3.47-.31-.35-.6-.72-.86-1.1l-.79-2.37zm8.33 9.92c0 .55-.45 1-1 1H14l2-2.5-1.04-3.1 3.1 3.1.92-.92-3.3-3.25.02-.02c1.13-1.25 1.93-2.69 2.4-4.22H20v-1.3h-4.53V8h-1.29v1.29h-1.44L11.46 5.5h9.04c.55 0 1 .45 1 1v14z" />
                  <path d="M0 0h24v24H0zm0 0h24v24H0z" fill="none" />
                </svg>
              )}
            </button>
          </div>
          <textarea
            name="translated_text"
            placeholder="Click the translate button"
            id="translation_text"
            value={text.translation_text}
            onChange={onChange}
            readOnly
          ></textarea>
        </form>
      </section>
    </Layout>
  );
};

export const getServerSideProps = async (context: any) => {
  const response: any = await (await language.fetchLangauges()).data;
  const languages = response.data.map((language: any) => {
    return {
      id: language.id,
      label: language.name,
      value: language.code,
      html_code: language.html_code,
      created_on: language.created_on,
      updated_on: language.updated_on,
      deleted_on: language.deleted_on,
    };
  });
  return {
    props: {
      workspaceId: context.params.id,
      languages,
    },
  };
};
export default WorkspaceDetails;
