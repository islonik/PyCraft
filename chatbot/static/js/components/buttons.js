/**
 * Add vertically stacked buttons as a bot response
 */
function addButtons(buttons) {
    setTimeout(() => {

        if (buttons[0].payload == "default") {
            $(
                '<div class="singleCardNew">' +
                    '<div class="buttons">' +
                        '<div class="menuNew"></div>' +
                    '</div>' +
                '</div>'
            )
            .appendTo(".chats")
            .hide()
            .fadeIn(1000);

            $(
                `
                <a class="action-button">
                    <li class="buttonTmplContentChild outer-child">Types</li>
                    <ul class="action-button-inner hidden">
                        <li class="buttonTmplContentChild"
                            value="Table"
                            actual-value="Table"
                            type="postback">Table</li>
                    </ul>
                </a>
                `
            ).appendTo(".menuNew");

            addEvent();
        }

        scrollToBottomOfResults();
    }, 1000);
}

function addEvent() {
    $(".outer-child").click(function() {
        $(".outer-child").not(this).next("ul").hide();
        $(this).next("ul").toggle();
    });

    $(".inner-child").click(function() {
        let header = $(this);
        let cont = header.next();
        cont.slideToggle(200, function() {});
    });

    $(".menuNew li:not(.outer-child):not(.inner-child)").off("click").on("click", function(e) {
        let type = $(this).attr("type");
        let msgText = $(this).text();
        if (type == "postback") {
            setUserResponse(msgText);
            send(msgText);
        }
    });
}

$(document).on("click", ".menu .menuChips", function() {
    const text = this.innerText;
    const payload = this.getAttribute("data-payload");
    setUserResponse(text);
    send(payload);
});