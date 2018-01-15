jQuery(function($) {
  $(window).scroll(function() {
    if ($(this).scrollTop() >= 300) {
      $('header .hero-body').addClass('sticky');
    }
    else {
      $('header .hero-body').removeClass('sticky');
    }
  });
});
