const converter = new showdown.Converter();

function scrollToBottomOfResults() {
    const terminalResultDiv = document.getElementById("chats");
    terminalResultDiv.scrollTop = terminalResultDiv.scrollHeight;
}