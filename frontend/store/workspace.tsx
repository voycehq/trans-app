import create from "zustand/react";

const workspaceStore = create((set: any, get: any) => ({
  workspaces: [],

  // func
  setWorkspaces: (workspaces: []) =>
    set((state: any) => ({ ...state, workspaces })),
  addWorkspace: (workspace: any) => {
    const workspaces = [...get().workspace, workspace];
    set((state: any) => ({ ...state, workspaces }));
  },
}));

export default workspaceStore;
