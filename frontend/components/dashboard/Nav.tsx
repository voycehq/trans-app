import Logo from "../Logo";
import style from "../../styles/components/dashboard/Nav.module.sass";

const Nav = (): JSX.Element => {
  return (
    <nav className={style.top__nav}>
      <Logo to="/dashboard" />
      <ul>
        <li>Help</li>
        <li>Profile</li>
      </ul>
    </nav>
  );
};

export default Nav;
