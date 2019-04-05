import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import copy
import numpy as np

import networkx as nx

def Main(args=[]):
    if(args==[]):
		
		#Collection of graphs used for testing
        G1_12b = [[0,1,1,0,0,1,0,0,0,0],[1,0,1,0,0,0,0,0,1,0],[1,1,0,1,0,0,0,0,0,0],[0,0,1,0,1,0,0,1,0,0],[0,0,0,1,0,1,1,0,0,0],[1,0,0,0,1,0,1,0,0,0],[0,0,0,0,1,1,0,0,0,1],[0,0,0,1,0,0,0,0,1,1],[0,1,0,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0]]
        positionsG1_12b = {0:(13,1), 1:(15,4), 2:(12, 4), 3:(9.5, 7), 4:(7,4), 5:(6,1), 6:(4,4), 7:(9.5,10), 8:(14,13), 9:(5, 13)}
        p2G1_12b={0:(32,1), 1: (38,8), 2:(26,8), 3:(21,14), 4:(16, 8), 5:(10,1), 6:(4,8), 7:(21,20),8:(33,26),9:(9,26)}
    
        CGraph(G1_12b, "G1_12b",10, p2G1_12b)
        
        #Original 3-reg 6 vertex example from Neil's office
        #Shows how 1-dim can't even get started on regular graphs
        Gorig = [[0,1,1,0,1,0],[1,0,0,1,1,0],[1,0,0,1,0,1],[0,1,1,0,0,1],[1,1,0,0,0,1],[0,0,1,1,1,0]]
        positionsGorig = {0:(0,6), 1:(6,6), 2: (0,0), 3:(6,0), 4:(3, 8),5:(3, -3)}
        #G = CGraph(Gorig, "Gorig", 6,positionsGorig)

        #following graph is ex 2.10 from printout
        G2_10 = [[0,1,0,0,0,0,0,0],[1,0,1,0,1,0,0,0],[0,1,0,1,1,0,1,0],[0,0,1,0,0,0,0,0],[0,1,1,0,0,1,1,0],[0,0,0,0,1,0,0,0],[0,0,1,0,1,0,0,1],[0,0,0,0,0,0,1,0]]
        positionsG2_10={0:(5,40), 1:(10,40),2:(15, 55),  3:(15,75), 4:(15,25), 5:(15, 5), 6:(20, 40), 7: (25, 40)}
        #CGraph(G2_10,"G2_10",8, positionsG2_10)
    
        #Two simple examples
        #G1.1ex from Neils oh for 1-dim w-l
        G1_1 = [[0,1,0,1,0,1],[1,0,0,0,0,1],[0,0,0,0,0,1],[1,0,0,0,1,0],[0,0,0,1,0,0],[1,1,1,0,0,0]]    
        #G1.2 ex N.O.H.
        G1_2 = [[0,1,0,1,1,1],[1,0,0,0,0,1],[0,0,0,0,0,1],[1,0,0,0,0,1],[1,0,0,0,0,0],[1,1,1,1,0,0]]

        #--------------Other examples i might want to use
        #following graph is H1, stabalizes with each vertex in own color class
        H1 = [[0,1,0,1,0,0],[1,0,1,1,1,0],[0,1,0,0,0,1],[1,1,0,0,1,0],[0,1,0,1,0,1],[0,0,1,0,1,0]]
        #following graph is H2, stabelizes with 4 color classes after the 1st coloring
        H2= [[0,1,0,1,0,0],[1,0,1,1,0,1],[0,1,0,0,0,1],[1,1,0,0,1,0],[0,0,0,1,0,1],[0,1,1,0,1,0]]
        #3.20 pg 67 first course in graph theory
        G3_20=[[0,1,1,0,0,0],[1,0,1,0,0,0],[1,1,0,1,0,0],[0,0,1,0,1,1],[0,0,0,1,0,0],[0,0,0,1,0,0]]
        #ex 2.10
        G2_10 = [[0,1,0,0,0,0,0,0],[1,0,1,0,1,0,0,0],[0,1,0,1,1,0,1,0],[0,0,1,0,0,0,0,0],[0,1,0,0,0,1,1,0],[0,0,0,0,1,0,0,0],[0,0,1,0,1,0,0,1],[0,0,0,0,0,0,1,0]]
        #H1 ex 3.30 in A 1st course in graph theory
        GH1=[[0,1,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0],[0,1,0,1,1,1,0,0,0],[0,0,1,0,0,1,0,0,0],[0,0,1,0,0,1,0,0,0],[0,0,1,1,1,0,1,0,0],[0,0,0,0,0,1,0,1,1],[0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,0]]
        #--------------------------------------------------

        print "No arguments"
        
    else:
        print "matrix, desc, n"
        print "args[0]",args[0]
        print "args[1]",args[1]
        print "args[2]-N:" , args[2]
        print "len(args[0])", len(args[0])
        print "matrix: "
        for row in args[0]:
            print row
        print "args[3]", args[3]
        if(args[3]!=[]):
            CGraph(args[0],args[1],args[2], args[3])
            print "pos:", args[3]
        else: 
            CGraph(args[0],args[1],args[2])
    
        return

