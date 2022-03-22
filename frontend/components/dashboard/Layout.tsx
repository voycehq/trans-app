import Nav from "./Nav";
import SideNav from "./SideNav";
import WorkspaceNav from "./WorkspaceNav";
import style from "../../styles/components/dashboard/Layout.module.sass";

interface Props {
  children: any;
  workspaceNav?: boolean;
  sideNav?: boolean;
}
const Layout = ({
  children,
  workspaceNav = true,
  sideNav = true,
}: Props): JSX.Element => {
  return (
    <main className={style.main__dashboard}>
      <Nav />
      <main className={style.dashboard__container}>
        {sideNav && <SideNav />}
        {workspaceNav && <WorkspaceNav />}
        <section className={style.body__content}>{children}</section>
        <div className={style.audio__container}>
          <audio controls>
            <source src="hey.mp3" type="audio/mpeg" />
            Your browser does not support the audio element.
          </audio>
        </div>
      </main>
    </main>
  );
};

export default Layout;
