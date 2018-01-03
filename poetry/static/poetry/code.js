
$(document).ready(function() {
  getPoem();
  $("#enter").click(function(){
    $(".explore_page_start").fadeOut(600);
  });


    $(".arrow").click(function() {
        console.log("We here");
        makeDisappear();

        setTimeout(function() {
          getPoem();
            makeAppear();
        }, 2000);
    });

});

function makeDisappear () {
    console.log("We doin it");
    $(".arrow").fadeOut(200);
    $(".explorePoem").slideUp(1000, function() {
        $("h3").removeClass("exposed");
        $("h3").addClass("hidden");
    });
    setTimeout(function() {
        $("h1").fadeOut(600);
    }, 1500);
    return true;

}
function makeSearchAppear() {
        setTimeout(function() {
         $("h1").fadeIn(1500, function() {

        $("h3").removeClass("hidden");
        $("h3").addClass("exposed");
        setTimeout( function() {
            $("p").slideDown(1000);
                    $(".arrow").fadeIn(200);

        }, 800);
        });
    }, 700);
}
function makeAppear() {
    console.log("makeAppear");
    setTimeout(function() {
         $("h1").fadeIn(1500, function() {

        $("h3").removeClass("hidden");
        $("h3").addClass("exposed");
        setTimeout( function() {
            $(".explorePoem").slideDown(1000);
                    $(".arrow").fadeIn(200);

        }, 800);
        });
    }, 700);
}
function getPoem(){
  $.ajax({
    type:"GET",
    url: "/poetry/explore",
    success: function(data){
      $("h1").html("<a href = '/poetry/" + data[0].pk + "'>" + data[0].fields.title + "</a>");
      $("h3").html("By: <a href = '/poetry/author/" + data[0].fields.writer[1] + "' >" + data[0].fields.writer[0] + "</a>");
      $(".explorePoem").html(data[0].fields.text.replace(/\n/g, "<br>"));
    }
  });
}
