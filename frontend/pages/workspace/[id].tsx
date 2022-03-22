/* eslint-disable react-hooks/exhaustive-deps */
import { NextPage } from "next";
import { useEffect, useState } from "react";
import workspace from "../../api/workspace";
import Layout from "../../components/dashboard/Layout";
import SelectMenu from "../../components/SelectMenu";
import useApi from "../../libs/useApi";
import workspaceStore from "../../store/workspace";
import style from "../../styles/pages/Workspace.module.sass";

const textOption = [
  { value: "english", label: "English" },
  { value: "french", label: "French" },
  { value: "spanish", label: "Spanish" },
];
const WorkspaceDetails: NextPage = ({ workspaceId }: any) => {
  const { request, loading, status, data } = useApi(workspace.getWorkspaceById);
  const { setWorkspace } = workspaceStore();

  const [state, setState] = useState([{ value: "english", label: "English" }]);
  const [outputText, setOutputText] = useState([
    { value: "french", label: "French" },
  ]);
  const handleSelectChange = (arr: any) => setState([arr]);
  const onOutputChange = (arr: any) => {
    if (state[0].value == arr.value) return;
    setOutputText([arr]);
  };

  useEffect(() => {
    setOutputText([textOption.filter((ele) => ele.value != state[0].value)[0]]);
  }, [state]);

  useEffect(() => {
    request(workspaceId);
  }, []);

  useEffect(() => {
    if (data && status == 200) setWorkspace(data.data);
  }, [data]);
  return (
    <Layout>
      <section className={style.body__content}>
        <header>
          <div>
            <SelectMenu
              id="text"
              onChange={handleSelectChange}
              options={textOption}
              value={state}
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
              options={textOption}
              value={outputText}
            />
          </div>
        </header>
        <main>
          <textarea
            placeholder="Type to translate"
            name="original"
            id="text"
          ></textarea>
          <div>
            <button title="Translate" type="button">
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
            </button>
          </div>
          <textarea name="translated_text" id="translated_text"></textarea>
        </main>
      </section>
    </Layout>
  );
};

export const getServerSideProps = (context: any) => {
  return {
    props: {
      workspaceId: context.params.id,
    },
  };
};
export default WorkspaceDetails;
