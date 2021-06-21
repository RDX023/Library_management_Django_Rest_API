
$('#submit_btn').click(function(){
var book_id = $("#book_id").val()

var title = $("#book_title").val()

var author = $("#author_name").val()

var genre = $("#genre").val()

var status = $("#status").val()

//ajax POST Cde 
//var data  = { "book_id" :  book_id ,"title" : title,"author" : author,"genre" : genre,"status" : status ,'csrfmiddlewaretoken': '{{ csrf_token }}', };
var data  = { "book_id" :  book_id ,"title" : title,"author" : author,"genre" : genre,"status" : status };

var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
$.ajax({
    type: "POST",
    url: "/books/",
    data : data,
    headers:{"X-CSRFToken": $crf_token},
    success: function(response){
      alert("Book added successfully");
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
 $('#status').val("Available");
});
