export default function Table({data,setData,editing}){

  const update=(i,k,v)=>{
    let c=[...data];
    c[i][k]=v;
    setData(c);
  };

  return (
    <table>
      <thead>
        <tr>
          <th>תז</th><th>יום</th>
          <th>ס1</th><th>ס2</th><th>ס3</th>
          <th>סהכ</th>
        </tr>
      </thead>
      <tbody>
        {data.map((r,i)=>(
          <tr key={i}>
            <td>{r.tz}</td>
            <td>{r.day}</td>

            {["s1","s2","s3"].map(k=>(
              <td key={k}>
                {editing
                  ? <input value={r[k]||""}
                      onChange={e=>update(i,k,e.target.value)} />
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