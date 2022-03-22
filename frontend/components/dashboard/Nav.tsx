import Logo from "../Logo";
import style from "../../styles/components/dashboard/Nav.module.sass";
import Link from "next/link";
import authStorage from "../../store";

const Nav = (): JSX.Element => {
  const { logout } = authStorage();
  return (
    <nav className={style.top__nav}>
      <Logo to="/workspace" />
      <ul>
        <li>Help</li>
        <li>Profile</li>
        <li>
          <Link href="/">
            <a onClick={logout}>Logout</a>
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Nav;
