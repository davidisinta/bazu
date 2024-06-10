import type { UUID } from "crypto";
import { WritableComputedRef } from "nuxt/dist/app/compat/capi";
declare global {
  export type UID = UUID;
  export interface Chats {
    id?: UUID|number;
    title: string;
    created_at: string;
    creator: string;
  }

}

export {};
