$(document).ready(function(){
  $(".favoriteline").click(function(){
    theselected = getSelectionText();
    $.ajax({
      type:"POST",
      url: "/poetry/favoriteline/",
      data: {
        theselected: theselected,
        poemNum: poemNum
      },
      success: function(back){
        alert(back);
      },
      failure: function(errMsg){
        alert(errMsg)
      }
    });
    return false;
  });

  $(".favoritepoem").click(function(){
    $.ajax({
      type:"POST",
      url: "/poetry/favorite/",
      data: {
        poemNum: poemNum
      },
      success: function(back){
        alert(back);
      },
      failure: function(errMsg){
        alert(errMsg);
      }
    });
    return false;
  });


});
function getSelectionText() {
    var text = "";
    if (window.getSelection) {
        text = window.getSelection().toString();
    } else if (document.selection && document.selection.type != "Control") {
        text = document.selection.createRange().text;
    }
    return text;
}
