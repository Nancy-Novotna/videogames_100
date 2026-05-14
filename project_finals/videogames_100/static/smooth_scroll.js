// Source - https://stackoverflow.com/a/34263413
// Posted by Keval Bhatt, modified by community. See post 'Timeline' for change history
// Retrieved 2026-05-02, License - CC BY-SA 3.0


document.addEventListener("DOMContentLoaded", function () {
    $(".filter_submit").click(function () {
        $('html, body').animate({
            scrollTop: $("#myDiv").offset().top
        }, 2000);
    });
});
