from Struct.fordFulkerson import fordFulkerson

def main():
    path = 'Dataset\instance1.txt'
    grafo = fordFulkerson(path)
    x = grafo.solve(17,12)
    print(x.node)
    


main()