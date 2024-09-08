const slider = document.querySelector('.slider');
const sliderItems = document.querySelectorAll('.slider-item');
const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');
let counter = 0;
const slideInterval = 5000;
let autoSlideInterval;

function updateSliderPosition() {
    slider.style.transform = 'translateX(' + (-counter * 100) + '%)';
}

function goToNextSlide() {
    counter = (counter + 1) % sliderItems.length;
    updateSliderPosition();
}

function goToPrevSlide() {
    counter = (counter - 1 + sliderItems.length) % sliderItems.length;
    updateSliderPosition();
}

function startAutoSlide() {
    autoSlideInterval = setInterval(goToNextSlide, slideInterval);
}

function stopAutoSlide() {
    clearInterval(autoSlideInterval);
}

nextButton.addEventListener('click', () => {
    goToNextSlide();
    stopAutoSlide(); 
    startAutoSlide(); 
});

prevButton.addEventListener('click', () => {
    goToPrevSlide();
    stopAutoSlide(); 
    startAutoSlide(); 
});

startAutoSlide();

