import { useState } from "react";

export default function Login({onLogin}){

  const [u,setU]=useState("");
  const [p,setP]=useState("");

  return (
    <div>
      <h2>כניסה</h2>

      <input placeholder="משתמש" onChange={e=>setU(e.target.value)} />
      <input type="password" onChange={e=>setP(e.target.value)} />

      <button onClick={onLogin}>כניסה</button>
    </div>
  );
}