
async function makeRequest(url, method='GET') {    let response = await fetch(url, {method});
    if (response.ok) {
        return await response.json();    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;    }
}

async function ButtonClick(event) {
    let target = event.target;
    let url = target.dataset.indexLink;
    let id = target.dataset.article;
    let response = await makeRequest(url);
    console.log(response)

}

async function CommentButtonClick(event) {
    let target = event.target;
    let url = target.dataset.indexLink;
    let id = target.dataset.comment;
    let response = await makeRequest(url);
    console.log(response)
}