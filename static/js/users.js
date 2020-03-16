$(document).ready(function()
{
	var token = '{%csrf_token%}';
	$.ajax({
       url: "data/",
       type: 'GET',
       dataType: 'json',
       headers:{
        "X-CSRFToken":token
       },
       contentType: "application/json",
       success:function(data)
       {
       let orders = data.orders;
       create_table(orders);

     }});
})
function create_table(orders){
  let table =  document.querySelector("#table_private");
  for(let order of orders){
      let tr = document.createElement("tr");
       for(let key of Object.keys(order))
       {
        let td = document.createElement("td");
        td.innerHTML = order[key];
        td.setAttribute("data-label",key);
        tr.appendChild(td);
       }
       let td = document.createElement("td");
       let a = document.createElement("a");
       a.href="https://wa.me/"+order["Номер курьера"]+"?text=Я%20заинтересован%20в%20услугах%20вашей%20фирмы"
       a.innerHTML=" WhatsApp"
       td.appendChild(a)
       tr.appendChild(td)
       let cancel = document.createElement("a")
       let td_cancel = document.createElement("td")
       console.log(order['Статус'])
       if(order["Статус"]==="Ожидание"){
        cancel.innerHTML="Отменить"
         cancel.href="remove_order/"+order["id"]+"/"
      }
      else{
    
          cancel.innerHTML="Вы не можете отменить заказ"
       

      }
      td_cancel.appendChild(cancel)
       tr.appendChild(td_cancel)
       table.appendChild(tr);
     }
}
