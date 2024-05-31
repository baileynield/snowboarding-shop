import json

from fastapi import FastAPI

from models import Board, Brand


app = FastAPI()

with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

boards: list[Board] = []

for board in snowboard_list:
    boards.append(Board(**board))


@app.get("/boards")
async def get_boards() -> list[Board]:
    return boards

@app.post("/boards")
async def create_boards(board: Board) -> None:
    boards.append(board)

@app.put("/boards/{board_id}")
async def update_board(board_id: int, updated_board: Board) -> None:
    for i, board in enumerate(boards):
        if board.id == board_id:
            boards[i] = updated_board
            return
        else:
            boards.apppend(updated_board)

@app.delete("/boards/{board_id}")
async def delete_boards(board_id: int) -> None:
    for i, board in enumerate(boards):
        if board.id == board_id:
            boards.pop(i)