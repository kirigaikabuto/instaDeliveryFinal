$(document).ready(function(){
function fun1() {
    var sel=document.getElementById('money').selectedIndex;
    var options=document.getElementById('money').options;
    alert('Выбрана опция '+options[sel].text);
    document.getElementById('summa').style.display = 'block';
}



});

$(document).ready(function(){
  $('.icon').on("click", function(){
    $(this).closest('.menu').toggleClass('menu-open');
  });
});
