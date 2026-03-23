
import { useEffect, useState } from "react";
import api from "../api";
import Table from "../components/Table";

export default function Dashboard(){

  const [data,setData]=useState([]);
  const [editing,setEditing]=useState(false);
  const [search,setSearch]=useState("");
  const [day,setDay]=useState("");

  const load=async()=>{
    let r=await api.get("/attendance/full");
    setData(r.data);
  };

  useEffect(()=>{load();},[]);

  const filtered = data.filter(r =>
    (r.tz.includes(search) || r.day.includes(search)) &&
    (day==="" || r.day===day)
  );

  return (
    <div>
      <h1>מערכת ישיבת בין הזמנים</h1>

      <input placeholder="חיפוש..." onChange={e=>setSearch(e.target.value)} />

      <select onChange={e=>setDay(e.target.value)}>
        <option value="">ללא סינון</option>
        <option>א</option><option>ב</option><option>ג</option>
        <option>ד</option><option>ה</option><option>ו</option>
      </select>

      <button onClick={()=>setEditing(true)}>ערוך</button>

      <button onClick={async()=>{
        await api.post("/attendance", data);
        setEditing(false);
        load();
      }}>שמור</button>

      <button onClick={()=>window.print()}>הדפס</button>

      <button onClick={()=>window.open(api.defaults.baseURL+"/export")}>
        אקסל
      </button>

      <Table data={filtered} setData={setData} editing={editing}/>
    </div>
  );
}
