import create from "zustand";

const workspaceStore = create((set: any, get: any) => ({
  workspaces: [],
  workspace: null,

  // func
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
