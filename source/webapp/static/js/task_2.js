
function login(login, password){
    $.ajax({
     url: 'http://localhost:8000/api/v1/login/',
     method: 'post',
     data: JSON.stringify({username: login, password: password}),
     dataType: 'json',
     contentType: 'application/json',
     success: function(response, status){localStorage.setItem('apiToken', response.token);},
     error: function(response, status){console.log(response);}

});
}
function logout(){
    $.ajax({

    url: 'http://localhost:8000/api/v1/logout/',

    method: 'post',

    headers: {'Authorization': `Token ${localStorage.getItem('apiToken')}`},

    dataType: 'json',

    success: function(response, status){console.log(response);},

    error: function(response, status){console.log(response);}

});
}
function view_all_issues(){
    $.ajax({
     url: `http://localhost:8000/api/v1/issues/`,
     method: 'get',
     headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
     dataType: 'json',
     contentType: 'application/json',
     success: function(response, status){console.log(response);},
     error: function(response, status){console.log(response);}

});
}
function view_all_projects(){
    $.ajax({
     url: `http://localhost:8000/api/v1/projects/`,
     method: 'get',
     headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
     dataType: 'json',
     contentType: 'application/json',
     success: function(response, status){console.log(response);},
     error: function(response, status){console.log(response);}

});
}
function view_all_issues_of_project(pk){
    $.ajax({

     url: `http://localhost:8000/api/v1/projects/1`,
     method: 'get',
     headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
     dataType: 'json',
     contentType: 'application/json',
     success: function(response, status){console.log(response.issues);},
     error: function(response, status){console.log(response);}

});
}
function create_issue(summary, description, project, status, type, createdBy, assignedTo) {
    $.ajax({
            url: `http://localhost:8000/api/v1/issues/`,
            method: 'post',
            headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
            data: JSON.stringify({
                summary: summary,
                description: description,
                project: project,
                status: status,
                type: type,
                created_by: createdBy,
                assigned_to: assignedTo

            }),
            dataType: 'json',
            contentType: 'application/json',
            success: function (response, status) {
                console.log(response);
            },
            error: function (response, status) {
                console.log(response);
            }
        }
    );
}
function delete_issue(pk) {
    $.ajax({
            url: `http://localhost:8000/api/v1/issues/${pk}`,
            method: 'delete',
            headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
            dataType: 'json',
            contentType: 'application/json',
            success: function (response, status) {
                console.log(response);
            },
            error: function (response, status) {
                console.log(response);
            }
        }
    );
}
login('admin', 'admin');


