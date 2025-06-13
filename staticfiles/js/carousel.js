// Carousel Configuration
const defaultConfig = {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    autoplay: {
        delay: 3000,
        disableOnInteraction: false,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        640: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 3,
        },
    },
    on: {
        init: function() {
            console.log('Swiper initialized');
        },
        error: function(error) {
            console.error('Swiper error:', error);
        }
    }
};

// Initialize a single carousel
function initCarousel(selector, customConfig = {}) {
    try {
        const element = document.querySelector(selector);
        if (!element) {
            console.warn(`Carousel element not found: ${selector}`);
            return null;
        }

        const config = { ...defaultConfig, ...customConfig };
        const swiper = new Swiper(selector, config);
        
        // Add error handling
        swiper.on('error', (error) => {
            console.error(`Error in carousel ${selector}:`, error);
        });

        return swiper;
    } catch (error) {
        console.error(`Failed to initialize carousel ${selector}:`, error);
        return null;
    }
}

// Initialize all carousels
function initAllCarousels() {
    const carousels = {
        projects: initCarousel('.projectsSlider'),
        certificates: initCarousel('.certificatesSlider'),
        jobs: initCarousel('.jobsSlider'),
        awards: initCarousel('.awardsSlider'),
        blogs: initCarousel('.blogsSlider')
    };

    // Log initialization status
    Object.entries(carousels).forEach(([name, swiper]) => {
        if (swiper) {
            console.log(`${name} carousel initialized successfully`);
        } else {
            console.warn(`${name} carousel failed to initialize`);
        }
    });

    return carousels;
}

// Handle video interactions
function setupVideoInteractions() {
    const videoContainers = document.querySelectorAll('.video-container');
    
    videoContainers.forEach(container => {
        const expandButton = container.querySelector('.expand-video');
        const iframe = container.querySelector('iframe');
        
        // Handle expand/collapse
        expandButton.addEventListener('click', () => {
            container.classList.toggle('expanded');
            // Pause carousel when video is expanded
            const swiper = container.closest('.swiper').swiper;
            if (container.classList.contains('expanded')) {
                swiper.autoplay.stop();
            } else {
                swiper.autoplay.start();
            }
        });

        // Handle mouse enter/leave
        container.addEventListener('mouseenter', () => {
            const swiper = container.closest('.swiper').swiper;
            swiper.autoplay.stop();
        });

        container.addEventListener('mouseleave', () => {
            if (!container.classList.contains('expanded')) {
                const swiper = container.closest('.swiper').swiper;
                swiper.autoplay.start();
            }
        });
    });
}

// Wait for DOM and Swiper to be ready
function waitForSwiper() {
    return new Promise((resolve) => {
        if (window.Swiper) {
            resolve();
        } else {
            const checkSwiper = setInterval(() => {
                if (window.Swiper) {
                    clearInterval(checkSwiper);
                    resolve();
                }
            }, 100);
        }
    });
}

// Initialize when everything is ready
document.addEventListener('DOMContentLoaded', async () => {
    try {
        await waitForSwiper();
        window.portfolioCarousels = initAllCarousels();
        setupVideoInteractions();
    } catch (error) {
        console.error('Failed to initialize carousels:', error);
    }
}); 