class CGraph:
    def __init__(self, adjMat, desc,n, graphPos=[]):
        self.G = adjMat #adjacency matrix for the given graph
        self.alg = "1-Dim W-L"
        self.algFName = "1Dim"
        
	self.graphPath = "//export//projects5//graph-cannonize//skoffler2//graph//graphs//1Dim//"
	self.cannonPath ="//export//projects5//graph-cannonize//skoffler2//graph//canonizationfiles//1Dim//"
        self.namesOfGraphsFile="//export//projects5//graph-cannonize//skoffler2//graph//canonizationfiles//1DimGraphNames.txt"

        #pathnames to be used in cgi script
        self.graphPathsrc = "../graphs/1Dim/"
	self.cannonPathsrc ="../canonizationfiles/1Dim/"
        self.namesOfGraphsFilesrc="../canonizationfiles/1DimGraphNames.txt"
        self.adjList=[]
        self.desc = desc
        self.pos = graphPos #layout of the nodes for networkx
        self.vertices = []
        self.iteration = 0
        self.init= True


        self.edgeWidth=5
        self.nodeSizeC=[]
        self.nodeSize=2000
        self.xNodeSize=2500
        self.xLNodeSize=3000
       
        self.fontSize = 14

        self.n = n
        self.cGraphs = []
        self.currGraph = []
        self.colList = []
        self.cGraphs=[]
        self.currExamples=[]
        self.gColorings=[] #list containing the graphColoring obj for each iteration
        self.stableColoring=0
        self.NXG = 0
        self.NXGFinal = 0
        self.NXG_fileNames = []
        self.NXGraphs = []
        self.ccInfo_fileNames=[]
        self.edgeNum = 0 #currently counts the number of "directed" edges       
        self.vColors = ['black','red','blue','orangered','purple','pink', 'magenta','yellow','cyan','saddlebrown','tomato','pink','lightskyblue' , 'darkviolet','mediumpurple','peru','dodgerblue','coral','fuchsia','dimgray','brown','lightsalmon','darkmagenta', 'mediumvioletred']
        if(not self.validateInput()):
            print "Input graph is not a valid encoding"
            print "n=", self.n
            print "adjMat: ", self.G
            return
        #print "graph: ", self.desc 
        #print "adjMat"
        #print self.printGraph(self.G)
        #self.adjMatToAdjList()
        #self.verifyUploadData()

        self.canonizeG()

    def adjMatToAdjList(self):
        for row in range(len(self.G)):
            self.adjList.append([])
            for col in range(len(self.G[row])):
                if(self.G[row][col]==1):
                    self.adjList[row].append(col)
        print
        print "adjList: ", self.adjList
        return
    
    def verifyUploadData(self):
        print "Graph Name:  " + self.desc
        print "gname type:" , type(self.desc) 
        print "gname.len:",len(self.desc)
        print "Graph Adj Mat: "
        print self.G
        print "row by row"
        for row in range(len(self.G)):
            print self.G[row]
        return
        
        
	#code for the one dim algorithm
    def canonizeG(self):

        print "Original graph"
        self.printGraph(self.G)
        self.genOriginalGraph()
        print "Initial coloring"
        self.initColor()
        self.genInitGraph()

        self.gColorings[self.iteration].printClassInfo() 
       	self.ccInfo_fileNames.append(self.gColorings[self.iteration].printClassInfoToFile(self.cannonPathsrc +self.desc))

        
        self.reColor()
        self.genGraph()
         #------- adding the rest of the rounds
        while(self.verifyNotStable()): #while we haven't stabelized
            self.cGraphs.append(self.currGraph)   
            self.reColor()
            self.gColorings[self.iteration].printClassInfo()
            self.ccInfo_fileNames.append(self.gColorings[self.iteration].printClassInfoToFile(self.cannonPathsrc +self.desc))
            self.genGraph()

        self.cGraphs.append(self.currGraph)
        self.stableColoring=self.cGraphs.index(self.currGraph)
         
        print "A stable coloring was reached in the " + str(self.stableColoring) + " iteration."
        print "The cananoziation of graph " + self.desc + "is as follows:"
        self.gColorings[self.iteration].printClassInfo()
        self.ccInfo_fileNames.append(self.gColorings[self.iteration].printClassInfoToFile(self.cannonPathsrc +self.desc))
        self.writeGraphCCFilesToFile()
        return

    
	#maintains 2 files for each canonization, one is a list of 
	#file names of the graphs generated and the other stores  associated 
	#the other stores color class information per round
    def writeGraphCCFilesToFile(self):
        fname = self.graphPath +self.desc+"GraphFileNames.txt"
        f = open(fname, 'w')
        for index in range(len(self.NXG_fileNames)):
           if(index<=self.stableColoring):  
               f.write(self.NXG_fileNames[index]+'\n')
        f.close()

        fname = self.cannonPath+self.desc+"ccInfoFileNames.txt"
        f = open(fname, 'w')
        for index in range(len(self.ccInfo_fileNames)):
            if(index <= self.stableColoring):
                f.write(self.ccInfo_fileNames[index] + '\n')
        f.close()
        print "Done writing files"
        return
		
     #Draw original graph according to input data
	 #using networkX, which uses matplotlib to draw the graphs
    def genOriginalGraph(self):
        n = self.n
        G=nx.Graph()
        plt.figure()
        nodeSize=[]
        fontSize=14
        for n in range(self.n):
            digits = len(str(n))
            G.add_node(n, label=str(n))
            if(digits==1):
                nodeSize.append(self.nodeSize)
            elif(digits==2):
                nodeSize.append(self.xNodeSize)
            else:
                nodeSize.append(self.xLNodeSize)
        self.nodeSizeC = nodeSize
        self.fontSize = fontSize
        
        n = self.n
        for u in range(n):
            for v in range(n):
                if(not u == v): #not a vertice
                    if(self.G[u][v]==1):#edge
                        G.add_edge(u,v)
        if(self.pos == []):
             nx.draw_networkx(G,width = self.edgeWidth, edge_color = 'black' ,node_label_color= "white", node_color = "black", font_color='white', node_size=self.nodeSizeC, font_size=self.fontSize)
        else:             
            nx.draw_networkx(G,width = self.edgeWidth, edge_color = 'black' , node_color = "black", font_color='white', pos = self.pos, node_size=self.nodeSizeC, font_size=self.fontSize)
  
        plt.axis('off')
        string = "OriginalGraph"+ self.desc
        fname = self.graphPath+ string + ".png"
		fnamesrc = self.graphPathsrc+ string + ".png"
        #save filename of graph to access later
        self.NXG_fileNames.append(fnamesrc)
        print "fpath" , fname
		fig = plt.gcf()
		fig.savefig(fname)
        self.NXG = G
        self.NXGraphs.append(G)        
        return
     
	#Generate the initial graph, based on the original graph
    def genInitGraph(self): 
        n = self.n
        G=nx.Graph()
        nodeC = []
        plt.figure()
        gColoring = self.gColorings[0]
        G.add_nodes_from([n-1], label=str(n))
        for node in range(self.n):
            for i in gColoring.colorDecoder.keys():#i= colorclass number
                
                if(gColoring.cGraph[node][node].color==gColoring.colorDecoder[i]):
                    nodeC.append(self.vColors[i])
                    
        for u in range(n):
            for v in range(n):
                if(not u == v): #not a vertice
                    if(self.G[u][v]==1):#edge
                        G.add_edge(u,v)
        if(self.pos == []):          
             nx.draw_networkx(G,width = self.edgeWidth, edge_color = 'black' , node_color = nodeC, font_color='white', node_size=self.nodeSizeC)
        else:
            nx.draw_networkx(G,pos = self.pos,width = self.edgeWidth, edge_color = 'black' , node_color = nodeC, font_color='white', node_size=self.nodeSizeC)
        plt.axis('off')
        string = "C"+str(self.iteration+1)+" " + self.desc
        fname =  self.graphPath + string + ".png"
        fnamesrc =  self.graphPathsrc + string + ".png"

        #save filename of graph to access later
        self.NXG_fileNames.append(fnamesrc)
		fig = plt.gcf()
		fig.savefig(fname)
        self.NXGraphs.append(G)
        self.NXG = G
        return

    def initColor(self):
        G1 = copy.deepcopy(self.G)      
        gColoring = GraphColoring(0, self.n,{})
        self.colList = []      
        G1=gColoring.createEmptyG(self.n)
        for v in range(self.n):
            
            degV = self.G[v].count(1)
            if(self.colList.count(degV)==0):
                self.colList.append(degV)
            G1[v][v]=degV


            
        self.colList.sort()
        print "InitColor graph G1"
        self.printGraph(G1)
        print "self.colList", self.colList
        for cNum in range(len(self.colList)): #create a color class
            cc = []
            for v in range(self.n):
                if(G1[v][v]==self.colList[cNum]):
                    vertex = Vertex(v, self.vColors[cNum])
                    cc.append(vertex)
                    gColoring.cGraph[v][v]=vertex
            gColoring.colorClasses.append(ColorClass(cNum,self.vColors[cNum],cc))
            gColoring.ccNames.append(self.vColors[cNum])
            gColoring.colorDecoder[cNum]= self.vColors[cNum]
            gColoring.neighbors.append(self.colList)

        self.gColorings.append(gColoring)
        #-------------
        for cc in range(len(self.gColorings[len(self.gColorings)-1].colorClasses)):
            for v in self.gColorings[len(self.gColorings)-1].colorClasses[cc].elements:
                G1[v.number][v.number]=cc
        print "InitColor graph G1"
        self.printGraph(G1)
        #-----------

        
        self.currGraph = G1
        self.cGraphs.append(G1)
        return
    #generates a graph at current stage in the algorithm
    def genGraph(self): 
        n = self.n
        NG=nx.Graph()
        nodeC = []
        plt.figure()
        gColoring = self.gColorings[self.iteration]
        NG.add_nodes_from(self.NXG.nodes())
        NG.add_edges_from(self.NXG.edges())
        print "in gengraph currgraph:"
        self.printGraph(self.currGraph)
        for node in range(self.n):
            for i in gColoring.colorDecoder.keys():#i= colorclass number
                if(gColoring.cGraph[node][node].color==gColoring.colorDecoder[i]):
                    nodeC.append(self.vColors[i])
        if(self.pos == []):          
             nx.draw_networkx(NG,width = self.edgeWidth, edge_color = 'black' , node_color = nodeC, font_color='white', node_size=self.nodeSizeC)
        else: 
            nx.draw_networkx(NG,edge_color = 'black',width = self.edgeWidth, node_color = nodeC, font_color='white', node_size=self.nodeSizeC, pos = self.pos)
        plt.axis('off')
        string = "C"+str(self.iteration + 1)+" " + self.desc
        fname = self.graphPath+ string + ".png"
        fnamesrc = self.graphPathsrc+ string + ".png"  

        #save filename of graph to access later
        self.NXG_fileNames.append(fnamesrc)
		plt.savefig(fname, format="PNG")

        self.NXGraphs.append(NG)
        plt.gcf().clear()
        return
    
    #as the algorithm proceeds, nodes individuate from other nodes
	#in their color class and form new color classes
    def reColor(self):
        print "previous rounds cc/neighbor"
        prevCC =  self.gColorings[self.iteration].colorDecoder
        print prevCC
        
        self.colList = []#colors for the round
        g = self.cGraphs[self.iteration]
        oldGCgraph = self.gColorings[self.iteration].cGraph
        self.iteration+=1
        gColoring = GraphColoring(self.iteration, self.n, prevCC,self.gColorings[self.iteration -1])
        newGCgraph = copy.deepcopy(oldGCgraph)
        G1 = copy.deepcopy(g)

        for i in range(self.n):
            nC=[g[i][i]]
            newColor = []
            for v in range(self.n):
                if (self.G[i][v]!=0):newColor.append(g[v][v])
            newColor.sort()
            nC = nC + newColor #new
            print "new color", nC
            if(self.colList.count(nC)==0):self.colList.append(nC)
            G1[i][i]=nC
        print "reColor Graph"
        self.printGraph(G1)
        self.colList.sort()
        neighborInfo =[]
        for cNum in range(len(self.colList)): #create a color class
            cc = []
            
            for v in range(self.n):
                if(G1[v][v]==self.colList[cNum]):
                    vertex = oldGCgraph[v][v]
                    vertex.color=self.vColors[cNum]
                    cc.append(vertex)
                    print "G1[", v, "][",v,"]:", G1[v][v][1:]
                    neighborInfo[cNum]= G1[v][v][1:]

                    G1[v][v]=vertex.color
                    
                    if(neighborInfo.count(G1[v][v][1:])==0):neighborInfo.append(G1[v][v][1:])
                    newGCgraph[v][v]=vertex
            gColoring.colorClasses.append(ColorClass(cNum,self.vColors[cNum],cc)) #don't think i need neighbor info here
            gColoring.ccNames.append(self.vColors[cNum])
            gColoring.colorDecoder[cNum]= self.vColors[cNum]
           
            print "new color decoder-neighbor"
            print gColoring.colorDecoder[cNum]
            #-------------
            gColoring.neighbors=neighborInfo
        #-----------------          
        self.currGraph = G1
        gColoring.cGraph=newGCgraph
        self.gColorings.append(gColoring)
        return
 
        
