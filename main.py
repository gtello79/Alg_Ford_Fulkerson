from Struct.fordFulkerson import fordFulkerson

def main():
    path = 'Dataset\instance1.txt'
    grafo = fordFulkerson(path)
    print(grafo.routes)



main()