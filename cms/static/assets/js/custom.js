$(function () {
    $('#riso_toggle').on('click', function () {
        $(this).siblings('[data-function]').toggle(300);
    })

    $('button[data-function="new"]').on('click', function () {
        $('button[data-function]').hide();

        $.ajax({
            type: "GET", // or "GET" depending on your API
            url: "/api/themes/", // Replace with your API URL
            data: null,
            headers: {
                "X-CSRFToken": csrf_token // Include the CSRF token in the request headers
            },
            success: function (response) {
                // Handle the API response
                console.log(response);
                if (Array.isArray(response)) {
                    $('#theme_list').empty()

                    var html = '';
                    response.forEach(function (theme) {
                        html += `<div class="card card-bordered mb-2">
                                    <div class="card-header ">
                                    <h3 class="card-title gap-1 text-gray-900">Theme <div class="text-primary">${theme.name}</div></h3>
                                    </div>
                                `

                        const templates = theme.templates
                        if (Array.isArray(templates)) {
                            html += `<div class="card-body row mb-4">`
                            templates.forEach(function (template) {
                                console.log('-----template', template)
                                html += `<div class="col-6">
                                            <div class="card">
                                                <div class="card-body px-0">
                                                    <img src="${template.thumbnail}" alt="${template.name}" class="img-fluid ">
                                                    <h5>${template.name}</h5>
                                                    <p>${template.description || ''}</p>
                                                    <div class="text-center">
                                                        <div class="form-check d-inline-block">
                                                            <input class="form-check-input" name="template_name" type="radio" value="${theme.template_name}" id="${template.id}" required/>
                                                            <label class="form-check-label" for="${template.id}">
                                                            </label>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        `
                            })
                            html += `</div></div>`
                        }
                    });

                    $('#theme_list').html(html);
                }
            },
            error: function (xhr, textStatus, errorThrown) {
                // Handle any errors
                console.error(xhr.responseText);
            }
        });


    });

    $('#form_new_page').on('submit', function (e) {
        e.preventDefault();
        const formData = new FormData(this);

        var object = {};
        formData.forEach(function (value, key) {
            object[key] = value;
        });
        object['csrf_token'] = csrf_token;
        object['sites'] = [1];
        // var json = JSON.stringify(object);

        $.ajax({
            url: "/api/pages/",
            type: "post",
            headers: {
                "accept": "application/json",
                "Content-Type": "application/json",
                "X-CSRFToken": csrf_token // Include the CSRF token in the request headers
            },
            data: JSON.stringify(object),
            success: function (response) {
                if (response['result']) {

                    Swal.fire({
                        title: 'Notice',
                        html: response['message'],
                        icon: "success",
                        type: "success"
                    }).then(function () {
                        // window.location.reload();

                    });
                } else {

                    Swal.fire({
                        title: 'Notice',
                        html: response['message'],
                        icon: "error",
                        type: "error"
                    }).then(function () {
                    });
                }
            },
            error: function (request, status, error) {
                Swal.fire({
                    title: 'Notice',
                    html: error,
                    icon: "error",
                    type: "error"
                }).then(function () {
                });
            }
        });
    });
});
