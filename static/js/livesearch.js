$(document).ready(function(){
    let value=$("#parameter").val()
    $("#parameter").on("change",function(){
       value = this.value
    });
    $("#search").on("keyup",function(){
        let search = this.value
        let object={
         parameter:value,
         search:search,
        }
        if(search.length>1){
            $.ajax({
               url: "live_search/",
               type: 'post',
               dataType: 'json',
               contentType: "application/json",
               data: JSON.stringify(object),
               success:function(data)
               {
               console.log(data)
               arr = JSON.parse(data.arr)
                var ul = document.querySelector(".live-search-list");
                  while (ul.hasChildNodes()) {
            if (ul.childNodes[0].id !== "myhead") {
                ul.removeChild(ul.childNodes[0])
            }
        }
                for(let el of arr){
                    let li = document.createElement("li");
                    li.innerHTML=el
                    li.addEventListener("click",function(){
                        let search = document.querySelector("#search")
                        search.value = this.innerHTML;
                    })
                    ul.appendChild(li)
                }
               }
         });
        }
    })

});