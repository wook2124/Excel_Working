import openpyxl

load_wb = openpyxl.load_workbook("r'C:\Users\YoungWook Kim\Downloads\Tablet.xlsx")
#시트 이름으로 불러오기
load_ws = load_wb['Sheet1']
 
#셀 주소로 값 출력
print(load_ws['A1'].value)
 
#셀 좌표로 값 출력
print(load_ws.cell(1,2).value)
