var question = [
    {
        prompt:"百鬼大小姐摔過誰?\n(a)爸爸\n(b)爺爺\n(c)大空昴\n(d)湊阿庫亞",
        answer:"a"
    },
    {
        prompt:"百鬼大小姐對壓歲錢做過什麼事?\n(a)把壓歲錢吃掉\n(b)喜歡壓歲錢袋子，把錢丟掉\n(c)錢臭臭的，用洗碗精洗錢\n(d)不喜歡壓歲錢，偷偷丟掉",
        answer:"b"
    },
    {
        prompt:"百鬼大小姐考英檢時，考官做了什麼事?\n(a)大小姐太可愛了，直接讓她過\n(b)大小姐不知道說了什麼讓考官笑出來了\n(c)大小姐走錯考場，被考官請出去\n(d)被考官認出要簽名",
        answer:"b"
    },
    {
        prompt:"百鬼大小姐的個性如何?\n(a)溫柔體貼\n(b)色色的\n(c)大大方方\n(d)我行我素",
        answer:"d"
    },
]
var score = 0;
for(var i=0; i<question.length; i++){
    var input=prompt(question[i].prompt);
    if(input==question[i].answer){
        score++;
        alert("答對了!");
    }
    else{
        alert("答錯了!");
    }
}
alert("總共答對"+ score + "題");
window.history.go(-1)