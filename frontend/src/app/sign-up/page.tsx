"use client";
import { FormEvent, useState } from "react";
import api from "@/lib/api";

export default function SignUpPage() {
  const [msg, setMsg] = useState("");

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const f = new FormData(e.currentTarget);
    const payload = {
      user_name: f.get("user_name"),
      user_email: f.get("user_email"),
      password: f.get("password"),
    };
    const res = await api.post("/auth/register", payload);
    localStorage.setItem("access_token", res.data.access_token);
    setMsg("Registered! Token saved. Go to Home.");
  }

  return (
    <form onSubmit={onSubmit} className="mx-auto max-w-md space-y-3 rounded border bg-white p-4">
      <h1 className="text-xl font-semibold">Sign Up</h1>
      <input name="user_name" placeholder="Name" className="w-full rounded border p-2" required />
      <input name="user_email" placeholder="Email" type="email" className="w-full rounded border p-2" required />
      <input name="password" placeholder="Password" type="password" className="w-full rounded border p-2" required />
      <button className="rounded bg-black px-3 py-2 text-white" type="submit">Create Account</button>
      {msg && <p className="text-green-700">{msg}</p>}
    </form>
  );
}