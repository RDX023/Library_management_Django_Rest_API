
        $('.speak').click(function () {
            var $val = $('#question').text();
            var question = $val;
            console.log("post question" + question)
            var $ans = $('#user_said').text();
            var answer = $ans;
            console.log("post answer" + answer)
            $.ajax({
              type: 'POST',
              url: 'http://127.0.0.1:8000/home/',
              data: {
                question_data: question,
                answer_data: answer,
              },
            });
            $('#user_said').text('');
          });
