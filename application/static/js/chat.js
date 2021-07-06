var chatDiv = document.getElementsByClassName('messages')[0];
chatDiv.scrollTop = chatDiv.scrollHeight;

var socket = io("http://127.0.0.1:5000");
socket.on("connect", () => {
    socket.emit("event", {data: "I\"m connected!"});
});

document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();

    socket.emit("sendMessage", { message: event.target[0].value })
    event.target[0].value = ""

});

socket.on("getMessage", (msg) => {
    const span = document.createElement("div");
    const messages = document.querySelector(".messages");

    span.innerHTML = `<strong>${msg.name}:</strong><span>${msg.message}</span>`
    messages.append(span)

    const scroll = document.querySelector("#box")
    scroll.scrollTo(0, (scroll.scrollHeight - scroll.clientHeight))
});