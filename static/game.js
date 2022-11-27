let words=[
    

]


$(document).ready(function () {
    getTemplates()
})

function getTemplates() {
    $.ajax({
        url: "/get-template",
        type: "get",
        success: function (result) {
            game(result.word)
        },
        error: function (result) {
            alert(result.responseJSON.message)
        }
    })
}

function game(randomWord) {


    $("#blanks").empty()

    for(i=0;i<randomWord.inputs;i++){
        let input_html=`<span class="fill_blanks" id="input_${i}">_</span>`
        $("#blanks").append(input_html)
    }

    $("#hint").html(randomWord.category)

    var gameOver = false;

    //fill the blanks only when the character is crct
    $(".clickable").click(function () {
        var correctGuess = false;

        //getting the id of the clicked button
        let id = $(this).attr("id")

        var life = parseInt($("#life").text())

        //looping through all the letters in the word
        for(var i=0;i<randomWord.word.length;i++){
            //check whether the character matches the id of button
            if(randomWord.word.charAt(i).toLowerCase()==id){
                //check life>0 & blank is empty/filled
                if (life > 0 && ($(".fill_blanks").eq(i).html() == "_" || $(".fill_blanks").eq(i).html() == id)) {

                    //fill blanks
                    $(".fill_blanks").eq(i).html(id);
                    correctGuess = true;

                    if ($("#blanks").text() === randomWord.word.toLowerCase()) {
                        $("#result").text("You Win!!")
                        correctGuess = true;
                        gameOver=true
                    }
                }
            }
        }

        if (life > 0 && correctGuess!=true && gameOver!=true) {           
            life = life - 1
            $("#life").text(life)
        }
        else if (life===0) {
            $("#result").text("You Lost!!")
            $("#correctAns").text(`Correct Answer: ${randomWord.word}`)
        }
    

    })
}