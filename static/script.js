function makeMove(row, col) {
    fetch("/move", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ row: row, col: col })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            updateBoard();
            if (data.winner) {
                document.getElementById("status").innerText = `Jogador ${data.winner} venceu!`;
            }
        } else {
            alert("Jogada inválida!");
        }
    });
}

function resetGame() {
    fetch("/reset", { method: "POST" })
    .then(() => {
        updateBoard();
        document.getElementById("status").innerText = "";
    });
}

function updateBoard() {
    document.getElementById("board").src = "/board_image?" + new Date().getTime();  // Atualiza a imagem
}
