$('#modalsubmit').on('click', function(event){
    event.preventDefault();
    let email = $('#modalemail').val();
    let instance = M.Modal.getInstance($('#submodal'));
    if(validateEmail(email)){
      createModalPost(email, instance);
    }else{
      displayModalError();
    }
});

function displayModalError(instance) {
  $("#modal-helper-text").text("Must enter a valid email.");
  $("#modalemail").addClass("invalid");

}

function createModalPost(sub_email, instance) {
  $.ajax({
        url : "subscriptions/new",
        type : "POST",
        data : { email : sub_email,
                 csrfmiddlewaretoken: window.CSRF_TOKEN}
    });
    instance.close();
    $("#modalinput").hide()
    $(".modal-footer").hide()
    $(".modal-content").text("Thanks for subscribing, we'll be in touch!")
};
