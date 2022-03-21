import Image from "next/image";
import { RefObject, useState } from "react";

import style from "../styles/components/Inputs.module.sass";
import { PasswordIcon } from "./Button";

interface WrapperProps {
  label: string;
  children: any;
  s?: any;
}
export const Wrapper = ({ label, children, s }: WrapperProps): JSX.Element => (
  <div style={s} className={style.input__group}>
    {children}
    <label>{label}</label>
    <span>
      <i></i>
    </span>
  </div>
);

interface InputProps {
  label: string;
  inputRef?: RefObject<HTMLInputElement>;
  s?: any;
  height?: number;
  onChange?: any;
  id: string;
  value: string;
  autoComplete?: boolean;
}
export const InputText = ({
  label,
  inputRef,
  s,
  ...rest
}: InputProps): JSX.Element => {
  const inputStyle: any = { height: rest.height + "px" };
  return (
    <Wrapper label={label} s={s}>
      <input
        style={inputStyle}
        ref={inputRef}
        className={style.effect}
        required
        type="text"
        onChange={rest.onChange}
        id={rest.id}
        value={rest.value}
        autoComplete={rest.autoComplete}
      />
    </Wrapper>
  );
};

export const InputEmail = ({
  label,
  inputRef,
  s,
  ...rest
}: InputProps): JSX.Element => {
  const inputStyle: any = { height: rest.height + "px" };
  return (
    <Wrapper label={label} s={s}>
      <input
        style={inputStyle}
        ref={inputRef}
        className={style.effect}
        required
        type="email"
        onChange={rest.onChange}
        id={rest.id}
        value={rest.value}
      />
    </Wrapper>
  );
};

export const InputPassword = ({
  label,
  s,
  ...rest
}: InputProps): JSX.Element => {
  const [showPassword, setShowPassword] = useState(false);
  const inputStyle: any = { height: rest.height + "px" };

  return (
    <Wrapper label={label} s={s}>
      <input
        style={inputStyle}
        className={style.effect}
        required
        type={showPassword ? "text" : "password"}
        onChange={rest.onChange}
        value={rest.value}
        id={rest.id}
      />
      <PasswordIcon onClick={() => setShowPassword(!showPassword)}>
        <Image
          src={`/image/${showPassword ? "visibility_off" : "visibility"}.svg`}
          height={20}
          width={20}
          alt="Visibility"
        />
      </PasswordIcon>
    </Wrapper>
  );
};
