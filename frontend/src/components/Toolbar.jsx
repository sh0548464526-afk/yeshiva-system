export default function Toolbar({onSearch}){

  return (
    <input
      placeholder="חיפוש..."
      onChange={e=>onSearch(e.target.value)}
      style={{marginBottom:"10px"}}
    />
  );
}