#-------------------------------------------------------------
    def loadCurrExamples(self):
        try:
            f = open(self.namesOfGraphsFile,'r')
            print "File opened"
            for fname in f.readlines():
                    print "graphName-" + fname
                    fn = str.rstrip(fname, '\n')
                    print "fn", fn
                    self.currExamples.append(fn)
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except:
           print "io error"
           print "CurrExamples: ", self.currExamples
        else:
            f.close()

        print "CurrExamples: ", self.currExamples
        return


    #just checks for graph name collision    
    def addNewExample(self):
        if(self.desc in self.currExamples):
            print "This graph has already been canonized."
            return False
        else:
            f = open(self.namesOfGraphsFile,'a')
            f.write(self.desc+'\n')
        return

    #test if the coloring is stable
    def verifyNotStable(self):
        bool = False
        if(len(self.gColorings[len(self.gColorings)-1].colorClasses)==len(self.gColorings[len(self.gColorings)-2].colorClasses)): #stable
            bool = True
        return bool

    def printGraph(self,g):
        for row in range(self.n):
            print g[row]
        return
    
    def validateInput(self):
        valid = True
        for row in range(len(self.G)):
            if(len(self.G[row])!=self.n):
                print "not n"
                print "self.G[row]", self.G[row]
                print "len self.G[row]", len(self.G[row])
                print "self.n",self.n
                
                return False
            for col in range(len(self.G[row])):
                if(self.G[row][col] not in [0,1]):
                    print "not 0,1"
                    return False
        return valid

