import { useState } from "react";
import Dashboard from "./pages/Dashboard";
import Settings from "./pages/Settings";

export default function App(){

  const [page,setPage] = useState("home");

  return (
    <div>

      <div style={{marginBottom:"20px"}}>
        <button onClick={()=>setPage("home")}>ראשי</button>
        <button onClick={()=>setPage("settings")}>הגדרות</button>
      </div>

      {page==="home" && <Dashboard />}
      {page==="settings" && <Settings />}

    </div>
  );
}