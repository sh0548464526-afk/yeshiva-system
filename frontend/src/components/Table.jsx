
import { useRef } from "react";

export default function Table({data,setData,editing}){

  const refs = useRef({});

  const move = (e,i,kIndex)=>{
    if(e.key==="ArrowDown") refs.current[`${i+1}-${kIndex}`]?.focus();
    if(e.key==="ArrowUp") refs.current[`${i-1}-${kIndex}`]?.focus();
    if(e.key==="ArrowRight") refs.current[`${i}-${kIndex+1}`]?.focus();
    if(e.key==="ArrowLeft") refs.current[`${i}-${kIndex-1}`]?.focus();
    if(e.key==="Enter") refs.current[`${i+1}-${kIndex}`]?.focus();
  };

  const update=(i,k,v)=>{
    let c=[...data];
    c[i][k]=v;
    setData(c);
  };

  const cols=["s1","s2","s3"];

  return (
    <table>
      <thead>
        <tr>
          <th>תז</th><th>יום</th>
          <th>ס1</th><th>ס2</th><th>ס3</th><th>סהכ</th>
        </tr>
      </thead>
      <tbody>
        {data.map((r,i)=>(
          <tr key={i}>
            <td>{r.tz}</td>
            <td>{r.day}</td>

            {cols.map((k,ki)=>(
              <td key={k}>
                {editing
                  ? <input
                      ref={el=>refs.current[`${i}-${ki}`]=el}
                      value={r[k]||""}
                      onKeyDown={e=>move(e,i,ki)}
                      onChange={e=>update(i,k,e.target.value)}
                    />
                  : r[k]}
              </td>
            ))}

            <td>{r.total}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
