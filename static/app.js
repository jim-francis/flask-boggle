
$('#submit-form').submit(async function(e){
    e.preventDefault();
    let word = getWord()
    const res = await axios.get("/check-word", { params: { word: word }})
    console.log(res)
});

function getWord(){
    const $word = $(".word").val()
    return $word
}