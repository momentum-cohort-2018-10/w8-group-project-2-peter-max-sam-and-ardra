function quizhtml (card) {
    return `
    <div class = "thiscard tc">
        <div class="front">  ${card.question} </div>
        <div class="back">  ${card.answer} </div>
    </div>
    `
}

function redoQuiz () {
    return `
    <button id='redobutton' class="button is-large is-outlined avenir tc" >play again?</button>
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
        $('.back').hide()
  }
}

$('#nextcard').on("click", function() {
    flipThroughCards();
});

$('#apple').on("click", function() {
    flipover();
});

function flipover() {
    $('.front, .back').toggle() 
}

$('#rightbutton').on("click", function() {
    console.log('right button clicked')
    rightButton()
});

function rightButton() {
    console.log('rightbuttonworks')
    $.ajax({
        url: "/api/cards/1/",
        method: 'PATCH',
        data: card.rightanswers += 1,
        contentType: 'application/json'
    })
}


function setupCSRFAjax () {
    var csrftoken = Cookies.get('csrftoken')
  
    $.ajaxSetup({
      beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader('X-CSRFToken', csrftoken)
        }
      }
    })
  }


function csrfSafeMethod (method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
  }

function loadPage () {
    loadQuizData()
    setupCSRFAjax()
}

loadPage()

