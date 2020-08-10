# if event.key == pygame.K_a:
#     solve(self.grid)
# if event.key == pygame.K_o:
#     self.grid[self.selected[1]][self.selected[0]] = 0
#     self.incorrect_cells.remove(self.selected)
# if event.key == pygame.K_y:
#     self.grid = [[0 for x in range(9)] for x in range(9)]
#     self.lockedcells = []
#     while self.running:
#         self.playing_events()
#         self.playing_update_ai()
#         self.playing_draw_ai()
# if self.selected and self.selected in self.changed_cells:
#     if event.key == pygame.K_RETURN:
#         num = self.tempgrid[self.selected[1]][self.selected[0]]
#         self.change_side(self.grid, self.tempgrid, self.selected, self.lockedcells)
#         self.cellchanged = True
#         self.cck = self.selected
#         self.checkRows(self.grid[self.cck[1]][self.cck[0]], self.selected[1], self.selected)
#         self.checkColumns(self.grid[self.cck[1]][self.cck[0]], self.selected[0], self.selected)
#         self.checksmallgrid(self.cck, self.grid[self.cck[1]][self.cck[0]])
#         print(self.selected)
#     def checkRows(self,num1,p,index):
#         for yidx,i in enumerate(self.grid):
#             for xidx,numss in enumerate(i):
#                 if numss == num1 and xidx != index[0]:
#                     print("Wrong")
#                     self.incorrect_cells.append(index)
#                     return  False
#         self.correctcells.append(index)
#         print("Rightrow")
#         return  True
#     def checkColumns(self,num1,p,index):
#         for yidx,i in enumerate(self.grid):
#             print(i)
#             if i[p] == num1 and yidx != index[1]:
#                 print(i[1])
#                 print("Wrong")
#                 self.incorrect_cells.append(index)
#                 return False
#         self.correctcells.append(index)
#         print("Right")
#         return True
#     def checksmallgrid(self,pos,num):
#         box_x = pos[0] // 3
#         box_y = pos[1] // 3
#         print(box_x,box_y)
#
#         for i in range(box_y * 3, box_y * 3 + 3):
#             for j in range(box_x * 3, box_x * 3 + 3):
#                 if self.grid[i][j] == num and [j, i] != pos:
#                     self.incorrect_cells.append(pos)
#                     print("Wrong")
#                     return  False
#         print("Right")
#
#         return True
#     def getpuzzle(self,dif:str):
#         url = "https://www.websudoku.com/?level=1"
#         data = requests.get(url)
#         soup = BeautifulSoup(data.text,'html.parser')
#         # print(soup)
#         a = ['f00', 'f01', 'f02', 'f03', 'f04', 'f05', 'f06', 'f07', 'f08', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15',
#              'f16', 'f17', 'f18', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25', 'f26', 'f27', 'f28', 'f30', 'f31', 'f32',
#              'f33', 'f34', 'f35', 'f36', 'f37', 'f38', 'f40', 'f41', 'f42', 'f43', 'f44', 'f45', 'f46', 'f47', 'f48',
#              'f50', 'f51', 'f52', 'f53', 'f54', 'f55', 'f56', 'f57', 'f58', 'f60', 'f61', 'f62', 'f63', 'f64', 'f65',
#              'f66', 'f67', 'f68', 'f70', 'f71', 'f72', 'f73', 'f74', 'f75', 'f76', 'f77', 'f78', 'f80', 'f81', 'f82',
#              'f83', 'f84', 'f85', 'f86', 'f87', 'f88']
#         data = []
#         for i in a:
#             data.append(soup.find('input',id=i))
#         board = [[0 for x in range(9)] for x in range(9)]
#         for index,cell in enumerate(data):
#
#             board[int(index//9)][index%9] = int(cell['value'])
#
#         return  board
# def checkallcells(self):
#     self.checkrowswhendone()
#     # self.checkColumnswhendone()
#     # self.checksmallgridwhendone()
#
#
# def checkrowswhendone(self):
#     for yidx, row in enumerate(self.grid):
#         checked = []
#         for xidx in range(9):
#             if self.grid[yidx][xidx] in checked:
#                 print("WRONG")
#
#     return True
#
#
# def checkColumnswhendone(self):
#     for xidx in range(9):
#         possiblesc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         for yidx, row in enumerate(self.grid):
#             if self.grid[yidx][xidx] in possiblesc:
#                 possiblesc.remove(self.grid[yidx][xidx])
#                 if [xidx, yidx] in self.incorrect_cells:
#                     self.incorrect_cells.remove([xidx, yidx])
#             else:
#                 if [xidx, yidx] not in self.lockedcells:
#                     self.incorrect_cells.append([xidx, yidx])
#                 if [xidx, yidx] in self.lockedcells:
#                     for k, row in enumerate(self.grid):
#                         if self.grid[k][xidx] == self.grid[yidx][xidx] and [xidx, k] not in self.lockedcells:
#                             self.incorrect_cells.append([xidx, k])
#
#
# def checksmallgridwhendone(self):
#     for x in range(3 + 1):
#         for y in range(3 + 1):
#             possibless = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#             print("resetting")
#             for i in range(3 + 1):
#                 for j in range(3 + 1):
#                     # print(x*3+i,y*3+j)
#                     xidx = x * 3 + i
#                     yidx = y * 3 + j
#                     if self.grid[yidx][xidx] in possibless:
#                         possibless.remove(self.grid[yidx][xidx])
#                     else:
#                         if [xidx, yidx] not in self.lockedcells and [xidx, yidx] not in self.incorrect_cells:
#                             self.incorrect_cells.append([xidx, yidx])
#                             # print("Wrong")
#                             return False
#                         if [xidx, yidx] in self.lockedcells:
#                             for k in range(3):
#                                 for ll in range(3):
#                                     xidx2 = x * 3 + k
#                                     yidx2 = y * 3 + k
#                                     if self.grid[yidx2][xidx2] == self.grid[yidx][xidx] and [xidx2,
#                                                                                              yidx2] not in self.lockedcells:
#                                         self.incorrect_cells.append([xidx2, yidx2])

