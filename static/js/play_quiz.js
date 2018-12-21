function quizhtml (card) {
    return `
    <div class = "container box thiscard">
        <div class = "subtitle front"> The question is: ${card.question} </div>
        <div class = "subtitle back"> The answer is: ${card.answer} </div>
    </div>
    `
}


function randCard(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

let quizNum = quizNumber

cardList = document.getElementById('cardlist')
cardQuestion = document.getElementById('question')
cardAnswer = document.getElementById('answer')


function loadQuizData () {
    $.get(`/api/quizzes/${quizNum}`)
      .then(function (quiz) {
        let numOfCards = randCard(quiz.cards.length)
        currentCard = quiz.cards[numOfCards]
        console.log(currentCard.question)
        cardQuestion.innerText = currentCard.question
        cardAnswer.innerText = currentCard.answer
        



    //     for (card of quiz.cards) {
    //         cardHTML = quizhtml(card)
    //         cardStock = document.createElement('div')
    //         cardStock.classList.add('cardStock')
    //         $(cardStock).attr('id', `cardnumber${counter}`)
    //         cardStock.innerHTML = cardHTML
    //         cardList.appendChild(cardStock)
    //         counter += 1
    //     }
    })
}

$('#nextcard').on("click", function() {
    loadQuizData();
});





function flipover() {
    $('.back').hide();

$('.front, .back').on( 'click', function() {
    $('.front, .back').toggle() 
})
}

function loadPage () {
    loadQuizData()
    flipover()
}

loadPage()
