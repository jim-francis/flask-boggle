
$('#submit-form').submit(async function(e){
    e.preventDefault();
    let word = getWord()
    // let res = await axios.get("/check-word", { params: { word: word }})
    let res = await getResponse(word)
    checkWord(res)
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

function checkWord(res){
    if (res === "not-word"){
        postMessage("Not a word", "error")
    } else if (res === "not-on-board"){
        postMessage("Invalid word", "error")
    } else {
        postMessage("Score!", "success")
    }
}

function postMessage(message, style){
    $(".messages").text(message).removeClass().addClass(`message ${style}`)
}