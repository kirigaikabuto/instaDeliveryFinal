$(document).ready(function() {

    var statuses = document.querySelectorAll(".statuses");
    for (var i = 0; i < statuses.length; i++) {

        statuses[i].addEventListener("change", function() {
            object = {
                id: this.id,
                value: this.value
            }
            console.log(object)
            var token = '{%csrf_token%}';
            $.ajax({
                url: "status/change/",
                type: 'post',
                dataType: 'json',
                headers: {
                    "X-CSRFToken": token
                },
                contentType: "application/json",
                data: JSON.stringify(object),
                success: function(data) {
                    console.log(data.message)
                    create_table();
                }
            })
        });


    }
    var table_empty = document.querySelector("#table_empty");

    function create_table() {
        var token = '{%csrf_token%}';
        $.ajax({
            url: "ajax/example/",
            type: 'GET',
            dataType: 'json',
            headers: {
                "X-CSRFToken": token
            },
            contentType: "application/json",
            success: function(data) {
                let orders = data.orders;
                create_orders(orders)
            }
        });
    }

    function create_orders(data) {
        let table_ajax = document.querySelector("#table_ajax");
        var tbody = document.createElement("tbody");
        while (table_ajax.hasChildNodes()) {
            if (table_ajax.childNodes[0].id !== "myhead") {
                table_ajax.removeChild(table_ajax.childNodes[0])
            }
        }

        for (let order of data) {
            let tr = document.createElement("tr");
            let a = document.createElement("a");
            for (let key of Object.keys(order)) {
                console.log(key)
                let td = document.createElement("td");
                td.innerHTML = order[key];
                td.setAttribute("data-label", key);
                if (order["Статус"] !== "Ожидание") {
                    a.style.display = "none";
                }
                tr.appendChild(td);
            }
            let select = document.createElement("select")

            let id = order["id"]+"select"
            select.id= id;

            let statuses = ["Статус", "Забрал", "Еду на доставку", "Доставлен"]
            for (let st of statuses) {
                let opt = document.createElement("option");
                opt.value = st;
                opt.text = st;
                select.appendChild(opt);

            }
            //
                 $("select#"+id).change(function(){

                    alert('Selected value: ' + $(this).val());
                     });
              select.addEventListener("change", function() {

                    object = {
                        id: order["id"],
                        value: this.value
                    }
                    var token = '{%csrf_token%}';

                    $.ajax({
                        url: "status/change/",
                        type: 'post',
                        dataType: 'json',
                        headers: {
                            "X-CSRFToken": token
                        },
                        contentType: "application/json",
                        data: JSON.stringify(object),
                        success: function(data) {
                            console.log(data.message)
                            create_table();

                        }
                    })

                });
                //
            let td = document.createElement("td");
            td.setAttribute("data-label", "Изменить статус");
            td.appendChild(select)
            let td_a = document.createElement("td");
            td_a.setAttribute("data-label", "отменить");

            a.href = "/curiers/private_curier/cancel/" + order["id"];
            a.innerHTML = "Отказаться"
            td_a.appendChild(a);
            var torrance1=document.createElement("td");
            torrance1.setAttribute("data-label","Отказ Клиента")
            var td_a_cancel = document.createElement("a");
            td_a_cancel.innerHTML = "Отказ Клиента";
            td_a_cancel.href="#"
            td_a_cancel.addEventListener("click",function(){
            var newobject = {
                        id: order["id"],
            }

            if (confirm("Вы уверены?")) {
                  alert("Заказ был отменен")
                  $.ajax({
                  url:"order/cancel/",
                  dataType: 'json',
                  method:"POST",
                  contentType: "application/json",
                  data:JSON.stringify(newobject),
                  success:function(data){
                     create_table();
                  }
                  });
                } else {
                  alert("Заказ не был отменен")
                }
            })
            torrance1.appendChild(td_a_cancel);
            tr.appendChild(td);
            tr.appendChild(td_a);
            tr.appendChild(torrance1);


            tbody.appendChild(tr);

            tr.addEventListener("click", function(event) {
                //при нажатии на заказ
            })
        }
        table_ajax.appendChild(tbody);
    }
    create_table();
});