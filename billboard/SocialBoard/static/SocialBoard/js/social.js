$(document).ready(function () {
    addNewPost()
})

function addNewPost() {
    var postInputs = $("#new-post-input-wrapper")
    var newPost = $("#new-post-btn")
    newPost.click(function () {
        postInputs.removeClass("hide")
        postInputs.addClass("new-post-input-wrapper")
        var title = $("<input>")
        var content = $("<input>")
        var submit = $("<button>")
        var titleTitle = $("<div>")
        var contentTitle = $("<div>")
        title.attr("type", "text").attr("id", "new-post-title")
        content.attr("type", "text").attr("id", "new-post-content")
        submit.attr("id", "submit-new-post")
        titleTitle.text("Post Title")
        contentTitle.text("Post Text")
        submit.text("Submit")
        submit.click(function () {
            var newTitle = $("#new-post-title")
            var newContent = $("#new-post-content")
            submitNewPost(newTitle[0].value,newContent[0].value)
        })
        titleTitle.appendTo(postInputs)
        title.appendTo(postInputs)
        contentTitle.appendTo(postInputs)
        content.appendTo(postInputs)
        submit.appendTo(postInputs)
        window.scrollBy(0, 200);
        newPost.attr("disabled", true)
    })
}
function submitNewPost(title, text) {
    $.ajax({
        type: "POST",
        url: "/socialbd/userAddedPost",
        headers: {"X-CSRFToken": csrf},
        data: {
            title: title,
            content: text,
            author: author
        },
        success: function(response) {
            window.location.reload()
        },
        error: function(response) {
            console.log(response)
        }
    })
}