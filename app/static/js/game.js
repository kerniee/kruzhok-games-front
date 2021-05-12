$("#start_analysis_button")[0].onclick = () => {
    $("#start_analysis_button").remove()
    $("#start_analysis").append("<div class='loader mt-3'></div>")
    setTimeout(() => {
        let text_block = $(".text-block");
        $(".loader").remove();
        $("#start_analysis").append("<h4>Общий командный рейтинг: <a>89%<a></h4>")
        $("#start_analysis").append("<h4>Вы хороший командный игрок!</h4>")
        text_block.css("visibility", "visible");
        text_block.css("height", "auto");
        text_block.css("padding", "3rem");
    }, 1000);
}