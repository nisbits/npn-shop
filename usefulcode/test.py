
def process():
    path=r"C:\Users\pc\Desktop\pythonproject_upload_file\fileupload\media" 
    path=path + "\\" + str(name)
    in_wb=load_workbook(path)
    in_ws=in_wb.worksheets[0]
    in_rownum=in_ws.max_row+1
    maxr=in_ws.max_row
    for row in range(1,maxr):
        print(str(in_ws["A"+str(row)].value)) 
        in_ws["A"+str(row)].value="ad"
        #print( str(in_ws["U"+str(row)].value) +"a")
    in_wb.save(filename=r"C:\Users\pc\Desktop\pythonproject_upload_file\fileupload\media\output.xlsx")
