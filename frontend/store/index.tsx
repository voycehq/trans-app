import create from "zustand";
import { persist } from "zustand/middleware";

const appStore = create(
  persist((set: any, get: any) => ({}), { name: "voyce" })
);

export default appStore;
export const store = {};
