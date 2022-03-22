import Link from "next/link";
import workspaceStore from "../../store/workspace";

import style from "../../styles/components/dashboard/WorkspaceNav.module.sass";
import Spinner from "../Spinner";

const WorkspaceNav = (): JSX.Element => {
  const { workspace }: any = workspaceStore();

  return (
    <aside className={style.workspace__bar}>
      <header>
        <h3>
          {!workspace && <Spinner visible />}
          {workspace && workspace.name}
        </h3>
      </header>
      <ul>
        <li>
          <Link href="/workspace">
            <a className={[style.active__link].join(" ")}>
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
              <span>Translate</span>
            </a>
          </Link>
        </li>

        <li>
          <Link href="/workspace">
            <a className="active">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                enableBackground="new 0 0 24 24"
                height="18px"
                viewBox="0 0 24 24"
                width="18px"
                fill="#64676c"
              >
                <g>
                  <rect fill="none" height="24" width="24" />
                </g>
                <g>
                  <g>
                    <circle cx="10" cy="8" r="4" />
                    <path d="M10.35,14.01C7.62,13.91,2,15.27,2,18v2h9.54C9.07,17.24,10.31,14.11,10.35,14.01z" />
                    <path d="M19.43,18.02C19.79,17.43,20,16.74,20,16c0-2.21-1.79-4-4-4s-4,1.79-4,4c0,2.21,1.79,4,4,4c0.74,0,1.43-0.22,2.02-0.57 L20.59,22L22,20.59L19.43,18.02z M16,18c-1.1,0-2-0.9-2-2c0-1.1,0.9-2,2-2s2,0.9,2,2C18,17.1,17.1,18,16,18z" />
                  </g>
                </g>
              </svg>
              <span>Users</span>
            </a>
          </Link>
        </li>
      </ul>
    </aside>
  );
};

export default WorkspaceNav;
