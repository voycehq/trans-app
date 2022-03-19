import style from "../styles/components/Button.module.sass";

interface Props {
  children: any;
  onClick: any;
}
const IconButton = ({ children, onClick }: Props): JSX.Element => {
  return (
    <div onClick={onClick} className={style.icon__button}>
      {children}
    </div>
  );
};

export const PasswordIcon = ({ children, onClick }: Props): JSX.Element => {
  return (
    <div onClick={onClick} className={style.password__visibility}>
      {children}
    </div>
  );
};

export default IconButton;
