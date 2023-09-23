// $('.hello').click(function (e) { 
//     console.log("hello again")
    
// });
// $('#slider1, #slider2, #slider3').owlCarousel({
//     loop: true,
//     margin: 20,
//     responsiveClass: true,
//     responsive: {
//         0: {
//             items: 1,
//             nav: false,
//             autoplay: true,
//         },
//         600: {
//             items: 3,
//             nav: true,
//             autoplay: true,
//         },
//         1000: {
//             items: 6,
//             nav: true,
//             loop: true,
//             autoplay: true,
//         }
//     }
// })

// $('.plus-cart').click(function(){
    
// })
var proval;
try{
$(document).ready(function() {
    $('.plus-cart').click(function(){
    var pid = $(this).attr("pid").toString();
    var id = $(this).attr("id").toString();
    var proval=document.getElementById(id).value;
    $.ajax({
        url: "/cart_quan",
        work:console.log("hello"),
        type: "GET",
        data:{prod_id:pid,prod_quantity:proval},
        dataType:"json",
        success:function(data){
        console.log(data.amount);
            document.getElementById('amount').innerText= data.amount;
            document.getElementById('total').innerText= data.totalamount;
            }
        })
    })
})
}
catch (error) {
    console.log(error)
}

try{
$('.remove-cart').click(function(){
    var pid = $(this).attr("pidi").toString();
    // var id = $(this).attr("id").toString();
    // var current_obj=document.querySelector('pipi');
    // console.log("this is pid",pid)
    // var trys=document.getElementById("trys");
    $.ajax({
        url: "/remove_cart",
        type: "GET",
        data:{prod_id:pid},
        dataType:"json",
        success:function(data){
            // document.getElementById('amount').innerText= datas.amount;
            // document.getElementById('total').innerText= datas.totalamount;
            console.log(data.name);
            // current_obj.remove()
            // var g=pid.parentNode.parentNode.parentNode;
            // trys.remove();
            // console.log(g);
            },
        error:function(error){
            console.log("error");
        }
        
        })
    })
}
catch (error) {
    console.log(error)
}
$('.remove').click(function(){
    var pid = $(this).attr("pidi").toString();
    var t=this
    console.log(t)
    // var pipi=document.querySelector('pipi');

    // console.log(pipi);
    $.ajax({
        url: "/remove_cart",
        type: "GET",
        data:{prod_id:pid},
        success:function(data){
            console.log(data.total_amount);
            document.getElementById('amount').innerText= data.amount;
            document.getElementById('total').innerText= data.totalamount;
            var h=t.parentNode.parentNode.parentNode.parentNode.parentNode;
            h.remove();
            // console.log(pid);
            // g.remove()
            // if(pipi==pid){
            //     pipi.style.display='none';
            // }
            },
        error:function(error){
            console.log(error);
        }
        })
    })
//     // Your code that uses $.ajax here
// });

// $('.minus-cart').click(function(){
//     var id = $(this).attr("pid").toString();
//     var eml = this.parentNode.children[2];
    
//     $.ajax({ 
//         type: "GET",
//         url: "/minuscart",
//         data:{prod_id:id},
//         success:function(data){
//             eml.innerText = data.quantity;
//             document.getElementById('amount').innerText= data.amount;
//             document.getElementById('totalamount').innerText= data.totalamount;
//         }
//     })
// })

// $('.remove-cart').click(function(){
//     var id = $(this).attr("pid").toString();
//     console.log(id)
//     $.ajax({
//         type: "GET",
//         url: "/removecart",
//         data:{prod_id:id},
//         success:function(data){
//             document.getElementById('amount').innerText= data.amount;
//             document.getElementById('totalamount').innerText= data.totalamount;
//         }
//     })
// })
// function getval(){
//    a= document.getElementById("numb").value;
//    console.log(a)
//    console.log("hello ji")
// }
