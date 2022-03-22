import Nav from "./Nav";
import SideNav from "./SideNav";
import WorkspaceNav from "./WorkspaceNav";
import style from "../../styles/components/dashboard/Layout.module.sass";
import workspaceStore from "../../store/workspace";

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
  const { audio } = workspaceStore();

  const styles = { width: "26rem", padding: "1rem" };

  return (
    <main className={style.main__dashboard}>
      <Nav />
      <main className={style.dashboard__container}>
        {sideNav && <SideNav />}
        {workspaceNav && <WorkspaceNav />}
        <section className={style.body__content}>{children}</section>
        <div
          style={audio.length ? styles : {}}
          className={style.audio__container}
        >
          {audio &&
            audio.map((audioLink: string) => {
              return (
                <audio key={audioLink} controls>
                  <source src={audioLink} type="audio/mpeg" />
                  Your browser does not support the audio element.
                </audio>
              );
            })}
        </div>
      </main>
    </main>
  );
};

export default Layout;
