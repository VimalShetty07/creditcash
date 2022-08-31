$(document).ready( function () {
    $('.rzp-button1').click(function (e){
        console.log("FFf")
        e.preventDefault();
        

        var name = $("[name = 'name']").val();
        var email = $("[name = 'email']").val();
        var number = $("[name = 'number']").val();


        if(name == ""|| email == ""|| number == "")
        {
          swal("Alert", "All fields must be provided","error");
          return false;  


        } 
        else{
            var options = {
                "key": "rzp_test_GB5h8MarzT5jOH", 
                "amount": "{{client.amount}}", 
                "currency": "INR",
                "name": "Creditcash",
                "description": "Test Transaction",
                "image": "https://example.com/your_logo",
                "order_id": "order_9A33XWu170gUtm",
                "callback_url": "https://eneqd3r9zrjok.x.pipedream.net/",
                "prefill": {
                    "name": "Gaurav Kumar",
                    "email": "gaurav.kumar@example.com",
                    "contact": "9999999999"
                },
                "notes": {
                    "address": "Razorpay Corporate Office"
                },
                "theme": {
                    "color": "#3399cc"
                }
            };
            var rzp1 = new Razorpay(options);
            rzp1.on('payment.failed', function(response){
                alert(response.error.metadata.payment_id);
            });
                rzp1.open();
        }   
})
})