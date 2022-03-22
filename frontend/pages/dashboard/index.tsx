/* eslint-disable react-hooks/exhaustive-deps */
import { NextPage } from "next";
import { useRouter } from "next/router";
import { useEffect } from "react";

const Dashboard: NextPage = () => {
  const router = useRouter();
  useEffect(() => {
    router.push("/workspace");
  }, []);
  return null;
};

export default Dashboard;
// /* eslint-disable react-hooks/exhaustive-deps */
// import { NextPage } from "next";
// import { useRouter } from "next/router";
// import Link from "next/link";
// import { FormEvent, useEffect, useRef, useState } from "react";

// import workspace from "../../api/workspace";
// import language from "../../api/language";
// import Alert from "../../components/Alert";
// import { InputText } from "../../components/Inputs";
// import Logo from "../../components/Logo";
// import SelectMenu from "../../components/SelectMenu";
// import Spinner from "../../components/Spinner";
// import useApi from "../../libs/useApi";
// import authStorage from "../../store";
// import style from "../../styles/pages/Dashboard.module.sass";
// import workspaceStore from "../../store/workspace";
// import Layout from "../../components/dashboard/Layout";

// const NewWorkspace: NextPage = () => {
//   const router = useRouter();
//   const { user, apiKey, getUser } = authStorage();
//   const { request, loading, status, data } = useApi(workspace.getUserWorkspace);
//   const { addWorkspace } = workspaceStore();

//   // Hooks
//   useEffect(() => {
//     request();
//   }, []);

//   useEffect(() => {
//     if (status == 200 && data) addWorkspace(data.data);
//   }, [data]);

//   useEffect(() => {
//     const user = getUser();
//     if (!user || !apiKey) router.push("/login");
//   }, [user]);

//   return (
//     <Layout workspaceNav={false}>
//       <main
//         className={style.dashboard}
//         style={{ minHeight: "100%", minWidth: "100%" }}
//       >
//         <div className={style.wrapper}>
//           <header>
//             <Logo />
//             <p>
//               A Voyce workspace is made up of teams, where members can
//               communicate and work together. <br /> When you join a workspace,
//               you&apos;ll be able to collaborate on that workspace.
//             </p>
//           </header>
//           <section className={style.workspace}>
//             <header>
//               <h3>Select a workspace.</h3>
//             </header>
//             <ul className={style.workspace__list}>
//               {loading && (
//                 <li style={{ pointerEvents: "none" }}>
//                   <p>loading...</p>
//                   <Link href="/workspace">
//                     <a title="Hello">
//                       <Spinner visible />
//                     </a>
//                   </Link>
//                 </li>
//               )}
//               {data &&
//                 data.data.map((workspace: any) => (
//                   <li key={workspace.id}>
//                     <p>{workspace.name}</p>
//                     <Link href={`/workspace/${workspace.id}`}>
//                       <a title={workspace.name}>
//                         <h1>{String(workspace.name).split("")[0]}</h1>
//                       </a>
//                     </Link>
//                   </li>
//                 ))}
//             </ul>
//             {user && (
//               <p style={{ textAlign: "left", marginTop: "4rem" }}>
//                 Hi {getUser().full_name.split(" ")[0]}! <br />
//                 Welcome to your Dashboard -:)
//               </p>
//             )}
//           </section>
//         </div>
//       </main>
//     </Layout>
//   );
// };

// export default NewWorkspace;
