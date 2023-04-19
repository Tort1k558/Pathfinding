import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPainter, QCursor

# TODO
# Size of windows

class GridWidget(QWidget):
    def __init__(self, num_cells):
        super().__init__()
        self.num_cells = num_cells
        self.cell_size = 0
        self.cells = [['white' for _ in range(self.num_cells)] for _ in range(self.num_cells)]
        self.setMouseTracking(True)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFixedSize(900, 900)
        self.start = list()
        self.end = list()
        self.graph = dict()
        self.prevPath = list()

        # init graph
        for i in range(self.num_cells):
            for k in range(self.num_cells):
                left = [i, k - 1]
                right = [i, k + 1]
                down = [i - 1, k]
                up = [i + 1, k]
                # Exclusion of exit from borders
                if left[0] < 0 or left[0] >= self.num_cells or left[1] < 0 or left[1] >= num_cells:
                    left = []
                if right[0] < 0 or right[0] >= self.num_cells or right[1] < 0 or right[1] >= num_cells:
                    right = []
                if down[0] < 0 or down[0] >= self.num_cells or down[1] < 0 or down[1] >= num_cells:
                    down = []
                if up[0] < 0 or up[0] >= self.num_cells or up[1] < 0 or up[1] >= num_cells:
                    up = []

                self.graph[str(i) + ',' + str(k)] = [left, right, down, up]

    def resizeEvent(self, event):
        self.cell_size = min(self.width() // self.num_cells, self.height() // self.num_cells)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.GlobalColor.white)
        painter.drawRect(QRect(0, 0, self.width(), self.height()))

        for i in range(self.num_cells):
            for j in range(self.num_cells):
                if self.cells[i][j] == 'black':
                    painter.setBrush(Qt.GlobalColor.black)
                elif self.cells[i][j] == 'white':
                    painter.setBrush(Qt.GlobalColor.white)
                elif self.cells[i][j] == 'red':
                    painter.setBrush(Qt.GlobalColor.red)
                elif self.cells[i][j] == 'green':
                    painter.setBrush(Qt.GlobalColor.green)
                elif self.cells[i][j] == 'yellow':
                    painter.setBrush(Qt.GlobalColor.yellow)

                painter.drawRect(QRect(i * self.cell_size, j * self.cell_size,
                                       self.cell_size, self.cell_size))

    def mousePressEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            x = event.pos().x() // self.cell_size
            y = event.pos().y() // self.cell_size
            if 0 <= x < self.num_cells and 0 <= y < self.num_cells:
                self.cells[x][y] = 'black'
            self.update()
        if event.buttons() == Qt.MouseButton.RightButton:
            x = event.pos().x() // self.cell_size
            y = event.pos().y() // self.cell_size
            if 0 <= x < self.num_cells and 0 <= y < self.num_cells:
                self.cells[x][y] = 'white'
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            x = event.pos().x() // self.cell_size
            y = event.pos().y() // self.cell_size
            if 0 <= x < self.num_cells and 0 <= y < self.num_cells:
                self.cells[x][y] = 'black'
            self.update()
        if event.buttons() == Qt.MouseButton.RightButton:
            x = event.pos().x() // self.cell_size
            y = event.pos().y() // self.cell_size
            if 0 <= x < self.num_cells and 0 <= y < self.num_cells:
                self.cells[x][y] = 'white'
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.update()

    def keyPressEvent(self, event):
        # Set start of path
        if event.key() == Qt.Key.Key_S:
            x = self.mapFromGlobal(QCursor.pos()).x() // self.cell_size
            y = self.mapFromGlobal(QCursor.pos()).y() // self.cell_size
            if 0 > x or x >= num_cells or 0 > y or y >= num_cells:
                print('out')
                return
            if len(self.start) != 0:
                self.cells[self.start[0]][self.start[1]] = 'white'
            self.start = [x, y]
            self.cells[x][y] = 'red'
            self.update()
        # Set end of path
        if event.key() == Qt.Key.Key_E:
            x = self.mapFromGlobal(QCursor.pos()).x() // self.cell_size
            y = self.mapFromGlobal(QCursor.pos()).y() // self.cell_size
            if 0 > x or x >= num_cells or 0 > y or y >= num_cells:
                print('out')
                return
            if len(self.end) != 0:
                self.cells[self.end[0]][self.end[1]] = 'white'
            self.end = [x, y]
            self.cells[x][y] = 'green'
            self.update()

        # BFS
        if event.key() == Qt.Key.Key_B:
            path = self.bfs(str(self.start[0]) + ',' + str(self.start[1]), str(self.end[0]) + ',' + str(self.end[1]))
            self.paint_path(path)
        # Clear and fill canvas
        if event.key() == Qt.Key.Key_C:
            self.clear_canvas()
        if event.key() == Qt.Key.Key_X:
            self.fill_canvas()

    def clear_canvas(self):
        for x in range(self.num_cells):
            for y in range(self.num_cells):
                self.cells[x][y] = 'white'
                self.start = list()
                self.end = list()
                self.prevPath = list()
                self.update()

    def fill_canvas(self):
        for x in range(self.num_cells):
            for y in range(self.num_cells):
                self.cells[x][y] = 'black'
                self.start = list()
                self.end = list()
                self.prevPath = list()
                self.update()

    def paint_path(self, path):
        if self.prevPath:
            for index, cell in enumerate(self.prevPath):
                if index == 0 or index == len(self.prevPath) - 1:  # no need to paint over the first and last
                    continue
                x = int(cell.split(',')[0])
                y = int(cell.split(',')[1])
                if self.cells[x][y] == 'black':
                    continue
                self.cells[x][y] = 'white'
                self.update()
        for index, cell in enumerate(path):
            if index == 0 or index == len(path) - 1:
                continue
            x = int(cell.split(',')[0])
            y = int(cell.split(',')[1])
            self.cells[x][y] = 'yellow'
            self.update()
        self.prevPath = path

    def bfs(self, start, end):
        if start == end or start is None or end is None:
            return []
        visited = set()
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]

            if node not in visited:
                neighbours = self.graph[node]

                for neighbour in neighbours:
                    if len(neighbour) == 0 or self.cells[neighbour[0]][neighbour[1]] == 'black':
                        continue
                    new_path = list(path)
                    new_path.append(str(neighbour[0]) + ',' + str(neighbour[1]))
                    queue.append(new_path)
                    if str(neighbour[0]) + ',' + str(neighbour[1]) == end:
                        return new_path

                visited.add(node)

        return []


class MainWindow(QMainWindow):
    def __init__(self, num_cells):
        super().__init__()
        self.grid_widget = GridWidget(num_cells)
        self.setCentralWidget(self.grid_widget)
        self.setWindowTitle("Pathfinding")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    num_cells = 200

    window = MainWindow(num_cells)
    window.show()

    sys.exit(app.exec())
