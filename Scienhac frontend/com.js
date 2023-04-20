const postID = '943659869113432918';
const blogID = '9160331485130872315';
const apiKey = 'AIzaSyDZhYG2aZx-9XbFzJHi0H6Xjqn2Ntvbbqo';
var commentData = {
    'content': 'This is a test comment.'
};

const requestUrl = `https://www.googleapis.com/blogger/v3/blogs/${blogID}/posts/${postID}/comments?key=${apiKey}`;

// Make the request to insert the comment
fetch(requestUrl, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(commentData)
})
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
