document.getElementById('solve-button').addEventListener('click', async () => {
    const inputs = document.querySelectorAll('input');
    let board = [];
    let row = [];

    // 1. Gather all the numbers from the grid
    inputs.forEach((input, index) => {
        // If empty, treat it as a 0
        let val = input.value ? parseInt(input.value) : 0;
        row.push(val);
        
        // Every 9 items, push the row to the board and start a new row
        if ((index + 1) % 9 === 0) {
            board.push(row);
            row = [];
        }
    });

    // 2. Send the board to our Python backend using Fetch API
    const response = await fetch('/solve', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ board: board })
    });

    const data = await response.json();

    // 3. Handle the response from Python
    if (data.status === 'success') {
        const solvedBoard = data.solved_board;
        // Fill the HTML inputs with the solved numbers
        inputs.forEach((input, index) => {
            const r = Math.floor(index / 9);
            const c = index % 9;
            input.value = solvedBoard[r][c];
        });
    } else {
        alert("This puzzle cannot be solved! Check your numbers.");
    }

    //Reset button functionality
    document.getElementById('reset-button').addEventListener('click', () => {
        inputs.forEach(input => input.value = '');
    });
});