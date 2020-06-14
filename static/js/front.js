var suggestions = 'Your overall score is below average. Add more missing skills (indicated by <i class="fas fa-times"></i> ) into your resume to increase your score.';
$(function () {

  if ($('#results').length) {
    // console.log("Hi");
    $('html, body').animate({ scrollTop: $('#results').offset().top }, 100)
  }
  $(".progress").each(function () {


    var value = $(this).attr('data-value');
    var left = $(this).find('.progress-left .progress-bar');
    var right = $(this).find('.progress-right .progress-bar');

    var finalScore = value;
    value = 0;
    var color = 'red';

    var scoreCounter = setInterval(function () {
      if (value > 0) {
        if (value <= 50) {
          right.css('transform', 'rotate(' + percentageToDegrees(value) + 'deg)')
        } else {
          right.css('transform', 'rotate(180deg)')
          left.css('transform', 'rotate(' + percentageToDegrees(value - 50) + 'deg)')
        }
      }
      $("#score").text(value + '%');

      if (value >= 50 && value < 70) {
        color = 'yellow';
        suggestions = 'Your overall score is average. Add more missing skills (indicated by <i class="fas fa-times"></i> ) into your resume to increase your score.';
      }
      else if (value >= 70) {
        color = 'green'
        suggestions = 'Your overall score looks good. Add more missing skills (indicated by <i class="fas fa-times"></i> ) into your resume to increase your score.';
      }
      $(".progress-bar").css("borderColor", color);

      value += 1;
      // console.log(value);

      if (value > finalScore) {
        $("h4").html(suggestions);
        clearInterval(scoreCounter);
      }
    }, 10, value, finalScore);



  })

  function percentageToDegrees(percentage) {

    return percentage / 100 * 360

  }

});