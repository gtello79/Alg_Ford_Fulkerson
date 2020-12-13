from Struct.fordFulkerson import fordFulkerson

def main():
    path = 'Dataset\instance1.txt'
    grafo = fordFulkerson(path)
    p = grafo.getRoutes(17,12)
    for x in p:
        print(x.nodes) 
    


main()