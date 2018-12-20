/* global fetch, $, books  */


let test = document.getElementById('test')


test.addEventListener('click', function (event) {
    searchApi()
})

function searchApi (event) {
    $.ajax({
        dataType: 'json',
        url: 'localhost:8000/api/quizzes', 
        data: {},
        success: console.log('yay')
    })
}