$(function() {

  // Submit form action
  $("#formId").submit(function(e) {
    e.preventDefault(); 
    
    $.ajax({
           type: "POST",
           url: "/_predict",
           data: {inpt_beds: $("#inpt_beds").val(),
				  inpt_baths: $("#inpt_baths").val(),
				  inpt_sqft: $("#inpt_sqft").val(),
				  inpt_age: $("#inpt_age").val(),
				  inpt_lotsize: $("#inpt_lotsize").val(),
				  inpt_garages: $("#inpt_garages").val()
           },
           success: function(data)
           {
               $("#house_price").html("$"+data);
               animateCSS('#price_wrapper', 'lightSpeedInLeft');
           }
    });
    
  });
  
  
  // Useful function recommended by the developers of Animate CSS.
  const animateCSS = (element, animation, prefix = 'animate__') =>
    // We create a Promise and return it
    new Promise((resolve, reject) => {
      const animationName = `${prefix}${animation}`;
      const node = document.querySelector(element);

      node.classList.add(`${prefix}animated`, animationName);

      // When the animation ends, we clean the classes and resolve the Promise
      function handleAnimationEnd() {
        node.classList.remove(`${prefix}animated`, animationName);
        node.removeEventListener('animationend', handleAnimationEnd);

        resolve('Animation ended');
      }

      node.addEventListener('animationend', handleAnimationEnd);
  });
 
 // Trigger animation. 
 animateCSS('#price_wrapper', 'tada'); 

});