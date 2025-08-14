"use client";
import { FormEvent } from "react";
import api from "@/lib/api";
import { useRouter } from "next/navigation";

export default function NewNotePage() {
  const router = useRouter();

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const f = new FormData(e.currentTarget);
    const payload = {
      note_title: f.get("note_title"),
      note_content: f.get("note_content") || "",
    };
    const res = await api.post("/notes", payload);
    router.push(/notes/${res.data.note_id});
  }

  return (
    <form onSubmit={onSubmit} className="mx-auto max-w-2xl space-y-3 rounded border bg-white p-4">
      <h1 className="text-xl font-semibold">New Note</h1>
      <input name="note_title" placeholder="Title" className="w-full rounded border p-2" required />
      <textarea name="note_content" placeholder="Write here…" className="h-60 w-full rounded border p-2"></textarea>
      <button className="rounded bg-black px-3 py-2 text-white" type="submit">Create</button>
    </form>
  );
}