$(function () {
    $('#riso_toggle').on('click', function () {
        $(this).siblings('[data-function]').toggle(300);
    })

    // $('button').on('click', function () {
    //     const idButton = $(this).attr('id');
    //     console.log('idButton', idButton, `div[data-kt-drawer-toggle="#${idButton}"]`, $(`div[data-kt-drawer-toggle="#${idButton}"]`))
    //     if ($(`div[data-kt-drawer-toggle="#${idButton}"]`)) {
    //         $(`div[data-kt-drawer-toggle="#${idButton}"]`).toggleClass('drawer-on');
    //     }
    // });
});
