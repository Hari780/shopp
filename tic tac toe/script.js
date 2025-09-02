let cells = document.querySelectorAll('.cell')
let status = document.querySelector('.status')
let turn = "X"

status.textContent = "Player X's turn"

cells.forEach(cell => {
  cell.onclick = () => {
    if (cell.textContent || winner() || turn === "O") return
    cell.textContent = turn
    if (winner()) {
      status.textContent = `Player ${turn} wins!`
    } else {
      turn = "O"
      status.textContent = `Player O's turn`
      setTimeout(playO, 500)
    }
  }
})

function playO() {
  let empty = [...cells].filter(c => !c.textContent)
  if (!empty.length) return
  let choice = empty[Math.floor(Math.random() * empty.length)]
  choice.textContent = "O"
  if (winner()) {
    status.textContent = "Player O wins!"
  } else {
    turn = "X"
    status.textContent = "Player X's turn"
  }
}

function winner() {
  let p = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  return p.some(c =>
    cells[c[0]].textContent &&
    cells[c[0]].textContent === cells[c[1]].textContent &&
    cells[c[0]].textContent === cells[c[2]].textContent
  )
}
