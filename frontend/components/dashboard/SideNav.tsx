import Image from "next/image";
import Link from "next/link";

import style from "../../styles/components/dashboard/SideNav.module.sass";

const SideNav = (): JSX.Element => {
  return (
    <aside className={style.aside__bar}>
      <ul>
        <li>
          <button className={[style.active__workspace].join(" ")} type="button">
            P
          </button>
        </li>
        <li>
          <button type="button">A</button>
        </li>
        <li>
          <Link href="/dashboard/workspace/new-workspace">
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
