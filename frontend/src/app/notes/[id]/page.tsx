"use client";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import api from "@/lib/api";
import { useParams, useRouter } from "next/navigation";
import { FormEvent, useEffect, useState } from "react";

type NoteDetail = { note_title: string; note_content: string };

export default function NoteDetailPage() {
  const { id } = useParams<{ id: string }>();
  const qc = useQueryClient();
  const router = useRouter();
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const { data, isLoading, error } = useQuery({
    queryKey: ["note", id],
    queryFn: async () => (await api.get(/notes/${id})).data as NoteDetail,
  });

  useEffect(() => {
    if (data) {
      setTitle(data.note_title);
      setContent(data.note_content || "");
    }
  }, [data]);

  const update = useMutation({
    mutationFn: async () => {
      await api.put(/notes/${id}, { note_title: title, note_content: content });
    },
    onSuccess: () => qc.invalidateQueries({ queryKey: ["note", id] }),
  });

  const del = useMutation({
    mutationFn: async () => { await api.delete(/notes/${id}); },
    onSuccess: () => router.push("/"),
  });

  if (isLoading) return <p>Loading…</p>;
  if (error) return <p className="text-red-600">Failed to load note.</p>;

  return (
    <form className="mx-auto max-w-2xl space-y-3" onSubmit={(e: FormEvent) => { e.preventDefault(); update.mutate(); }}>
      <input value={title} onChange={(e)=>setTitle(e.target.value)} className="w-full rounded border p-2" />
      <textarea value={content} onChange={(e)=>setContent(e.target.value)} className="h-72 w-full rounded border p-2" />
      <div className="flex gap-2">
        <button className="rounded bg-black px-3 py-2 text-white" type="submit">Save</button>
        <button onClick={()=>del.mutate()} className="rounded border px-3 py-2" type="button">Delete</button>
      </div>
    </form>
  );
}