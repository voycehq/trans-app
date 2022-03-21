import type { NextPage } from "next";
import Image from "next/image";
import Link from "next/link";
import Logo from "../components/Logo";

import style from "../styles/pages/Index.module.sass";

const Home: NextPage = () => {
  return (
    <div>
      <nav className={style.nav}>
        <div className={style.logo}>
          <Logo />
        </div>

        <ul className={style.links}>
          <li>
            <Link href="/login">
              <a>Login</a>
            </Link>
          </li>
          <li>
            <Link href="/signup">
              <a>Sign up now</a>
            </Link>
          </li>
        </ul>
      </nav>

      <section className={style.hero}>
        <div className={style.hero__content}>
          <h2>The smartest Trans-Voicer yet.</h2>
          <p>
            Instantly transform text into audio so that you can share, <br />{" "}
            delete, and sell your translated audio. It&rsquo;s fast, it&rsquo;s
            easy, and it&rsquo;s <br /> always online.*
          </p>
          <Link href="/">
            <a>
              Watch demo{" "}
              <Image src="/image/play-icon.svg" height={20} width={20} alt="" />
            </a>
          </Link>
        </div>

        <div className={style.image__wrapper}>
          <div className={style.image__item}>
            <Image
              src="/image/dashboard-one.png"
              alt=""
              width={1516}
              height={948}
            />
          </div>
          <div className={style.divider}></div>
          <div className={style.image__item}>
            <Image
              src="/image/dashboard-two.png"
              alt=""
              width={1516}
              height={948}
            />
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
