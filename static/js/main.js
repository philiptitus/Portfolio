$('.navToggle').on('click', function (e) {
    e.preventDefault();
    $('body').toggleClass('navToggleActive');
  });
  
  
  $(window).scroll(function(){
    if ($(this).scrollTop() > 10) {
      $('body').addClass('fixedHeader');
    } else {
      $('body').removeClass('fixedHeader');
    }
  });
  
  
  var swiper = new Swiper(".testimonialSwiper", {
    navigation: {
      nextEl: ".test-swiper-button-next",
      prevEl: ".test-swiper-button-prev",
    },
  });
  
  
  var swiper = new Swiper(".certificatesSlider", {
    slidesPerView: 1,
    spaceBetween: 16,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".cert-swiper-button-next",
      prevEl: ".cert-swiper-button-prev",
    },
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
      1024: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
    },
  });
  
  
  

  var swiper = new Swiper(".projectsSlider", {
    slidesPerView: 1,
    spaceBetween: 16,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".proj-swiper-button-next",
      prevEl: ".proj-swiper-button-prev",
    },
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
      1024: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
    },
  });




  var swiper = new Swiper(".awardsSlider", {
    slidesPerView: 1,
    spaceBetween: 16,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".award-swiper-button-next",
      prevEl: ".award-swiper-button-prev",
    },
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
      1024: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
    },
  });




  
  var swiper = new Swiper(".blogsSlider", {
    slidesPerView: 1,
    spaceBetween: 16,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".blog-swiper-button-next",
      prevEl: ".blog-swiper-button-prev",
    },
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
      1024: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
    },
  });





  
  
 

  
  var swiper = new Swiper(".collegeSlider", {
    slidesPerView: 1,
    spaceBetween: 16,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".cert-swiper-button-next",
      prevEl: ".cert-swiper-button-prev",
    },
    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
      768: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
      1024: {
        slidesPerView: 2,
        spaceBetween: 16,
      },
    },
  });
  