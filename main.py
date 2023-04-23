import itertools
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QSizePolicy
from PyQt6.QtCore import Qt, QRect, QTimer
from PyQt6.QtGui import QPainter, QCursor
import mainwindow as mw


# TODO
# Size of windows

class GridWidget(QWidget):
    def __init__(self, num_cells):
        super().__init__()
        self.num_cells = num_cells
        self.cell_size = 0
        self.setObjectName('grid_widget')
        self.cells = [['white' for _ in range(self.num_cells)] for _ in range(self.num_cells)]
        self.setMouseTracking(True)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.start = list()
        self.end = list()
        self.graph = dict()
        self.prevPath = list()
        self.path = list()
        self.all_ways = list()
        self.timer = QTimer()
        self.step_iter = None
        self.visualisation = False
        self.delay = 10
        self.algorithm = 'BFS'
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

        if event.key() == Qt.Key.Key_B:
            self.all_ways.clear()
            if len(self.start) == 2 and len(self.end) == 2:
                if self.cells[self.start[0]][self.start[1]] == 'red' \
                        and self.cells[self.end[0]][self.end[1]] == 'green':
                    if self.algorithm == 'BFS':
                        self.path = self.bfs(str(self.start[0]) + ',' + str(self.start[1]),
                                        str(self.end[0]) + ',' + str(self.end[1]))
                    elif self.algorithm == 'DFS':
                        self.path = self.dfs(str(self.start[0]) + ',' + str(self.start[1]),
                                        str(self.end[0]) + ',' + str(self.end[1]))

                    if (len(self.all_ways) != 0 and self.visualisation):
                        self.timer.setInterval(self.delay)
                        self.timer.timeout.connect(self.paint_step)
                        self.step_iter = self.step_generator().__iter__()
                        self.timer.start()
                    else:
                        self.paint_path(self.path)
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

    def clear_cells(self, cells):
        for cell in cells:
            x = int(cell.split(',')[0])
            y = int(cell.split(',')[1])
            if x == self.start[0] and y == self.start[1] or x == self.end[0] and y == self.end[1]:
                continue
            self.cells[x][y] = 'white'
        self.update()

    def step_generator(self):
        for item in self.all_ways:
            yield item

    def paint_step(self):
        if self.step_iter is not None:
            step = next(self.step_iter)
            if step == self.all_ways[-1]:
                self.step_iter = None
                self.timer.stop()
                self.clear_cells(self.all_ways)
                self.paint_path(self.path)
            x = int(step.split(',')[0])
            y = int(step.split(',')[1])
            if (x == self.start[0] and y == self.start[1] or x == self.end[0] and y == self.end[1]):
                return
            self.cells[x][y] = 'yellow'
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
                self.all_ways.append(node)
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

        return None

    def dfs(self, start, end):
        if start == end or start is None or end is None:
            return []
        visited = set()
        queue = [[start]]
        for path in queue:
            node = path[-1]
            if node == end:
                return path
            if node not in visited:
                self.all_ways.append(node)
                neighbours = self.graph[node]
                for neighbour in neighbours:
                    if len(neighbour) == 0 or self.cells[neighbour[0]][neighbour[1]] == 'black':
                        continue
                    new_path = list(path)
                    new_path.append(str(neighbour[0]) + ',' + str(neighbour[1]))
                    index = queue.index(path)
                    queue.insert(index+1,new_path)

                visited.add(node)

        return None

class MainWindow(QMainWindow):
    def __init__(self, num_cells):
        super().__init__()
        self.grid_widget = GridWidget(num_cells)
        self.ui = mw.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.gridLayout_2.addWidget(self.grid_widget)
        self.grid_widget.setStyleSheet("QWidget#grid_widget{color: FFF;}")
        self.grid_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.grid_widget.setMinimumSize(600, 600)
        self.ui.checkBox.stateChanged.connect(self.change_visualization)
        self.ui.spinBox.valueChanged.connect(self.change_delay)
        self.ui.comboBox.currentIndexChanged.connect(self.change_path_algorithm)
        self.resize(self.minimumSize())
        self.setFixedSize(self.size())

    def change_path_algorithm(self, index):
        self.grid_widget.algorithm = self.ui.comboBox.currentText()

    def change_visualization(self, state):
        self.grid_widget.visualisation = state

    def change_delay(self, value):
        self.grid_widget.delay = value


if __name__ == '__main__':
    app = QApplication(sys.argv)

    num_cells = 50

    window = MainWindow(num_cells)
    window.setWindowTitle("Pathfinding")
    window.show()

    sys.exit(app.exec())
