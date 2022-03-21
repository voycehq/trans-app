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

      getUser: (): User => get().user,
      setUser: (user: User) => set((state: any) => ({ ...state, user })),
      updateUser: (data: any) => {
        const user: any = get().user;
        Object.keys(data).forEach((key: string) => {
          user[key] = data[key];
        });

        get().setUser(user);
      },
    }),
    { name: "voyce" }
  )
);

export default authStorage;
export const store = { authStorage };