class GraphColoring():
    def __init__(self, iteration,n , prevCC,oldCGraph=[]):
        self.oldCGraph = oldCGraph #some version of a graph from the last iteration
        self.iteration = iteration
        self.ccNames = []
        self.colorClasses = [] #contains a list of color class objects rep. the color classes that exist in this coloring/iteration of the graph
        self.colorDecoder = {} #key=newColorName:value=sorted list of colorset from this round that corresponds to this new color
        #cGraph contains a matrix with updated vertex/edge/non-edge elts
        self.cGraph = self.createEmptyG(n)
        self.neighbors=[]
        self.prevCC=prevCC
       

    def createEmptyG(self,n):
        z = [[0 for j in range(n)] for i in range(n)]
        return z

    def getNeighborInfo(self, ccNum):
        if(self.iteration<1):
            return ''
        else:
            print"hello"
            info = "nhbrs:"
        
            neighbors = self.neighbors[str(ccNum)]
            print "neighbor[cc="+ str(ccNum)+"]", neighbors
            for k in self.prevCC.keys():
                if(neighbors.count(k)>0): #have count number of neighbors of color(ccNum)
                    info = info + " " + str(neighbors.count(k)) + " " + str(self.prevCC[k])
            return info   
    
    def printClassInfo(self):
        print "self.neighbors: " , self.neighbors
        print "prevcc: " , self.prevCC
        for cc in self.colorClasses:
            cc.printClassInfo()

    def printClassInfoToFile(self,fname1):
       
        fname = fname1 + "CC"+str(self.iteration+1)+".txt"
        f = open(fname, 'w')
        if(self.iteration==1):
            f.write("New color classes determined by number of neighbors from each color class in previous round"+ '\n')
       # for neighbor in self.colorClasses[cc.number].neighborInfo:
        for cc in self.colorClasses:
            neighborStr = "_"+ self.getNeighborInfo(cc.number)
            f.write(cc.printClassInfoToFile()+ " " +
            neighborStr + '\n')
        f.close()
        return fname   


class ColorClass():
    def __init__(self, number, color, elements, nInfo=[]):
        self.number = number #number of the colorclass
        self.color=color #color of this class
        self.elements = elements #list of elements in this color class
        #self.neighborInfo=nInfo

    #prints class info
    def printClassInfo(self):
        vs = "Vertices: {"
        print "Color class("+str(self.number)+"):"+self.color+ " contains",
        print vs,
        for c in range(len(self.elements)):
            if(c==len(self.elements)-1):
                print self.elements[c].descV(),
            else:
                print self.elements[c].descV()+",",
        print "}"

    #returns string rep info for this class to be stored in cc file
    def printClassInfoToFile(self):
        colorClassString = str(self.number) +"_"+ str(self.color)+ "_"
        vs = "V{"       
        colorClassString+=vs
        for c in range(len(self.elements)):
            if(c==len(self.elements)-1):
                 colorClassString+=self.elements[c].descV()
            else:
                 colorClassString+= self.elements[c].descV()+","
        colorClassString+= "}"
        return colorClassString
            
class Vertex:
    def __init__(self, number, color="black"):
        self.number = number
        self.color = color
                                                              
    def printV(self):
        print str(self.number)
        
    def descV(self):
        return str(self.number)

Main()
