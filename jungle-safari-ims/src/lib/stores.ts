import { readable, writable } from "svelte/store";
import type { User } from "./types"; 
import { load, Store } from "@tauri-apps/plugin-store";

let store: Store;
load("store.json", {autoSave: true}).then((val) => {
    store = val
    store.get<{ value: User | undefined }>("user").then(val => user.set(val?.value))
})

export const current = writable<string>()
export const page = writable<string>("analysis")

export const user = writable<User | undefined>(undefined)

user.subscribe(async (val) => {
    
  if (!val) {
    current.set("login")
  } else if (!val.store) {
    current.set("store-select")
  } else {
    current.set("default")
  }

    await store.set('user', { value: undefined })
    await store.save()
})


export const api_url = readable("http://172.16.204.89:8000")

