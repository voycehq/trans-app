import type { NextPage } from "next";
import Link from "next/link";

import style from "../styles/pages/Index.module.sass";

const Home: NextPage = () => {
  return (
    <div>
      <nav className={style.nav}>
        <div className={style.logo}>
          <h1>Voyce</h1>
        </div>

        <ul className={style.links}>
          <li>
            <a href="#">Watch demo</a>
          </li>
          <li>
            <Link href="/">
              <a>Sign up now</a>
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Home;
