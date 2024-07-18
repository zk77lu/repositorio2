


const swiper = new Swiper('.swiper-container', {
    direction: 'horizontal',
    loop: true,
    grabCursor: false,
    centeredSlides: false,
    slidesPerView: 1, // Show one slide at a time
    spaceBetween: 30,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  });

  // Update slide index when the slide changes
  swiper.on('slideChange', function () {
    var totalImagens=document.querySelectorAll('.swiper-slide')
    NumeroTotal=totalImagens.length
    const slideIndex = (swiper.realIndex % swiper.slides.length) + 1;
    document.getElementById('slideIndex').innerText = slideIndex + " " + "de" + NumeroTotal;
  });