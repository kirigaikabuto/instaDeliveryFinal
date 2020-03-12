
var object = {
	marshrut:null,
	ves:null,
  from:null,
  from_phone:null,
  from_comment:null,
  to:null,
  distance:null,
  to_phone:null,
  to_date:null,
  to_date_until:null,
  to_comment:null,
  itog:null,
  summa:null,
  nal:null,
  raschet:null,
}

var matches = document.querySelectorAll("button.marshrut");
var previousElement=null;
for(let i=0;i<matches.length;i++)
{ 
  
  matches[i].addEventListener("click",function(){
  	if(previousElement!=null)
  	{
  		previousElement.classList.remove("style_for_button");
  	}
  	this.classList.toggle("style_for_button");
  	previousElement = this;
  	object.marshrut = this.innerHTML;
    update_itogo();
  });
}

var ves = document.querySelectorAll("button.ves_value");
var previousElement1=null;
for(let i=0;i<ves.length;i++)
{

  ves[i].addEventListener("click",function(){
  	if(previousElement1!=null)
  	{
  		previousElement1.classList.remove("style_for_button");
  	}
  	this.classList.toggle("style_for_button");
  	previousElement1 = this;
    let ourves = this.innerHTML.split(" ");

    ourves = ourves[1].split("кг");
  	object.ves = parseInt(ourves[0]);
    update_itogo();
  });
}
var from  = document.querySelector("#from");
object.from = from.value;
var tel = document.querySelector("#from_phoner");
tel.addEventListener("change",function(){
  object.from_phone = tel.value;
});
var comment1 = document.querySelector("#comment1");
comment1.addEventListener("change",function(){
  //console.log(comment1.value.length)
     object.from_comment = comment1.value;

});

var to  = document.querySelector("#to");
object.to = to.value;
var distance = document.querySelector("#distance");
distance.addEventListener("change",function(){
  object.distance = parseFloat(distance.value.split(" ")[0]);
})
var tel2 = document.querySelector("#phone_number2");
tel2.addEventListener("change",function(){
  object.to_phone = tel2.value;
});
var data1 = document.querySelector("#data_1");
data1.addEventListener("change",function(){
  object.to_date = data1.value;
});
var data2 = document.querySelector("#data_to_until");
data2.addEventListener("change",function(){
  object.to_date_until = data2.value;
});
var comment2 = document.querySelector("#comment2");
comment2.addEventListener("change",function(){
  object.to_comment = comment2.value;
});
var summa = document.querySelector("#summa");

summa.addEventListener("change",function(){
  object.summa = parseInt(this.value);
  update_itogo();
})
var main = document.querySelectorAll(".kalkul")[0];
main.addEventListener("mouseout",function(){
  let check = true;
  for(let prop in object)
  {

    if(object[prop]==null)
    {
      // console.log(object);
    }
  }
});
update_itogo(); 

function update_itogo(){
   object.from = from.value;
   object.to = to.value;
   object.distance = parseFloat(distance.value.split(" ")[0]);
   var itogo =document.querySelector("#itogo");
   let price_distance=0;
   let price_ves =0;
   let price_marshrut=0;
     if(object.distance<6)
     {
      price_distance = 800;
     }
     else{
      price_distance = 800+(object.distance-6)*80;
     }
  if(object.ves !== null)
  {
     price_ves = 100*(object.ves-3);
     if(price_ves<0)
     {
      price_ves = 0;
     }
  }
  if(object.marshrut!==null){
      if(object.marshrut =="Авто")
        {
          price_marshrut = 300;
        }
  }
  
  let result = price_distance+price_marshrut+price_ves;
  itogo.value = result;
  object.itog=result;
  let nal = document.querySelector("#nal");
  let raschet = document.querySelector("#raschet")
  nal_value = parseInt(nal);
  raschet_value = parseInt(nal);
  if (object.summa !== null){
  nal.value = object.summa;
  raschet.value = object.summa-result;
  }

}
$(document).ready(function(){
  $('#send').on("click", function(){
    object.nal = document.querySelector("#nal").value;
    object.raschet = document.querySelector("#raschet").value;
    //проверка
    var fromеtest  = document.querySelector("#origin-input");
    var tel = document.querySelector("#from_phoner");
    var comment1 = document.querySelector("#comment1");
    var totest  = document.querySelector("#destination-input");
    var tel2 = document.querySelector("#phone_number2");
    var data1 = document.querySelector("#data_1");
    var data2 = document.querySelector("#data_to_until");
    var comment2 = document.querySelector("#comment2");
    
  ///
  if (fromеtest.value.length==0){
    console.log(from.value.length);
    alert("Заполните поле from");
  }
  else if(tel.value.length==0){
    alert("Заполните поле телефон откуда");
  }
   else if(comment1.value.length==0){
     alert("Заполните поле комментарий1");
  }
   else if(totest.value.length==0){
    alert("Заполните поле to");
  }
   else if(tel2.value.length==0){
    alert("Заполните поле телефон куда");
  }
  else if(data1.value.length==0){
    alert("Заполните поле дата");
  }
  else if(data2.value.length==0){
    alert("Заполните поле дата и день");
  }
  else if(comment2.value.length==0){
   alert("Заполните второй комментарий");
  }
  else{
    var token = '{%csrf_token%}';
     $.ajax({
       url: "kalkul/send/",
       type: 'post',
       dataType: 'json',
       headers:{
        "X-CSRFToken":token
       },
       contentType: "application/json",
       data: JSON.stringify(object),
       success:function(data)
       {
        alert(data.message)
        console.log(data.arr)
        window.location.replace("http://127.0.0.1:8000/users/private/");
       }
     })
  }
  });

     
});

