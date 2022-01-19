let score = 0

$('#submit-form').on("submit", async function(e){
    e.preventDefault();
    let word = getWord()
    let res = await getResponse(word)
    await checkWord(res)
    if(res === "ok"){
        handleScore(word)
    }
    $(".word").val("").focus()
});

function getWord(){
    const $word = $(".word").val()
    return $word
}

async function getResponse(word){
    let res = await axios.get("/check-word", { params: { word: word }})
    return res.data.result
}

async function checkWord(res){
    if (res === "not-word"){
        postMessage("Not a word", "error")
    } else if (res === "not-on-board"){
        postMessage("Invalid word", "error")
    } else {
        postMessage("Score!", "success")
    }
}

function postMessage(message, style){
    console.log(message, style)
    $("#messages").text(message).removeClass().addClass(`message ${style}`)
}

function handleScore(word){
    score+= word.length
    $("#score").text(score)
}