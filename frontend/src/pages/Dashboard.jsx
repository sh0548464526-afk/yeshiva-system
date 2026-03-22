import {useEffect,useState} from "react";
import api from "../api";
import Table from "../components/Table";

export default function Dashboard(){

  const [data,setData]=useState([]);
  const [editing,setEditing]=useState(false);

  const load=async()=>{
    let r=await api.get("/attendance/full");
    setData(r.data);
  };

  useEffect(()=>{load();},[]);

  const save=async()=>{
    await api.post("/attendance",data);
    setEditing(false);
    load();
  };

  return (
    <div>

      <h1>מערכת ישיבת בין הזמנים</h1>

      <button onClick={()=>setEditing(true)}>ערוך</button>
      <button onClick={save}>שמור</button>
      <button onClick={()=>window.open("/export")}>אקסל</button>

      <Table data={data} setData={setData} editing={editing} />

    </div>
  );
}