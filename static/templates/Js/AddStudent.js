
$('#submit_btn').click(function(){
 var library_id = $('#library_id').val();

var name = $('#name').val();

var phone_no = $('#phone_no').val();

var email_id = $('#email_id').val();

var course = $('#course').val();

var data  = { "library_id" :  library_id ,"name" : name ,"phone_no" : phone_no ,"email_id" : email_id,"course" : course};

var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');


$.ajax({
    type: "POST",
    url: "/students/",
    data : data,
    headers:{"X-CSRFToken": $crf_token},
    success: function(response){
      alert("Student Data added successfully");
    },
    error: function(){
      alert("error while POST");
    }
});

});

$('#reset_btn').click(function(){
$(document).ready(function() {
    $('input[type=text]').each(function() {
        $(this).val('');
    });
});
});