document.addEventListener("DOMContentLoaded", () => {
    const squares = document.querySelectorAll('.square');
    const status = document.getElementById('status');
    const restartButton = document.getElementById('restartButton');

    function renderBoard(board) {
        for (let row = 0; row < 3; row++) {
            for (let col = 0; col < 3; col++) {
                const btn = document.querySelector(`.square[data-row='${row}'][data-col='${col}']`);
                btn.textContent = board[row][col] || "";
            }
        }
    }

    function updateStatus(winner) {
        if (winner === null) {
            status.textContent = "Sua vez!";
        } else if (winner === "X" || winner === "O") {
            status.textContent = `Game over! ${winner} venceu!`;
        } else if (winner === "Empate" || winner === "Tie") {
            status.textContent = "Empate!";
        }
    }

    function makeMove(row, col) {
        fetch("/move", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ row, col })
        })
        .then(res => res.json())
        .then(data => {
            renderBoard(data.board);
            if (data.winner) {
                updateStatus(data.winner);
                disableBoard();
            } else {
                updateStatus(null);
            }
        });
    }

    function disableBoard() {
        squares.forEach(btn => btn.disabled = true);
    }

    function enableBoard() {
        squares.forEach(btn => btn.disabled = false);
    }

    function startGame() {
        fetch("/start", { method: "POST" })
        .then(res => res.json())
        .then(data => {
            renderBoard(data.board);
            enableBoard();
            updateStatus(null);
        });
    }

    squares.forEach(btn => {
        btn.addEventListener('click', function() {
            if (this.textContent === "") {
                makeMove(
                    parseInt(this.getAttribute('data-row')),
                    parseInt(this.getAttribute('data-col'))
                );
            }
        });
    });

    restartButton.addEventListener('click', startGame);

    // Start game on page load
    startGame();
});