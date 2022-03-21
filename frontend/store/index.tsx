import create from "zustand";
import { persist } from "zustand/middleware";

export interface User {
  id: number;
  date_id: number;
  email: string;
  full_name: string;
  is_verified: boolean;
  deleted_on?: string;
  created_on?: string;
  updated_on?: string;
}

const authStorage = create(
  persist(
    (set: any, get: any) => ({
      apiKey: null,
      user: null,

      // func
      getApiKey: (): string => get().apiKey,
      setApiKey: (apiKey: string) =>
        set((state: any) => ({ ...state, apiKey })),

      setUser: (user: User) => set((state: any) => ({ ...state, user })),
      getUser: (): User => get().user,
    }),
    { name: "voyce" }
  )
);

export default authStorage;
export const store = { authStorage };
