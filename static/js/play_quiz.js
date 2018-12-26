function quizhtml (card) {
    return `
    <div class = "container box thiscard">
        <div class="front"> The question is: ${card.question} </div>
        <div class="back"> The answer is: ${card.answer} </div>
    </div>
    `
}

function redoQuiz () {
    return `
    <button id='redobutton'>play again?</button>
    `
}

function randCard(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

let quizNum = quizNumber

let cardList = document.getElementById('card')
let cardQuestion = document.getElementById('question')
let cardAnswer = document.getElementById('answer')

let cardPile = []
let usedPile = []

function loadQuizData () {
    console.log('loading!')
    $.get(`/api/quizzes/${quizNum}`)
      .then(function (quiz) {
        cardPile = (quiz.cards)
        usedPile = []
        flipThroughCards()
    })
}

function flipThroughCards () {
    console.log('flipping!')
    if (cardPile.length == 0) {
        cardList.innerHTML = redoQuiz()
        let redo = document.getElementById('redobutton')
        redo.addEventListener('click', function (event) {
            loadQuizData()
        })
    } else {
        let numOfCards = randCard(cardPile.length)
        let currentCard = cardPile[numOfCards]
        cardList.innerHTML = quizhtml(currentCard)
        usedPile.push(currentCard)
        cardPile.splice(numOfCards, 1)
        console.log(numOfCards)
        console.log(cardPile)
        console.log(usedPile)
        $('.back').hide();
  }
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
    flipThroughCards();
});

$('#card').on("click", function() {
    flipover();
});

// $().on("click", function() {
//     console.log('fuckjquery');
// });




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
