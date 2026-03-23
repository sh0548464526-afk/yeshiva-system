async function loadData(){
    let res = await fetch("/api/students")
    let data = await res.json()

    let table = document.getElementById("table")
    table.innerHTML = ""

    data.forEach(row=>{
        let tr = "<tr><td>"+row[0]+"</td><td>"+row[1]+"</td></tr>"
        table.innerHTML += tr
    })
}

window.onload = loadData

document.addEventListener("input", function(e){
    if(e.target.id==="search"){
        let val = e.target.value.toLowerCase()
        document.querySelectorAll("#table tr").forEach(tr=>{
            tr.style.display = tr.innerText.toLowerCase().includes(val) ? "" : "none"
        })
    }
})
