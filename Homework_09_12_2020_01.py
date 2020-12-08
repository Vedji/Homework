from tkinter import *
# by Veji

number = [[1, 1, 1, 1, 1],
          [1, 1, 2, 1, 1],
          [0, 1, 1, 1, 0],
          [0, 0, 1, 0, 0],
          [1, 0, 2, 0, 1],
          [1, 1, 1, 1, 1]]


def increase_array(arr: list, coord: tuple, returned_list: list) -> None:
    """ Работает только при условии квадратного массива. """

    if coord in returned_list:
        return
    else:
        returned_list.append((coord[0], coord[1]))
        if coord[1] - 1 >= 0 and arr[coord[1]][coord[0]] == arr[coord[1] - 1][coord[0]]:
            increase_array(arr, (coord[0], coord[1] - 1), returned_list)
        if coord[1] + 1 < len(arr) and arr[coord[1]][coord[0]] == arr[coord[1] + 1][coord[0]]:
            increase_array(arr, (coord[0], coord[1] + 1), returned_list)
        if coord[0] - 1 >= 0 and arr[coord[1]][coord[0]] == arr[coord[1]][coord[0] - 1]:
            increase_array(arr, (coord[0] - 1, coord[1]), returned_list)
        if coord[0] + 1 < len(arr[coord[1]]) and arr[coord[1]][coord[0]] == arr[coord[1]][coord[0] + 1]:
            increase_array(arr, (coord[0] + 1, coord[1]), returned_list)
        return


class MainWindow(Tk):
    def __init__(self, num_array: list):
        super(MainWindow, self).__init__()
        self.title('Painting')
        self.num_array = []
        self.buttons = []
        self.painting_buttons = []

        min_array_len = len(min(num_array))
        for y in num_array:
            self.num_array.append(y[0:min_array_len])

        self.minsize(min_array_len * 50, len(self.num_array) * 50)

        for y_plane in range(len(self.num_array)):
            buff = []
            for x_plane in range(len(self.num_array[y_plane])):
                _btn = Button(self, text=str(self.num_array[y_plane][x_plane]),
                              command=lambda c=(x_plane, y_plane): self.paint_btn(c), bg='#FFFFFF')
                _btn.grid(row=y_plane, column=x_plane, ipadx=25, ipady=25)  # От этой
                buff.append(_btn)
            self.buttons.append(buff)

        self.mainloop()

    def paint_btn(self, coord: tuple) -> None:
        if coord not in self.painting_buttons:
            if self.painting_buttons:
                for _coord in self.painting_buttons:
                    self.buttons[_coord[1]][_coord[0]]['bg'] = '#FFFFFF'
                    self.buttons[_coord[1]][_coord[0]]['activebackground'] = '#FFFFFF'
                self.painting_buttons.clear()
            painting_buttons = []
            increase_array(self.num_array, coord, painting_buttons)
            bg = '#660066'

            for _coord in painting_buttons:
                self.buttons[_coord[1]][_coord[0]]['bg'] = bg
                self.buttons[_coord[1]][_coord[0]]['activebackground'] = bg
                self.painting_buttons.append(_coord)


if __name__ == '__main__':
    MainWindow(number)
    print(number)
