jQuery(
  (function ($) {
    "use strict";

    $(window).on("scroll", function () {
      if ($(this).scrollTop() > 50) {
        $(".main-nav").addClass("menu-shrink");
      } else {
        $(".main-nav").removeClass("menu-shrink");
      }
    });

    $(".alert").fadeTo(2000, 500).slideUp(500, function () {
      $(".alert").slideUp(500);
    });

  })(jQuery)
);
