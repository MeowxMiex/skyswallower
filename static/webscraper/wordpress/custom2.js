jQuery(document).ready(function ($) {



    // init Masonry
    var $wp_masonry_grid = $('.wp-masonry-posts').masonry({
        itemSelector: '.wp-masonry-grid-post',
        // columnWidth: wp_masonry_ajax_object.columnwidth,
        // gutter: wp_masonry_ajax_object.gutter,
        percentPosition: true
    });
    // layout Masonry after each image loads
    $wp_masonry_grid.imagesLoaded().progress(function () {
        $wp_masonry_grid.masonry('layout');
    });

});