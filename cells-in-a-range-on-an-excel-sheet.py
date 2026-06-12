def cellsInRange(s: str):
    start, end = s.split(':')
    start_col, start_row = ord(start[0]) - 64, int(start[1])
    end_col, end_row = ord(end[0]) - 64, int(end[1])
    
    result = []
    for col in range(start_col, end_col + 1):
        for row in range(start_row, end_row + 1):
            result.append(chr(col + 64) + str(row))
    
    return result