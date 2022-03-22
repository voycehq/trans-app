/* eslint-disable react-hooks/exhaustive-deps */
import Image from "next/image";
import Link from "next/link";
import { useEffect } from "react";
import workspace from "../../api/workspace";
import useApi from "../../libs/useApi";
import workspaceStore from "../../store/workspace";

import style from "../../styles/components/dashboard/SideNav.module.sass";
import Spinner from "../Spinner";

const SideNav = (): JSX.Element => {
  const { request, loading, data } = useApi(workspace.getUserWorkspace);
  const { workspace: currentWorkspace }: any = workspaceStore();

  useEffect(() => {
    request();
  }, []);

  return (
    <aside className={style.aside__bar}>
      <ul>
        {loading && <Spinner visible bgColor="#fff" />}
        {data &&
          data.data &&
          data.data.map((workspace: any) => {
            let isActive: boolean = false;
            if (currentWorkspace && workspace.id == currentWorkspace.id) {
              isActive = workspace.id == currentWorkspace.id;
            }
            return (
              <li key={workspace.id}>
                <Link href={`/workspace/${workspace.id}`}>
                  <a
                    className={[isActive ? style.active__workspace : ""].join(
                      " "
                    )}
                  >
                    {String(workspace.name).split("")[0]}
                  </a>
                </Link>
              </li>
            );
          })}
        {/* <li>
          <button className={[style.active__workspace].join(" ")} type="button">
            P
          </button>
        </li>
        <li>
          <button type="button">A</button>
        </li> */}
        <li>
          <Link href="/workspace/new-workspace">
            <a>
              <Image
                src="/image/plus-icon.svg"
                height={25}
                width={25}
                alt="Plus Icon"
              />
            </a>
          </Link>
        </li>
      </ul>
    </aside>
  );
};

export default SideNav;
