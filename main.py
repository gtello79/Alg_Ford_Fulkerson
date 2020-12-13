from Struct.fordFulkerson import fordFulkerson

def main():
    path = 'Dataset\instance5.txt'
    grafo = fordFulkerson(path)
    x = grafo.solve(0,89)
    print(x.node)
    '''
    p = grafo.getRoutes(17,12)
    for x in p:
        print(x.nodes) 
    '''


main()