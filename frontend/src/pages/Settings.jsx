import { useState } from "react";

export default function Settings(){

  const [students,setStudents]=useState([]);

  const add=()=>{
    setStudents([...students,{tz:"",name:""}]);
  };

  return (
    <div>

      <h2>ניהול תלמידים</h2>

      <button onClick={add}>הוסף</button>

      <table>
        <thead>
          <tr><th>תז</th><th>שם</th></tr>
        </thead>

        <tbody>
          {students.map((s,i)=>(
            <tr key={i}>
              <td>
                <input
                  value={s.tz}
                  onChange={e=>{
                    let c=[...students];
                    c[i].tz=e.target.value;
                    setStudents(c);
                  }}
                />
              </td>

              <td>
                <input
                  value={s.name}
                  onChange={e=>{
                    let c=[...students];
                    c[i].name=e.target.value;
                    setStudents(c);
                  }}
                />
              </td>
            </tr>
          ))}
        </tbody>

      </table>

    </div>
  );
}