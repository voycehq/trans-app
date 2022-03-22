import create from "zustand";

const workspaceStore = create((set: any, get: any) => ({
  workspaces: [],
  workspace: null,
  text: null,
  translatedText: null,
  audio: [],

  // func
  setText: (text: any) => set((state: any) => ({ ...state, text })),
  setAudio: (audio: any) => set((state: any) => ({ ...state, audio })),
  setTranlatedText: (text: any) =>
    set((state: any) => ({ ...state, translatedText: text })),

  setTextAndTransText: (text: any, transText: any) =>
    set((state: any) => ({ ...state, text, translatedText: transText })),

  delText: () => set((state: any) => ({ ...state, text: null })),
  setWorkspace: (workspace: any) =>
    set((state: any) => ({ ...state, workspace })),

  setWorkspaces: (workspaces: []) =>
    set((state: any) => ({ ...state, workspaces })),

  addWorkspace: (workspace: any) => {
    const workspaces = [...get().workspaces, workspace];
    set((state: any) => ({ ...state, workspaces }));
  },
}));

export default workspaceStore;
