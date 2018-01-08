jQuery(function($) {
  $(window).scroll(function() {
    if ($(this).scrollTop() >= 300) {
      $('header .hero-body').css('position', 'fixed').css('top', '2rem').css('width', '100%');
    }
    else {
      $('header .hero-body').css('position', '');
    }
  });
});
