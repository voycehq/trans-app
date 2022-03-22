/* eslint-disable react-hooks/exhaustive-deps */
import { useRouter } from "next/router";
import { FormEvent, useEffect, useRef, useState } from "react";
import workspace from "../../api/workspace";
import useApi from "../../libs/useApi";
import workspaceStore from "../../store/workspace";
import Alert from "../Alert";
import { InputText } from "../Inputs";
import SelectMenu from "../SelectMenu";
import Spinner from "../Spinner";

interface Props {
  options: [];
  inputRef: any;
  state: any;
  onSubmit: any;
  onChange: any;
  loading: any;
  onOptionChange: any;
  api: any;
}
const NewWorkspace = ({
  onSubmit,
  options,
  inputRef,
  state,
  onChange,
  loading,
  onOptionChange,
  api,
}: Props) => {
  // const router = useRouter();
  // const inputTextRef = useRef<HTMLInputElement>(null);
  // const [state, setState]: any = useState({
  //   name: "",
  //   default_language: null,
  // });

  // const handleOnChange = ({ target: { value } }: any) =>
  //   setState({ ...state, name: value });

  // const onLanguageChange = (arr: any) => {
  //   if (!arr) return setState({ ...state, default_language: arr });
  //   if (state.default_language && state.default_language.value == arr.value)
  //     return;

  //   setState({ ...state, default_language: arr });
  // };

  // const { request, loading, _private, data, status } = useApi(
  //   workspace.newWorkspace
  // );

  // const onSubmit = (event: FormEvent<HTMLFormElement>) => {
  //   event.preventDefault();
  //   if (state.default_language == null) {
  //     setTimeout(() => {
  //       _private._reset();
  //     }, 5000);
  //     _private._setError(true)._setMessage("Please select a defualt language");
  //     return;
  //   }
  //   request({
  //     name: state.name,
  //     default_language: state.default_language.value,
  //   });
  // };

  // useEffect(() => {
  //   if (status == 200 && data.data) addWorkspace(data.data);
  // }, [data]);
  return (
    <div>
      {api.status !== null && (
        <Alert
          className={api.error ? "danger" : "success"}
          visible={api.status !== null}
        >
          {api.message}
        </Alert>
      )}
      <form onSubmit={onSubmit}>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: ".5rem",
          }}
        >
          <InputText
            label="New workspace"
            id="name"
            value={state.name}
            inputRef={inputRef}
            onChange={onChange}
          />
          <SelectMenu
            id="translated_text"
            palceholder="Select default langue"
            onChange={onOptionChange}
            options={options}
            value={[state.default_language]}
            width="100%"
          />
        </div>
        <button type={loading ? "button" : "submit"}>
          {loading && <Spinner visible bgColor="#fff" />}
          {!loading && <span>Create workspace</span>}
        </button>
      </form>
    </div>
  );
};

export default NewWorkspace;
