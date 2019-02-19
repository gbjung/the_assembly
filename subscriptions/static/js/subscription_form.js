$('.submitbutton').on('click', function(event){
    event.preventDefault();
    let email = $('#email').val();
    if(validateEmail(email)){
      createPost(email);
    }else{
      displayError();
    }
});

function validateEmail(email) {
  let re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(email);
}

function displayError() {
  $(".helper-text").text("Must enter a valid email.");
  $(".email").addClass("invalid");
}

function createPost(sub_email) {
  $.ajax({
        url : "subscriptions/new",
        type : "POST",
        data : { email : sub_email,
                 csrfmiddlewaretoken: window.CSRF_TOKEN}
    });
    $('.email').hide();
    $('.helper-text').hide();
    $('.submitbutton').addClass('disable-anchor');
    $('.submitbutton').text("SUBSCRIBED!");
    $('.subscribed').show();
};
