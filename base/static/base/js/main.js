(function($) {
    "use strict";



    var windowOn = $(window);
    ////////////////////////////////////////////////////
    // 01. PreLoader Js
    windowOn.on('load', function() {
        $("#loading").fadeOut(500);
    });



    jQuery(document).ready(function() {

        // /*====== mobile off canvas active ======*/
        // function headermobileAside() {
        //     var navbarTrigger = $('.mobile-aside-button'),
        //         endTrigger = $('.mobile-aside-close'),
        //         container = $('.mobile-off-canvas-active'),
        //         wrapper = $('.wrapper');
        //     wrapper.prepend('<div class="body-overlay"></div>');
        //     navbarTrigger.on('click', function(e) {
        //         e.preventDefault();
        //         container.addClass('inside');
        //         wrapper.addClass('overlay-active');
        //     });
        //     endTrigger.on('click', function() {
        //         container.removeClass('inside');
        //         wrapper.removeClass('overlay-active');
        //     });
        //     $('.body-overlay').on('click', function() {
        //         container.removeClass('inside');
        //         wrapper.removeClass('overlay-active');
        //     });
        // };
        // headermobileAside();


        // /*--- language currency active ----*/
        // $('.mobile-language-active').on('click', function(e) {
        //     e.preventDefault();
        //     $('.lang-dropdown-active').slideToggle(900);
        // });
        // $('.mobile-currency-active').on('click', function(e) {
        //     e.preventDefault();
        //     $('.curr-dropdown-active').slideToggle(900);
        // });
        // $('.mobile-account-active').on('click', function(e) {
        //     e.preventDefault();
        //     $('.account-dropdown-active').slideToggle(900);
        // });


        // /*---------------------
        // 	mobile-menu
        // --------------------- */
        // var $offCanvasNav = $('.mobile-menu'),
        //     $offCanvasNavSubMenu = $offCanvasNav.find('.dropdown');
        // /*Add Toggle Button With Off Canvas Sub Menu*/
        // $offCanvasNavSubMenu.parent().prepend('<span class="menu-expand"><i></i></span>');
        // /*Close Off Canvas Sub Menu*/
        // $offCanvasNavSubMenu.slideUp();
        // /*Category Sub Menu Toggle*/
        // $offCanvasNav.on('click', 'li a, li .menu-expand', function(e) {
        //     var $this = $(this);
        //     if (($this.parent().attr('class').match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/)) && ($this.attr('href') === '#' || $this.hasClass('menu-expand'))) {
        //         e.preventDefault();
        //         if ($this.siblings('ul:visible').length) {
        //             $this.parent('li').removeClass('active');
        //             $this.siblings('ul').slideUp();
        //         } else {
        //             $this.parent('li').addClass('active');
        //             $this.closest('li').siblings('li').removeClass('active').find('li').removeClass('active');
        //             $this.closest('li').siblings('li').find('ul:visible').slideUp();
        //             $this.siblings('ul').slideDown();
        //         }
        //     }
        // });

        // // mobile__menu__end







        // scrollToTop
        $.scrollUp({
            scrollName: 'scrollUp', // Element ID
            topDistance: '300', // Distance from top before showing element (px)
            topSpeed: 300, // Speed back to top (ms)
            animation: 'fade', // Fade, slide, none
            animationInSpeed: 200, // Animation in speed (ms)
            animationOutSpeed: 200, // Animation out speed (ms)
            scrollText: '<i class="icofont-rounded-up"></i>', // Text for element
            activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
        });


        $(window).on('scroll', function() {
            var scroll = $(window).scrollTop();
            if (scroll < 245) {
                $(".header__sticky").removeClass("sticky");
            } else {
                $(".header__sticky").addClass("sticky");
            }
        });


        // Grid Countdown
        $('[data-countdown]').each(function() {
            var $this = $(this),
                finalDate = $(this).data('countdown');
            $this.countdown(finalDate, function(event) {
                $this.html(event.strftime('<div class="count"><p>%D</p><span>Days</span></div><div class="count"><p>%H</p> <span>Hrs</span></div><div class="count"><p>%M</p> <span>Min</span></div><div class="count"> <p>%S</p> <span>Sec</span></div>'));
            });
        });



        /*====== Search active ======*/
        function sidebarSearch() {
            var searchTrigger = $('.header__icon'),
                endTriggersearch = $('.header__search__close'),
                container = $('.header__main__search__active ');
            searchTrigger.on('click', function(e) {
                e.preventDefault();
                container.addClass('inside');
            });
            endTriggersearch.on('click', function() {
                container.removeClass('inside');
            });
        };
        sidebarSearch();




        // // Counter Js
        $('.counter').counterUp({
            delay: 100,
            time: 1000
        });





        /* magnificPopup video view */
        $('.video-btn').magnificPopup({
            type: 'iframe'
        });


        /* magnificPopup img view */
        $('.popup__img').magnificPopup({
            type: 'image',
            gallery: {
                enabled: true
            },
        });


        //testimonial__section__start
        $('.testimonial__slider__active').slick({
            infinite: true,
            slidesToShow: 2,
            slidesToScroll: 1,
            dots: false,
            prevArrow: '<span class="prev_class"><i class="icofont-long-arrow-left"></i></span>',
            nextArrow: '<span class="next_class"><i class="icofont-long-arrow-right"></i></span>',
            responsive: [{
                    breakpoint: 1367,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 993,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 769,
                    settings: {
                        slidesToShow: 1,
                    }
                },
                {
                    breakpoint: 321,
                    settings: {
                        slidesToShow: 1,
                    }
                },
            ]

        });
        $('.testimonial__slider__active__3').slick({
            infinite: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            dots: false,
            prevArrow: '<span class="prev_class"><i class="icofont-long-arrow-left "></i></span>',
            nextArrow: '<span class="next_class"><i class="icofont-long-arrow-right active"></i></span>',
            responsive: [{
                    breakpoint: 1367,
                    settings: {
                        slidesToShow: 1,
                    }
                },
                {
                    breakpoint: 993,
                    settings: {
                        slidesToShow: 1,
                    }
                },
                {
                    breakpoint: 769,
                    settings: {
                        slidesToShow: 1,
                    }
                },
                {
                    breakpoint: 321,
                    settings: {
                        slidesToShow: 1,
                    }
                },
            ]

        });

        //about__course__slider__start
        $('.about__course__slider__active').slick({
            infinite: true,
            slidesToShow: 3,
            slidesToScroll: 1,
            dots: false,
            arrows: false,
            responsive: [{
                    breakpoint: 1367,
                    settings: {
                        slidesToShow: 3,
                    }
                },
                {
                    breakpoint: 993,
                    settings: {
                        slidesToShow: 3,
                    }
                },
                {
                    breakpoint: 769,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 500,
                    settings: {
                        slidesToShow: 1,
                    }
                },
            ]

        });


        //instructor__slider__start
        $('.instructor__slider__active').slick({
            infinite: true,
            slidesToShow: 2,
            slidesToScroll: 1,
            dots: false,
            arrows: false,
            responsive: [{
                    breakpoint: 1367,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 993,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 769,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 500,
                    settings: {
                        slidesToShow: 1,
                    }
                },
            ]

        });



        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl)
        })



        // Block Show/hide option
        if (document.querySelector('.toggle-btn') !== null) {
            $('.toggle-btn').on('click', function(e) {
                e.preventDefault();
                var $this = $(this).attr('data-target');
                $($this).toggleClass('visible');
            });
        }




        // image loaded portfolio init
        var gridfilter = $('.grid');
        if (gridfilter.length) {
            $('.grid').imagesLoaded(function() {
                $('.gridFilter').on('click', 'button', function() {
                    var filterValue = $(this).attr('data-filter');
                    $grid.isotope({
                        filter: filterValue
                    });
                });
                var $grid = $('.grid').isotope({
                    itemSelector: '.grid-item',
                    percentPosition: true,
                    masonry: {
                        columnWidth: '.grid-item',
                    }
                });
            });
        }

        // project Filter
        if ($('.gridFilter button').length) {
            var projectfiler = $('.gridFilter button');
            if (projectfiler.length) {
                $('.gridFilter button').on('click', function(event) {
                    $(this).siblings('.active').removeClass('active');
                    $(this).addClass('active');
                    event.preventDefault();
                });
            }
        }


        /* Tilter Activation */
        if ($('[data-tilt]').length) {

            $('[data-tilt]').tilt({
                perspective: 2000,
            });

        }
        /* ----------------------------
            AOS Scroll Animation 
        -------------------------------*/
        AOS.init({
            offset: 40,
            duration: 1000,
            once: true,
            easing: 'ease',
        });




        /*===================================
            Svg Icon Draw
        ====================================*/
        var $svgIconBox = $('.single-svg-icon-box');
        $svgIconBox.each(function() {
            var $this = $(this),
                $svgIcon = $this.find('.svg-icon'),
                $id = $svgIcon.attr('id'),
                $icon = $svgIcon.data('svg-icon');
            var $vivus = new Vivus($id, { duration: 100, file: $icon });
            $this.on('mouseenter', function() {
                $vivus.reset().play();
            });
        });




    });

})(jQuery);




var swiper = new Swiper(".hero__course", {
    effect: "cards",
    grabCursor: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
});


var swiper = new Swiper(".featured__course", {
    grabCursor: true,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    slidesPerView: 1,
    breakpoints: {
        575: {
            slidesPerView: 2,
        },

        768: {
            slidesPerView: 2,
        },

        992: {
            slidesPerView: 3,
        },
        1200: {
            slidesPerView: 3
        },
        1500: {
            slidesPerView: 4
        }
    },
});