export default function Modal({open,children,onClose}){

  if(!open) return null;

  return (
    <div style={{
      position:"fixed",
      top:0,left:0,right:0,bottom:0,
      background:"rgba(0,0,0,0.5)"
    }}>

      <div style={{
        background:"#fff",
        margin:"100px auto",
        padding:"20px",
        width:"300px"
      }}>
        {children}
        <button onClick={onClose}>סגור</button>
      </div>

    </div>
  );
}