<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>لعبة XO مشوقة</title>
    <style>
        * {
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
        }

        body {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }

        h1 {
            margin-bottom: 20px;
            font-size: 2.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .status {
            margin-bottom: 20px;
            font-size: 1.25rem;
            font-weight: bold;
            background: rgba(255, 255, 255, 0.1);
            padding: 10px 20px;
            border-radius: 50px;
            backdrop-filter: blur(5px);
        }

        .board {
            display: grid;
            grid-template-columns: repeat(3, 100px);
            grid-template-rows: repeat(3, 100px);
            gap: 10px;
            background-color: rgba(255, 255, 255, 0.05);
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        }

        .cell {
            background-color: #fff;
            border: none;
            border-radius: 8px;
            font-size: 2.5rem;
            font-weight: bold;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.1s directly, background-color 0.2s;
        }

        .cell:hover {
            background-color: #e0e0e0;
        }

        .cell:active {
            transform: scale(0.95);
        }

        .cell.X {
            color: #ff4b5c;
        }

        .cell.O {
            color: #05dfd7;
        }

        .reset-btn {
            margin-top: 25px;
            padding: 12px 30px;
            font-size: 1rem;
            font-weight: bold;
            color: #1e3c72;
            background-color: #fff;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            transition: all 0.2s ease;
        }

        .reset-btn:hover {
            background-color: #05dfd7;
            color: #fff;
            transform: translateY(-2px);
        }
    </style>
</head>
<body>

    <h1>لعبة X O</h1>
    <div class="status" id="status">دور اللاعب: X</div>

    <div class="board" id="board">
        <button class="cell" data-index="0"></button>
        <button class="cell" data-index="1"></button>
        <button class="cell" data-index="2"></button>
        <button class="cell" data-index="3"></button>
        <button class="cell" data-index="4"></button>
        <button class="cell" data-index="5"></button>
        <button class="cell" data-index="6"></button>
        <button class="cell" data-index="7"></button>
        <button class="cell" data-index="8"></button>
    </div>

    <button class="reset-btn" id="resetBtn">إعادة اللعب</button>

    <script>
        const board = document.getElementById('board');
        const cells = document.querySelectorAll('.cell');
        const statusText = document.getElementById('status');
        const resetBtn = document.getElementById('resetBtn');
        
        let currentPlayer = 'X';
        let gameState = ["", "", "", "", "", "", "", "", ""];
        let isGameActive = true;

        const winningConditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], // الصفوف
            [0, 3, 6], [1, 4, 7], [2, 5, 8], // الأعمدة
            [0, 4, 8], [2, 4, 6]             // الأقطار
        ];

        function handleCellClick(e) {
            const clickedCell = e.target;
            const clickedCellIndex = parseInt(clickedCell.getAttribute('data-index'));

            if (gameState[clickedCellIndex] !== "" || !isGameActive) {
                return;
            }

            gameState[clickedCellIndex] = currentPlayer;
            clickedCell.textContent = currentPlayer;
            clickedCell.classList.add(currentPlayer);

            checkResult();
        }

        function checkResult() {
            let roundWon = false;

            for (let i = 0; i < winningConditions.length; i++) {
                const winCondition = winningConditions[i];
                let a = gameState[winCondition[0]];
                let b = gameState[winCondition[1]];
                let c = gameState[winCondition[2]];

                if (a === '' || b === '' || c === '') {
                    continue;
                }
                if (a === b && b === c) {
                    roundWon = true;
                    break;
                }
            }

            if (roundWon) {
                statusText.textContent = `مبروك! اللاعب ${currentPlayer} هو الفائز! 🎉`;
                statusText.style.color = '#05dfd7';
                isGameActive = false;
                return;
            }

            let roundDraw = !gameState.includes("");
            if (roundDraw) {
                statusText.textContent = "تعادل! لا يوجد فائز 🤝";
                isGameActive = false;
                return;
            }

            // تبديل الأدوار
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            statusText.textContent = `دور اللاعب: ${currentPlayer}`;
        }

        function resetGame() {
            currentPlayer = 'X';
            gameState = ["", "", "", "", "", "", "", "", ""];
            isGameActive = true;
            statusText.textContent = `دور اللاعب: ${currentPlayer}`;
            statusText.style.color = '#fff';
            cells.forEach(cell => {
                cell.textContent = "";
                cell.classList.remove('X', 'O');
            });
        }

        cells.forEach(cell => cell.addEventListener('click', handleCellClick));
        resetBtn.addEventListener('click', resetGame);
    </script>
</body>
</html>
