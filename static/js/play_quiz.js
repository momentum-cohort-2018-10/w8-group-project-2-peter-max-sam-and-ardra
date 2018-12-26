function quizhtml (card) {
    return `
    <div class = "container box thiscard">
        <div class="front"> The question is: ${card.question} </div>
        <div class="back"> The answer is: ${card.answer} </div>
    </div>
    `
}

function randCard(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

let quizNum = quizNumber

let cardList = document.getElementById('card')
let cardQuestion = document.getElementById('question')
let cardAnswer = document.getElementById('answer')


function loadQuizData () {
    $.get(`/api/quizzes/${quizNum}`)
      .then(function (quiz) {
        let numOfCards = randCard(quiz.cards.length)
        console.log(numOfCards)
        const cardPile = (quiz.cards)
        console.log(cardPile[1])
        let currentCard = quiz.cards[numOfCards]
        cardList.innerHTML = quizhtml(currentCard)
        $('.back').hide();
    })
}

    //     for (card of quiz.cards) {
    //         cardHTML = quizhtml(card)
    //         cardStock = document.createElement('div')
    //         cardStock.classList.add('cardStock')
    //         $(cardStock).attr('id', `cardnumber${counter}`)
    //         cardStock.innerHTML = cardHTML
    //         cardList.appendChild(cardStock)
    //         counter += 1
    //     }


$('#nextcard').on("click", function() {
    loadQuizData();
});

$('#card').on("click", function() {
    flipover();
});

// function loadRandomArray () {
//     $.get(`/api/quizzes/${quizNum}`)
//       .then(function (quiz) {
//         for  (let card of quiz.cards) {
            
//         } 



function flipover() {
    // $('.back').hide();
    // $('.front, .back').on( 'click', function() {
    $('.front, .back').toggle() 
    // })
}

function loadPage () {
    loadQuizData()
}

loadPage()
