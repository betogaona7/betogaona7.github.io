$(document).ready(function() {
  var ripple_wrap = $('.ripple-wrap'),
      rippler = $('.ripple'),
      finish = false,

      monitor = function(el) {
        var computed = window.getComputedStyle(el, null),
            borderwidth = parseFloat(computed.getPropertyValue('border-left-width'));

        if (!finish && borderwidth >= 1500) {
          el.style.WebkitAnimationPlayState = "paused";
          el.style.animationPlayState = "paused";
          swapContent();
          console.log("Here we made a swap");
        }
        if (finish) {
          el.style.WebkitAnimationPlayState = "running";
          el.style.animationPlayState = "running";
          console.log("running");
          return;
        } else {
          window.requestAnimationFrame(function() {monitor(el)});
          console.log("else running");
        }
      };

  storedcontent = $('#content-2').html();
  $('#content-2').remove();
  
  rippler.bind("webkitAnimationEnd oAnimationEnd msAnimationEnd mozAnimationEnd animationend", function(e){
    ripple_wrap.removeClass('goripple');
  });

  $('body').on('click', '.link', function(e) {
    rippler.css('left', e.clientX + 'px');
    rippler.css('top', e.clientY + 'px');
    e.preventDefault();
    ripple_wrap.addClass('goripple');
    window.requestAnimationFrame(function() {monitor(rippler[0])});

  });
  
  function swapContent() {
      var newcontent = $('#content-area').html();
      $('#content-area').html(storedcontent);
      storedcontent = newcontent;
      // do some Ajax, put it in the DOM and then set this to true
      setTimeout(function() {
        finish = true;
      },10);
      document.title = "Alberto Gaona | Projects ";
      finish = true;
  }
});