// 변수값 정의의
let computerNum = 0;
let userInput = document.getElementById("user-input")
let playButton = document.getElementById("play-button")
let resultText = document.getElementById("result-text")
let chanceArea = document.getElementById("chance-area")
let resetButton = document.getElementById("reset-button")
let mainImg = document.getElementsByClassName("main-img")
let resultAreaImg = document.querySelector(".main-img"); //이게 뭘까?
let gameOver = false;
let chances = 5
let userValuelist = []


//랜덤 숫자 뽑기
function pickrandomNum(){
    computerNum = Math.floor(Math.random()*100)+1;
    console.log(computerNum);
}

playButton.addEventListener("click",play)
resetButton.addEventListener("click",reset)
userInput.addEventListener("focus",focusInput)

//숫자추측하기
function play(){
    const userValue = userInput.value;

    if(userValue<1 || userValue>100){
        resultText.textContent = "1과 100사이값을 입력 바랍니다."
        return
    }

    if(userValuelist.includes(userValue)){
        resultText.textContent = "이미 입력한 숫자입니다.다시 입력해주세용."
        return
    }

    if(chances == 1){
        gameOver = true;
    }

    chances --;
    userValuelist.push(userValue)
    chanceArea.textContent = `남은 기회:${chances}`

    if(userValue < computerNum) {
        resultAreaImg.src= "https://media0.giphy.com/media/3ov9jExd1Qbwecoqsg/200.gif";
        resultText.textContent = "UP!!";
    } else if(userValue > computerNum){
        resultAreaImg.src = "https://media.giphy.com/media/r2puuhrnjG7vy/giphy.gif";
        resultText.textContent = "Down!!"
    } else {
        resultAreaImg.src =
            "https://media.tenor.com/images/0a81b89954678ebe228e15e35044f7a5/tenor.gif";
        resultText.textContent = "That’s right!"
        gameOver = true;
    }

    if(gameOver == true){
        playButton.disabled = true;
    }


    console.log(userValuelist)
}

//reset 기능
function reset(){
    resultText.textContent = "죽기 싫다면 맞춰라"
    chances = 5
    chanceArea.textContent = `남은 기회:${chances}`
    playButton.disabled = false;
    pickrandomNum()
    userInput.value = ""
    userValuelist = []
}


//focus 지우기
function focusInput(){
    userInput.value = ""
}

pickrandomNum()