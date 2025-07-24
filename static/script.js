function makeMove(row, col) {
    fetch("/move", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ row: row, col: col })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            renderBoard(data.board);
            if (data.winner) {
                document.getElementById("status").innerText = `Jogador ${data.winner} venceu!`;
            }
        } else {
            alert("Jogada inválida!");
        }
    });
}

function startGame() {
    fetch("/start", { method: "POST" })
    .then(response => response.json())
    .then(data => {
        renderBoard(data.board);
        document.getElementById("status").textContent = "Jogo iniciado!";
    });
}

function updateBoard() {
    document.getElementById("board").src = "/board_image?" + new Date().getTime();  // Atualiza a imagem
}
    
function resetGame() {
    alert("Game reset!");
    fetch("/reset", { method: "POST" })
    .then(() => {
        updateBoard();
        document.getElementById("status").innerText = "";
    });
}


function renderBoard(board) {
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            const btn = document.querySelector(`#grid button[data-row='${row}'][data-col='${col}']`);
            btn.textContent = board[row][col] || " ";
        }
    }
}