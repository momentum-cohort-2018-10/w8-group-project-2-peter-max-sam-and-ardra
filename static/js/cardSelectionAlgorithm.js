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