function get_comments() {
    $.ajax({
        method: "GET",
        url: "/comments/{{ post.id }}/{{ post.slug }}/",
        success: function(data) {
            document.getElementById("comments").innerHTML = data;
        },
        error: function(data) {
            console.log("error")
            console.log(data)
        }
    })
}

function reply(fid) {
    var ffid = "#p-" + fid
    $(ffid).slideToggle();
    var url = '/comments/{{ post.slug }}/' + fid;
    $.ajax({
        type: "GET",
        url: url,
        success: function(data) {
            $(ffid).html(data);
        }
    });
}

$(document).on('click', '.submit-btn', function(e) {
    var fid = "#" + $(this).parents('form:first').attr('id');
    var url = "/api/comments/create/";
    $.ajax({
        type: "POST",
        url: url,
        data: $(fid).serialize(),
        success: function(data) {
            get_comments();
            $(fid).closest('form').find("input[type=text], textarea").val("");
        }
    });
    e.preventDefault();
});

$(document).on('click', '.update-btn', function(e) {
    var fid = "#" + $(this).parents('form:first').attr('id');
    var url = $(this).parents('form:first').attr('action');
    // alert(url);
    $.ajax({
        type: "PUT",
        url: url,
        data: $(fid).serialize(),
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        },
        success: function(data) {
            get_comments();
        }
    });
    e.preventDefault();
});

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function delete_comment(url) {
    if (!confirm("delete it ?")) {
        return 0;
    }
    $.ajax({
        type: "DELETE",
        url: url,
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        },
        success: function(data) {
            get_comments();
        }
    });
}

$(document).on('click', '.activity-btn', function(e) {
    e.preventDefault();
    url = $(this).attr("link");
    $.ajax({
        type: 'POST',
        url: url,
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        },
        success: function(data) {
            get_comments();
        }
    });
});

function get_edit_form(arg) {
    $(arg).slideToggle();
}

$(document).ready(get_comments);


//  NEW API HANDLER USING JQUERY
$(document).on('click','.activity-btn',function(event) {
    event.preventDefault();
    url = $(this).attr("link");
    var current_acivity = $(this)
    var action = activity_request(url);

    // we get in action a json object 
    /*
        activity_type = 'F','U','D','DE'
        'DE' == delete operations

    */
})