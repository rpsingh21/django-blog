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
    var current_acivity = $(this).parent().attr("class");
    var action = activity_request(url);
    var p = $(this).parent().parent();

    // we get in action a json object 
    /*
        activity_type = 'F','U','D','DE'
        'DE' == delete operations

    */
    var c_obj = $(this).find("span");
    var c_value = parseInt(c_obj.text());
    $(this).find("i").removeClass("text-danger text-success");
    switch (action) {
      case "DE":
          // $(this).find("i").removeClass("text-danger text-success");
          $(this).find("span").html(c_value-1);
          break;
      case "D":
          if (current_acivity == "U"){
            $(this).find("span").html(c_value-1);

            // now add 1 in other vote
            p.find("D").find("i").addClass("text-danger");
            var ch = p.find("D").find("span");
            ch.html(parseInt(ch.text())+1);
          }
          else{
            $(this).find("span").html(c_value+1);
            $(this).find("i").removeClass("text-success");
          }
          break;
      case "U":
          if (current_acivity == "D"){
            $(this).find("span").html(c_value-1);

            // now add 1 in other vote
            p.find("D").find("i").addClass("text-danger");
            var ch = p.find("D").find("span");
            ch.html(parseInt(ch.text())+1);
          }
          else{
            $(this).find("span").html(c_value+1);
            $(this).find("i").removeClass("text-success");
          }
          break;
      case "F":
          $(this).find("span").html(c_value+1);
          $(this).find("i").removeClass("text-danger");
          break;
      }

})